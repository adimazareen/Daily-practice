import cv2
import numpy as np
import mediapipe as mp

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Colors and Labels
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]  # Blue, Green, Red, Eraser (Black)
color_names = ['Blue', 'Green', 'Red', 'Eraser']
color_index = 0  # Start with Blue
draw_color = colors[color_index]

# Drawing thickness
draw_thickness = 7
eraser_thickness = 40

# Canvas
cap = cv2.VideoCapture(0)
canvas = None
prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # Draw color selection bar
    for i, name in enumerate(color_names):
        x1, x2 = i * 100, (i + 1) * 100
        cv2.rectangle(frame, (x1, 0), (x2, 50), colors[i], -1)
        cv2.putText(frame, name, (x1 + 5, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (255, 255, 255) if i != 3 else (0, 0, 0), 2)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            index_tip = handLms.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_tip.x * w), int(index_tip.y * h)

            # Selection mode (if finger is on top bar)
            if y < 50:
                color_index = x // 100
                draw_color = colors[color_index]
                prev_x, prev_y = 0, 0  # Reset drawing
            else:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y

                if draw_color == (0, 0, 0):  # Eraser
                    cv2.line(canvas, (prev_x, prev_y), (x, y), draw_color, eraser_thickness)
                else:
                    cv2.line(canvas, (prev_x, prev_y), (x, y), draw_color, draw_thickness)

                prev_x, prev_y = x, y
    else:
        prev_x, prev_y = 0, 0

    # Combine frame and canvas
    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    cv2.imshow("Air Drawing with Color & Eraser", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
