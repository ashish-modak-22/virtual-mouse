import cv2
import numpy as np
import time
import pyautogui
import autopy
import HandTrackingModule as htm
import KalmanFilter as kf



################# Declaring constants ####################

CAMERA_WIDTH , CAMERA_HEIGHT = 640, 480
SCREEN_WIDTH, SCREEN_HEIGHT = autopy.screen.size()
REDUCED_FRAME = 100
SMOOTHENING_VALUE = 5
SCROLL_SPEED = 5
SCROLL_BUFFER = 0

###########################################################


# Previous and current cursor positions(used for smoothing and movement calculation)
x_previous_location, y_previous_location = 0, 0
x_current_location, y_current_location = 0, 0

# Used to calculate the FPS
previous_time = 0

# Gesture state flags to prevent mouse actions
mouse_down = False
right_click_active = False
scroll_active = False

# Variables used for velocity based scrolling
prev_y = 0
prev_y_time = 0
scroll_velocity = 0


###########################################################



detector = htm.HandDetector(maxHands=1)
filter = kf.MouseKalmanFilter()



# Initialize webcam capture 
cap = cv2.VideoCapture(0)


# Set camera width (property 3) and height (property 4) for stable tracking performance
cap.set(3, CAMERA_WIDTH)
cap.set(4, CAMERA_HEIGHT)



while True:

    success, img = cap.read()

    img = detector.findHands(img)

    lmList = detector.findPosition(img)


    if len(lmList)!=0:

        x_index_finger, y_index_finger = lmList[8][1:]
        x_middle_finger, y_middle_finger = lmList[12][1:]

        

        gesture = detector.detectGesture()



        cv2.rectangle(
                img,
                (REDUCED_FRAME, REDUCED_FRAME),
                (CAMERA_WIDTH - REDUCED_FRAME, CAMERA_HEIGHT - REDUCED_FRAME),
                (0, 255, 0),
                2
            )
        


        if gesture == "Move":


            x_converted = np.interp(x_index_finger, (REDUCED_FRAME, CAMERA_WIDTH - REDUCED_FRAME), (0, SCREEN_WIDTH))


            y_converted = np.interp(y_index_finger, (REDUCED_FRAME, CAMERA_HEIGHT-REDUCED_FRAME), (0, SCREEN_HEIGHT))



            x_current_location, y_current_location = filter.update(x_converted, y_converted)


            
            autopy.mouse.move(SCREEN_WIDTH - x_current_location, y_current_location)


            cv2.circle (
                img,
                (x_index_finger, y_index_finger),
                15,
                (255, 0, 0),
                cv2.FILLED
            )


            x_previous_location, y_previous_location = x_current_location, y_current_location


        if gesture == "Left_Click":

            length = detector.findDistance(8, 12)
            

            if length < 30:

                if drag_timer_start is None:
                    drag_timer_start = time.time()

                cv2.circle(
                   img,
                   (x_index_finger, y_index_finger),
                   10,
                   (0, 255, 0),
                   cv2.FILLED
                )

                cv2.circle(
                   img,
                   (x_middle_finger, y_middle_finger),
                   10,
                   (0, 255, 0),
                   cv2.FILLED
                )


                if not mouse_down:

                    autopy.mouse.click()
                    mouse_down = True

            else:

                mouse_down = False

        drag_timer_start = None

            

        if gesture == "Right_Click":

            if not right_click_active:
                autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
                right_click_active = True

        else:
            right_click_active = False



        if gesture == "Scroll":

            current_time = time.time()

            dy = y_index_finger - prev_y
            dt = current_time - prev_y_time

            if dt > 0:

                scroll_velocity = dy / dt   # speed calculation

                if abs(scroll_velocity) > 50:

                    if scroll_velocity < 0:
                        pyautogui.scroll(int(min(120, abs(scroll_velocity))))
                    else:
                        pyautogui.scroll(-int(min(120, abs(scroll_velocity))))

            prev_y = y_index_finger
            prev_y_time = current_time




    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time


    cv2.putText(
        img,
        str(int(fps)),
        (20, 50),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (255, 0, 0),
        3
    )


    cv2.imshow("Virtual Mouse", img)

    if cv2.waitKey(1) == ord('s'):
        break


cap.release()

cv2.destroyAllWindows()
