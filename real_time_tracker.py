import cv2
import mediapipe as mp

def human_tracker():
    # Initialize MediaPipe Holistic Detection (for body, face, and hands)
    mp_holistic = mp.solutions.holistic
    holistic = mp_holistic.Holistic(
        static_image_mode=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    # Initialize drawing utility
    mp_drawing = mp.solutions.drawing_utils

    # Start capturing webcam feed
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access the webcam.")
        return

    print("Press 'q' to exit.")

    while True:
        # Read a frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Cannot read the frame.")
            break

        # Convert BGR frame to RGB (MediaPipe works with RGB images)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with Holistic Detection
        results = holistic.process(rgb_frame)

        # Check if any landmarks are detected
        if results.pose_landmarks:
            # Draw body landmarks
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
            )

            # Draw face landmarks if detected
            if results.face_landmarks:
                mp_drawing.draw_landmarks(
                    frame, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
                    mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1),
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=1)
                )

            # Convert landmarks to lists
            pose_landmarks = list(results.pose_landmarks.landmark)
            face_landmarks = list(results.face_landmarks.landmark) if results.face_landmarks else []

            # Calculate bounding box including the head, body, and face
            landmarks = pose_landmarks + face_landmarks
            h, w, _ = frame.shape

            x_min = int(min([lm.x for lm in landmarks]) * w)
            y_min = int(min([lm.y for lm in landmarks]) * h)
            x_max = int(max([lm.x for lm in landmarks]) * w)
            y_max = int(max([lm.y for lm in landmarks]) * h)

            # Draw the bounding box
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)

        # Display the frame
        cv2.imshow('Human Movement Tracker', frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    human_tracker()
