# 4. b.
# Shi-Tomasi Corner Detector

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:/DIP/images/taj.jpg')
ori = cv2.imread('D:/DIP/images/taj.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 10)
corners = np.int0(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)
cv2.imshow('Original', ori)
cv2.imshow('Shi-Tomasi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
