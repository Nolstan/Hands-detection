import cv2
import mediapipe as mp  

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
video = cv2.VideoCapture(0)

#  reduce resolution for better speed
video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with mp_hands.Hands(max_num_hands=4, min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while True:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)  # Flip horizontally

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True

        # Draw landmarks directly on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hands", frame)

        if cv2.waitKey(1) == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
