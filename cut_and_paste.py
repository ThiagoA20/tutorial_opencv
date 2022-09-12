import cv2 as cv
import numpy as np

img1 = cv.imread("assets/cards.jpg", -1)
img2 = cv.imread("assets/forest.jpg", -1)
img2 = cv.resize(img2, (0, 0), fx=2, fy=2)

print(img1.shape)
print(img2.shape)

cards_cut = img1[250:400, 50:300]
img2[350:500, 500:750] = cards_cut

cv.imshow("img2", img2)
cv.waitKey(0)
cv.destroyAllWindows()