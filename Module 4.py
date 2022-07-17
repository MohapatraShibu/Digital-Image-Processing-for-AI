# Module – 4:
# Object Detection in OpenCV
# Finding corners

import numpy as np
import cv2
from matplotlib import pyplot as plt

# read the image
img = cv2.imread('images/bunchofshapes.jpg')
cv2.imshow('Original Image', img)

# convert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect corners with the goodFeaturesToTrack function.
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
corners = np.int0(corners)

# we iterate through each corner,
# making a circle at each point that we think is a corner.
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 9, 255, -1)

plt.imshow(img)
plt.show()