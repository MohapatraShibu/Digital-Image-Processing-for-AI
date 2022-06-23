# 2. f
# arithmetic operation of
# subtraction of pixels of two images

# importing opencv
import cv2
import numpy as np

# reading the images
img = cv2.imread('D:/DIP/images/pic2.png')
img1 = cv2.imread('D:/DIP/images/pic3.png')

# subtract the images
subtracted = cv2.subtract(img, img1)

# TO show the output
cv2.imshow('image', subtracted)

# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
