# 2. b.
# Access image properties i.e., Shape

import numpy as np
import cv2 as cv

img = cv.imread('D:/DIP/images/messi5.jpg')

px = img[100, 100]
print(px)

# accessing only blue pixel
blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])

print(img.shape)
print(img.size)
print(img.dtype)