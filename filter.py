import cv2 as cv
import numpy as np

img = cv.imread("assets/forest.jpg", -1)
img = cv.resize(img, (0, 0), fx=2, fy=2)

# RGB filters
# shape = img.shape
# for y in range(shape[0]):
#     for x in range(shape[1]):
#         # img[y][x][0] = 255 # blue filter
#         img[y][x][1] = 255 # green filter
#         # img[y][x][2] = 255 # red filter

# Blur
# average = cv.blur(img, (7, 7))
# cv.imshow("Blur", average)

cv.imshow("Result", img)
cv.waitKey(0)
cv.destroyAllWindows()