# Hand Cricket App

This is a simple application that allows users to play hand cricket using hand gestures captured through the webcam. The game is played by making different hand gestures representing numbers from 1 to 10.

![Capture](https://github.com/venkatasai7/HandRecognition/assets/87575630/cc41ea6e-b80f-45f9-9885-62920c4ce830)

## Features

- Detects hand gestures using computer vision techniques.
- Allows users to play hand cricket by making gestures corresponding to numbers.
- Generates a random number to simulate the opponent's move.
- Tracks the score and determines if the player is out or not.
- Provides real-time feedback through the webcam feed.

## Installation

To run the application, ensure you have Python installed on your system. You can install Python from [python.org](https://www.python.org/downloads/).

1. Clone or download the repository to your local machine:

```bash
git clone https://github.com/venkatasai7/HandRecognition/tree/main
```

2. Navigate to the project directory
   
4. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Connect a webcam to your computer.
2. Run the `main.py` script:

```bash
python main.py
```

3. Make hand gestures corresponding to numbers from 1 to 10 as follows:
   - Index finger only: 1
   - Index and middle fingers: 2
   - Index, middle, and ring fingers: 3
   - All fingers except pinky: 4
   - All fingers : 5
   - only Thumb : 6
   - Thumb and index finger: 7
   - Thumb, middle and index finger: 8
   - All fingers except pinky : 9
   - Thumb and pinky: 10

4. The application will display the opponent's move and update the score accordingly.
5. Continue playing until you get out or exit the game.


![Capture2](https://github.com/venkatasai7/HandRecognition/assets/87575630/ea219100-f453-4156-b50b-7f600094f1b5)


## Dependencies

The application relies on the following Python packages:

- cv2 (OpenCV)
- cvzone
- numpy

Ensure you have these packages installed before running the application.







