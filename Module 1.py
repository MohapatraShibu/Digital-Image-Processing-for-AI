# Module – 1:
# Basics of Computer Vision and OpenCV
# Histogram representation on images

import cv2
import matplotlib.pyplot as plt

# reads an input image
img = cv2.imread('images/1.jpg', 0)
cv2.imshow('Shibu', img)

# find frequency of pixels in range 0-255
hist = cv2.calcHist([img], [0], None, [256], [10, 256])

# plotting graph of an image
plt.plot(hist)
plt.show()