# 2. f.
# arithmetic operation of
# bitwise OR of two images

import cv2
import numpy as np

path = r'D:/DIP/images/bit1.png'
img = cv2.imread(path)
print(img)

path2 = r'D:/DIP/images/bit2.png'
img4 = cv2.imread(path2)
print(img4)

cv2.imshow('window1', img)
cv2.waitKey(0)
#
# cv2.imshow('window2',img4)
# cv2.waitKey(0)
# path to input images are specified and
# images are loaded with imread command
img1 = cv2.imread('D:/DIP/images/bit1.png')
img2 = cv2.imread('D:/DIP/images/bit2.png')

# cv2.bitwise_or is applied over the
# image inputs with applied parameters

destor = cv2.bitwise_or(img2, img1, mask=None)

# the window showing output image
# with the Bitwise OR operation
# on the input images

cv2.imshow('BitwiseOR', destor)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
