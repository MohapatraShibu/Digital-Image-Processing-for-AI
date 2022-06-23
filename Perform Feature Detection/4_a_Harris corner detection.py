# 4. a.
# Harris Corner detection

import cv2
import numpy as np

imput_img = 'D:/DIP/images/taj.jpg'
ori = cv2.imread(imput_img)
image = cv2.imread(imput_img)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
image[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('Original', ori)
cv2.imshow('Harris', image)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
