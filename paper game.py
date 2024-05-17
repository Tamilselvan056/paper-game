import mediapipe as mp
import numpy as np
import cv2
import random

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Images for the game
img1 = cv2.imread('FIVE.png')
img2 = cv2.imread('TWO.png')
img3 = cv2.imread('ZERO.png')
images = [img1, img2, img3]

# Initialize game score
score = 0

# Initialize game screen
screen = cv2.imread('screen.png')

# Main game loop
while True:
    # Randomly select an image to show
    img = random.choice(images)

    # Show the image for 5 seconds
    cv2.imshow('Finger Game', img)
    cv2.imshow('Screen', screen)
    cv2.waitKey(50)

    # Process the image with the hand tracking model
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img)
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        finger_count = 0
        for finger in [4, 8, 12, 16, 20]:
            if hand_landmarks.landmark[finger].y < hand_landmarks.landmark[finger-2].y:
                finger_count += 1
        if img is img1:
            if finger_count == 2:
                score += 1
        elif img is img2:
            if finger_count == 0:
                score += 1
        elif img is img3:
            if finger_count == 2:
                score += 1
            elif finger_count == 5:
                score += 1

    # Check if game is over
    if score >= 10:
        print('Player wins!')
        break

# Clean up
hands.close()
cv2.destroyAllWindows()
