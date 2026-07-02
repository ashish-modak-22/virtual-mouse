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
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-2ea44f?style=for-the-badge&logo=windowsterminal&logoColor=white)
 
</div>

---

## 📖 Table of Contents
 
- [Overview](#-overview)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Architecture & Module Breakdown](#-architecture--module-breakdown)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Gesture Controls](#-gesture-controls)
- [Kalman Filter — Motion Smoothing](#-kalman-filter--motion-smoothing)
- [Configuration](#-configuration)
- [Performance](#-performance)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)
- [Contact](#-contact)

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
