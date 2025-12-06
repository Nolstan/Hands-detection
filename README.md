# Real-Time Hand Detection with MediaPipe

This project uses OpenCV and Google's MediaPipe library to perform real-time hand detection and landmark tracking from a webcam feed.

## Features

*   Detects up to 4 hands simultaneously.
*   Draws 21 hand landmarks and their connections in real-time.
*   Flips the video feed horizontally for a more intuitive mirror-like view.
*   Optimized for speed by using a lower resolution (640x480).

## Requirements

You will need Python 3 installed, along with the following libraries:

*   `opencv-python`
*   `mediapipe`

You can install these dependencies using pip:

```bash
pip install opencv-python mediapipe
```

## How to Run

1.  Make sure you have a webcam connected to your computer.
2.  Navigate to the project directory in your terminal.
3.  Run the script:
    ```bash
    python main.py
    ```
4.  A window will open showing the webcam feed. Press the **'q'** key to close the window and stop the script.
