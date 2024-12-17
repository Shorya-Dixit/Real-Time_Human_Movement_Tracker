# Real-Time Human Movement Tracker

## Project Overview
This project implements a real-time human movement tracker using OpenCV and MediaPipe. The tracker captures a live webcam feed, detects human landmarks (including face, body, and hands), and draws bounding boxes around the human figure.

## Objectives

- Capture live webcam feed in real-time.
- Detect human landmarks, including body, face, and hands using the MediaPipe Holistic model.
- Draw bounding boxes around the detected human figure (body + head).
- Display the processed video feed with tracking overlays.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

## Setup Instructions

### 1. Create a Virtual Environment
It's recommended to use a virtual environment for managing project dependencies. To create one, follow these steps:

#### On Windows:
```python
python -m venv tracker_env
tracker_env\Scripts\activate
```
#### On macOS/Linux:
```python
python3 -m venv tracker_env
source tracker_env/bin/activate
```

### 2. Install Dependencies
Once the virtual environment is activated, install the required dependencies by running the following command:

```python
pip install -r requirements.txt
```
  **OR**
  
You can manually install the dependencies using:

```python
pip install opencv-python mediapipe
```

### 3. Clone or Download the Project
Clone or download the repository to your local machine.

```python
git clone https://github.com/Shorya-Dixit/Real-Time_Human_Movement_Tracker.git
```

### 4. Run the Project
To start the real-time human movement tracker, run the following command:

```python
python src/real_time_tracker.py
```
This will open a webcam feed and start tracking human movements. The bounding box will appear around the detected body and head. Press 'q' to exit the program.

### 5. Deactivate the Virtual Environment
Once you are done with the project, you can deactivate the virtual environment using:

```python
deactivate
```

## How It Works
The project uses the MediaPipe Holistic model, which provides human pose, face, and hand landmarks. The code captures frames from the webcam, processes them to detect these landmarks, and then draws a bounding box around the detected human figure.

- The Holistic model is used for detecting both the body and face landmarks.
- A bounding box is drawn based on the minimum and maximum x/y coordinates of the detected landmarks.

## Notes
- The code uses OpenCV for handling video capture and drawing bounding boxes on the frames.
- MediaPipe is used for detecting landmarks for pose, face, and hands.
- Ensure your webcam is properly connected and accessible for the application to function.
