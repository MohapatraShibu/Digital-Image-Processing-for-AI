# 3. j.
# Histograms (2D Histogram, Find, Plot, analyze, Histogram Equalization)

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:/DIP/images/messi5.jpg', 0)

equ = cv2.equalizeHist(img)

# stacking images side-by-side
res = np.hstack((img, equ))
cv2.imwrite('res.png', res)

# Plot
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
