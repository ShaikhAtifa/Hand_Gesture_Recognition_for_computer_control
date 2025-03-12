# Hand_Gesture_Recognition_for_computer_control
Here's a README for your project, tailored for a GitHub repository. It describes the functionality, setup, and use of the code you've supplied:

---

# Hand Gesture Controlled Presentation & Media Controller

The project allows a presentation and media playback to be controlled using hand gestures through a webcam. The project uses hand tracking to trigger actions like navigation of slides, drawing annotations, changing screen brightness, and managing media playback.

## Features
- Slide Navigation: Navigate between presentation slides with certain hand gestures.
- Annotation Drawing: Draw on slides with gestures.
- Screen Brightness Control: Brighten or darken the screen through hand gestures.
- Media Control: Pause or play media through a gesture.
- Window Management: Maximize and minimize the presentation window.

## Prerequisites
Make sure to have the following libraries installed:

- OpenCV (`opencv-python`)
- PyAutoGUI (`pyautogui`)
- PyGetWindow (`pygetwindow`)
- cvzone (`cvzone`)
- Screen Brightness Control (`screen_brightness_control`)
- NumPy (`numpy`)

You may install these with pip:

```bash
pip install opencv-python pyautogui pygetwindow cvzone screen_brightness_control numpy
```

## Setup

1. Clone the repository or download the project files.
2. Put your presentation slides inside a folder called `Presentation`. The images should be named in a manner so that they will load in proper order (e.g., slide1.jpg, slide2.jpg, etc.).
3. Make sure your webcam is configured and available for the script.

## How to Use

1. Run the script:
    ```bash
python hand_gesture_presentation.py
```


2. The application will display a window displaying your webcam and the current slide.
3. Use the following gestures to move to the next or previous slide:
    - Left (Swipe Left): Go to the previous slide.
    - Right (Swipe Right): Go to the next slide.
- Pointer Gesture (Index Finger Up): Show a pointer on the slide.
    - Draw Gesture (Index Finger Up): Start drawing annotations on the slide.
    - Erase Gesture (Index & Middle Fingers Up): Erase annotations.
    - Brightness Up Gesture (Thumb & Index Finger Up): Increase screen brightness.
- Brightness Down Gesture (Thumb, Index, and Middle Finger Up): Dim the screen brightness.
    - Minimize Window Gesture (Ring & Pinky Fingers Up): Minimize the slide window.
    - Maximize Window Gesture (Middle, Ring, and Pinky Fingers Up): Maximize the slide window.
    - Play/Pause Media Gesture (All Fingers Up): Pause or play media.

4. Press 'q' to quit the program.

## Code Explanation

- Hand Detection: Hand gestures are detected and finger locations tracked using `cvzone` HandTrackingModule.
- Slide Navigation: Hand gestures translate to navigating left or right through slides.
- Annotation Drawing: Index finger can be used to draw annotations on the slides.
- Brightness Control: Screen brightness controlled with gestures.
- Window Management: The presentation window minimized/maximized by gestures.
- Media Control: Switch on/off media playback with a gesture.

## Troubleshooting

- Slide Window Not Found: Be sure that the presentation window is correctly named in the script (`"Slides"`).
- Hand Tracking Issues: Be in a good lighting environment and your hand visible to the camera for tracking.
- Libraries Not Found: Be sure all the needed libraries are installed, and your Python environment is properly configured.

## License

This project uses the MIT License - see the [LICENSE](LICENSE) file for more information.
