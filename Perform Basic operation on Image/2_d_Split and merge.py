# 2. c.
# Setting Region of Image (ROI)

import numpy as np
import cv2

img = cv2.imread('D:/DIP/images/messi5.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

b = img[:, :, 0]
img[:, :, 2] = 0

cv2.imshow('imagewindow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
