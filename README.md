# 🖐️ AI Virtual Mouse
 
<div align="center">
 
### Control your computer's mouse using nothing but hand gestures — powered by Computer Vision, MediaPipe, and Kalman Filtering.

---

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-00A79D?style=for-the-badge&logo=google&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-automation-FF6F00?style=for-the-badge&logo=python&logoColor=white)
![autopy](https://img.shields.io/badge/autopy-mouse%20control-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-numerical%20computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge)](https://opensource.org/licenses/Apache-2.0)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-2ea44f?style=for-the-badge&logo=windowsterminal&logoColor=white)
 
</div>

---

## 🌟 Overview
 
**AI Virtual Mouse** is a real-time, computer-vision-based system that replaces the physical mouse with **hand gestures** captured through a standard webcam. It leverages **Google's MediaPipe Hands** solution for high-fidelity 21-point hand landmark detection, combined with **OpenCV** for image processing and a custom **Kalman Filter** for smooth, jitter-free cursor motion.

The project is built with a modular architecture — separating hand detection, gesture recognition, motion smoothing, and system-level mouse control into independent, reusable components.
 
> Move your cursor, click, right-click, drag, and scroll — all without touching a physical mouse.
 
---

## ✨ Key Features
 
- 🖱️ **Cursor Movement** — Control the mouse pointer in real time using your index finger.
- 👆 **Left Click** — Trigger a left click via a pinch gesture between index and middle fingers.
- ✌️ **Right Click** — Perform a right click using a dedicated finger combination.
- 📜 **Velocity-Based Scrolling** — Scroll up/down dynamically based on hand movement speed.
- 🎯 **Kalman Filter Smoothing** — Physically-modeled motion prediction eliminates jitter while preserving responsiveness.
- 📊 **Real-Time FPS Counter** — Live performance monitoring overlay on the camera feed.
- 🧩 **Modular Codebase** — Cleanly separated modules for detection, filtering, and control logic.
- 🖥️ **Cross-Platform** — Works on Windows, macOS, and Linux (subject to `autopy` support).

---

 
## ⚙️ How It Works
 
```
┌─────────────────┐     ┌──────────────────┐     ┌───────────────────┐
│   Webcam Feed   │ ──▶ │  Hand Detection  │ ──▶ │  Landmark         │
│   (OpenCV)      │     │  (MediaPipe)     │     │  Extraction       │
└─────────────────┘     └──────────────────┘     └───────────────────┘
                                                            │
                                                            ▼
┌─────────────────┐       ┌──────────────────┐       ┌───────────────────┐
│ System Mouse    │  ◀──  │  Kalman Filter   │ ◀──   │  Gesture          │
│ Control         │       │  (Smoothing)     │       │  Recognition      │
│ (autopy/pyautogui)      └──────────────────┘       └───────────────────┘
└─────────────────
```
1. **Capture** — A live video stream is captured frame-by-frame via OpenCV.
2. **Detect** — Each frame is passed to MediaPipe Hands, which returns 21 hand landmarks.
3. **Interpret** — Finger positions are analyzed to detect which fingers are raised, and a gesture is classified as Move, Left Click, Right Click, Scroll.
4. **Smooth** — Raw coordinates from the "Move" gesture are passed through a Kalman Filter to predict and smooth cursor motion.
5. **Act** — The final, smoothed coordinates are mapped to screen space and dispatched as native OS-level mouse events.
---

## 🛠️ Tech Stack
 
| Category              | Technology                                   |
|------------------------|-----------------------------------------------|
| Language               | Python 3.8+                                   |
| Computer Vision         | OpenCV                                        |
| Hand Tracking           | MediaPipe Hands                               |
| Numerical Computing     | NumPy                                         |
| Motion Filtering        | Kalman Filter (via `cv2.KalmanFilter`)        |
| Mouse Automation        | autopy, PyAutoGUI                             |
 
---

## 📁 Project Structure
 
```
virtual-mouse/
│
├── HandTrackingModule.py     # Hand detection & gesture recognition (MediaPipe wrapper)
├── KalmanFilter.py           # Kalman Filter class for cursor motion smoothing
├── AI_Virtual_Mouse.py       # Main application — camera loop & control logic
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```
 
---
## 🧩 Architecture & Module Breakdown

### 1. `HandTrackingModule.py`
Wraps MediaPipe's Hands solution into a reusable `HandDetector` class.

**Responsibilities:**
- Detecting hands and drawing landmarks (`findHands`)
- Extracting pixel-space landmark coordinates (`findPosition`)
- Calculating Euclidean distance between any two landmarks (`findDistance`)
- Determining which fingers are raised (`fingersUp`)
- Classifying the current gesture (`detectGesture`) into one of: `Move`, `Left_Click`, `Right_Click`, `Scroll`, or `NONE`

### 2. `KalmanFilterModule.py`
A dedicated module implementing a **4-state Kalman Filter** (`x, y, vx, vy`) using OpenCV's built-in `cv2.KalmanFilter`.

**Responsibilities:**
- Predicting the next cursor position based on motion history
- Correcting predictions using real (noisy) landmark measurements
- Returning smoothed `(x, y)` coordinates every frame

### 3. `AI_Virtual_Mouse.py`
The orchestrator — ties everything together.

**Responsibilities:**
- Capturing and preprocessing webcam frames
- Invoking `HandDetector` for landmark detection and gesture classification
- Mapping hand-space coordinates to screen-space coordinates
- Passing raw coordinates through the Kalman Filter
- Executing OS-level mouse actions (move, click, right-click, drag, scroll)
- Rendering visual feedback (bounding box, cursor indicators, FPS counter)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A working webcam
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ashish-modak-22/virtual-mouse.git
   cd AI-Virtual-Mouse
   ```
2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
  > ⚠️ **Note:** `autopy` may require additional system-level build tools (e.g., `cmake`, Xcode Command Line Tools on macOS, or `python3-dev` on Linux). Refer to the [autopy documentation](https://github.com/autopilot-rs/autopy) if installation fails.

### Running the Application

```bash
python AI_Virtual_Mouse.py
```

- A webcam window titled **"Virtual Mouse"** will open.
- Position your hand within the green bounding box for best tracking accuracy.
- Press **`s`** to quit the application.

---

## ✋ Gesture Controls

| Gesture                          | Finger Pattern                  | Action              |
|-----------------------------------|----------------------------------|----------------------|
|  Index finger only               | `[0, 1, 0, 0, 0]`                | Move Cursor          |
|  Index + Middle finger           | `[0, 1, 1, 0, 0]`                | Left Click            |
|  Pinky  + Index finger          | `[0, 1, 0, 0, 1]`                | Right Click           |
|  Four fingers (no thumb)         | `[0, 1, 1, 1, 1]`                | Scroll                |

> Finger states are represented as a binary array `[Thumb, Index, Middle, Ring, Pinky]`, where `1` = extended, `0` = folded.

---

## 🎯 Kalman Filter — Motion Smoothing

Raw hand-tracking coordinates are inherently noisy due to camera resolution limits, lighting conditions, and natural hand tremor. Instead of simple exponential smoothing, this project uses a **Kalman Filter** for statistically optimal motion estimation.

### `Core Concept`
Every frame, the filter performs a two-step cycle:

1. **Predict** — Estimates the next cursor position using a motion model (position + velocity).
2. **Correct** — Blends that prediction with the actual noisy measurement, weighted by a dynamically computed **Kalman Gain**.

Because the filter tracks **velocity as a hidden state** (not directly measured, but inferred), it can distinguish between:
- **Involuntary jitter** (near-zero velocity) → suppressed
- **Intentional fast movement** (rising velocity) → tracked and followed responsively

### `State Model`

| State Variable | Description                  |
|------------------|-------------------------------|
| `x`              | Cursor X position              |
| `y`              | Cursor Y position              |
| `vx`             | Velocity in X direction        |
| `vy`             | Velocity in Y direction        |


### `Tunable Parameters`

| Parameter              | Effect                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| `process_noise`          | Trust in the motion model. Lower → smoother but slightly delayed.        |
| `measurement_noise`      | Trust in raw tracking data. Higher → more smoothing, more lag on fast moves. |

---

## 🔧 Configuration

Key constants can be adjusted directly in `AI_Virtual_Mouse.py`:

| Constant              | Default | Description                                  |
|-------------------------|---------|-----------------------------------------------|
| `CAMERA_WIDTH`           | `640`   | Webcam capture width                          |
| `CAMERA_HEIGHT`          | `480`   | Webcam capture height                         |
| `REDUCED_FRAME`          | `100`   | Margin defining the active tracking region    |
| `SCROLL_SPEED`           | `5`     | Base scroll sensitivity                       |
| `maxHands`               | `1`     | Maximum number of hands tracked simultaneously |
| `detectionCon`           | `0.5`   | Minimum hand detection confidence threshold   |

---

## 📈 Performance

- Real-time FPS is displayed in the top-left corner of the video feed.
- Performance depends primarily on:
  - Webcam resolution
  - CPU capability (MediaPipe inference is CPU-bound by default)
  - MediaPipe model complexity settings
- Typical performance on a mid-range CPU: **20–30 FPS** at 640×480 resolution.

---

## 🩺 Troubleshooting

| Issue                                   | Possible Cause                          | Solution                                                        |
|-------------------------------------------|-------------------------------------------|---------------------------------------------------------------------|
| Webcam window doesn't open                | Camera in use by another application       | Close other apps using the webcam                                    |
| Cursor lags significantly                 | High `measurement_noise` or low FPS         | Lower `measurement_noise`, reduce camera resolution                   |
| Cursor jitters despite Kalman filter      | `process_noise` too high                    | Decrease `process_noise` value                                       |
| `autopy` fails to install                 | Missing build dependencies                  | Install `cmake` and platform-specific build tools                    |
| Hand not detected                         | Poor lighting / hand outside frame          | Improve lighting, keep hand within the green bounding box            |

---

## 📄 License


## 📄 License
 
This project is open source and available under the [Apache License 2.0](License).

---

## 🙏 Acknowledgements

- [MediaPipe](https://developers.google.com/mediapipe) by Google — for the hand landmark detection solution
- [OpenCV](https://opencv.org/) — for image processing and Kalman Filter implementation
- [autopy](https://github.com/autopilot-rs/autopy) & [PyAutoGUI](https://pyautogui.readthedocs.io/) — for cross-platform mouse automation

---

<div align="center">

⭐ If you found this project useful, consider giving it a star on GitHub!

</div>

