# 1. a.
# Load an image, display it and save it back

# import required packages
import cv2

# loading image
img = cv2.imread('D:/DIP/images/taj.jpg')

# converting to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# converting to HSV colorspace
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# displaying image
cv2.imshow('Image file', img)
cv2.waitKey(0)

# saving file back to disk
cv2.imwrite("D:/DIP/1. Perform GUI Features in OpenCV/newfile.jpg", img)

