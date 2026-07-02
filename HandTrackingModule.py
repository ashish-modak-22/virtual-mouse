import cv2
import mediapipe as mp


class HandDetector:


    def __init__(self, maxHands = 2, detectionCon = 0.5): 

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands = maxHands,
            min_detection_confidence = detectionCon
        )

        self.mp_draw = mp.solutions.drawing_utils
        self.results = None
        self.tipId = [4, 8, 12, 16, 20]


    def findHands(self, img):

        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:

            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    img,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS  
                )

        return img
    

    def findPosition(self, img, handNo = 0, draw = True):

        self.lmList = []
        h, w, c = img.shape

        if self.results and self.results.multi_hand_landmarks:
            # Get first detected hand
            hand = self.results.multi_hand_landmarks[handNo]

            for id, landmark in enumerate(hand.landmark):
                cx = int(landmark.x * w)
                cy = int(landmark.y * h)
                self.lmList.append([id, cx, cy])

        return self.lmList
    

    def findDistance(self, p1, p2):

        x1,y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2,y2 = self.lmList[p2][1], self.lmList[p2][2]
        length = ((x2-x1)**2 + (y2-y1)**2)**0.5

        return length
    

    def fingersUp(self):
        fingers = []

        
        # Thumb
        if self.lmList[self.tipId[0]][1] > self.lmList[self.tipId[0]-1][1]:
            fingers.append(1)

        else:
            fingers.append(0)

        # Other 4 fingers
        for id in range(1, 5):
        
            # In opencv , reverse orientation is used
            if self.lmList[self.tipId[id]][2] < self.lmList[self.tipId[id]-2][2]:
                fingers.append(1)

            else:
                fingers.append(0)

        return fingers
    

    def detectGesture(self):
        fingers = self.fingersUp()
        
        if fingers == [0, 1, 0, 0, 0]:
            return "Move"
        
        elif fingers == [0, 1, 1, 0, 0]:
            return "Left_Click"
        
        elif fingers == [0, 1, 0, 0, 1]:
            return "Right_Click"
        
        elif fingers == [0, 1, 1, 1, 1]:
            return "Scroll"
        
        
        return "NONE"
    
