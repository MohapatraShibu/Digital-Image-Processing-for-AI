# 2. f.
# arithmetic operation of
# bitwise NOT of two images

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

# cv2.bitwise_not is applied over the
# image input with applied parameters
dest_not1 = cv2.bitwise_not(img1, mask=None)
dest_not2 = cv2.bitwise_not(img2, mask=None)

# the windows showing output image
# with the Bitwise NOT operation
# on the 1st and 2nd input image
cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
