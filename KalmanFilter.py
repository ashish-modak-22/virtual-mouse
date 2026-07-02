import cv2
import numpy as np

class MouseKalmanFilter:
    def __init__(self, process_noise=1e-3, measurement_noise=1e-1):
       
        self.kf = cv2.KalmanFilter(4, 2)

        self.kf.measurementMatrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ], np.float32)

        self.kf.transitionMatrix = np.array([
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], np.float32)

        self.kf.processNoiseCov = np.eye(4, dtype=np.float32) * process_noise

        self.kf.measurementNoiseCov = np.eye(2, dtype=np.float32) * measurement_noise

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
    