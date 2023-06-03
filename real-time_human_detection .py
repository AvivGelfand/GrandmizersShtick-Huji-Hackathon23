import cv2
import mediapipe as mp

# Build Keypoints using MP Holistic
mp_holistic = mp.solutions.holistic  # Holistic model
mp_drawing = mp.solutions.drawing_utils  # Drawing utilities


def mediapipe_detection(image, model):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = model.process(image_rgb)
    return results


def draw_styled_landmarks(image, results):
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_holistic.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing.DrawingSpec(
            color=(80, 22, 10), thickness=2, circle_radius=4
        ),
        connection_drawing_spec=mp_drawing.DrawingSpec(
            color=(80, 44, 121), thickness=2, circle_radius=2
        ),
    )
    mp_drawing.draw_landmarks(
        image,
        results.left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS,
        landmark_drawing_spec=mp_drawing.DrawingSpec(
            color=(121, 22, 76), thickness=2, circle_radius=4
        ),
        connection_drawing_spec=mp_drawing.DrawingSpec(
            color=(121, 44, 250), thickness=2, circle_radius=2
        ),
    )
    mp_drawing.draw_landmarks(
        image,
        results.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS,
        landmark_drawing_spec=mp_drawing.DrawingSpec(
            color=(245, 117, 66), thickness=2, circle_radius=4
        ),
        connection_drawing_spec=mp_drawing.DrawingSpec(
            color=(245, 66, 230), thickness=2, circle_radius=2
        ),
    )

    # Draw face landmarks if available
    if results.face_landmarks is not None:
        for landmark in results.face_landmarks.landmark:
            x = int(landmark.x * image.shape[1])
            y = int(landmark.y * image.shape[0])
            cv2.circle(image, (x, y), 2, (80, 110, 10), -1)


# Rest of the code...


cap = cv2.VideoCapture(0)

with mp.solutions.holistic.Holistic(
    min_detection_confidence=0.5, min_tracking_confidence=0.5
) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        results = mediapipe_detection(frame, holistic)
        draw_styled_landmarks(frame, results)

        cv2.imshow("OpenCV Feed", frame)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
