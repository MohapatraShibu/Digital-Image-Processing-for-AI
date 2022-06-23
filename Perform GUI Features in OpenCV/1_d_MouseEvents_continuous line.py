# 1. d.
# Perform mouse Events
# Continuous line

import numpy as np
import cv2


# drawing=False # true if mouse is pressed
# mode=True

def event_handling_for(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 244), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)


img = np.zeros((512, 512, 3), np.uint8)
# img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', event_handling_for)

cv2.waitKey(0)
cv2.destroyAllWindows()