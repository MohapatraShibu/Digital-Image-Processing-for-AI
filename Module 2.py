# Module – 2:
# Image Manipulation and processing
# Resizing of image along with interpolation methods

import cv2
import numpy as np

# Read the image using imread function
image = cv2.imread('images/1.jpg')
cv2.imshow('Original Image', image)
scale_down = 0.6

# Scaling Down the image 0.6 times using different Interpolation Method
res_inter_nearest = cv2.resize(image, None, fx = scale_down, fy= scale_down, interpolation= cv2.INTER_NEAREST)
res_inter_linear = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
res_inter_area = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_AREA)

# Concatenate images in horizontal axis for comparison
vertical= np.concatenate((res_inter_nearest, res_inter_linear, res_inter_area), axis = 0)
horizontal= np.concatenate((res_inter_nearest, res_inter_linear, res_inter_area), axis = 1)

# Display the image Press any key to continue
cv2.imshow('Inter Nearest :: Inter Linear :: Inter Area', vertical)
cv2.waitKey(0)

cv2.imshow('Inter Nearest :: Inter Linear :: Inter Area', horizontal)
cv2.waitKey(0)