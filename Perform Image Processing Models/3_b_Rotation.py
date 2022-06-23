# 3. b.
# Geometric Transformations of Images
# (Rotation, Affine Transformation, Perspective Transformation)

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('D:/DIP/images/messi5.jpg', 0)

# Rotation
rows, cols = img.shape

# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
