import cv2
import numpy as np



class MouseKalmanFilter:
    def __init__(self, process_noise=1e-3, measurement_noise=1e-1):

        # Initialize Kalman Filter with 4 state variables (x, y, dx, dy) and 2 measurements (x, y)
        self.kf = cv2.KalmanFilter(4, 2)

        
        # Measurement matrix maps state to measurement space( We observe only x and y)
        self.kf.measurementMatrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ], np.float32)


        # This transition matrix defines motion model( Constant velocity model)
        self.kf.transitionMatrix = np.array([
            [1, 0, 1, 0],   # x = x + dx
            [0, 1, 0, 1],   # y = y + dy
            [0, 0, 1, 0],   # dx remains same
            [0, 0, 0, 1]    # dy remains same
        ], np.float32)


        # Process noise controls how much we trust the model prediction
        self.kf.processNoiseCov = np.eye(4, dtype=np.float32) * process_noise

        # Measurement noise controls how much we trust incoming measurements
        self.kf.measurementNoiseCov = np.eye(2, dtype=np.float32) * measurement_noise

        # Flag to check if filter has been initialized with first measurement
        self.initialized = False

    def update(self, x, y):

        measurement = np.array([[np.float32(x)], [np.float32(y)]])

        if not self.initialized:
          
            self.kf.statePre = np.array([[x], [y], [0], [0]], np.float32)
            self.kf.statePost = np.array([[x], [y], [0], [0]], np.float32)
            self.initialized = True

        self.kf.predict()
        corrected = self.kf.correct(measurement)

        return corrected[0, 0], corrected[1, 0]
    
