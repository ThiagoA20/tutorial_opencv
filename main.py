import cv2 as cv
import numpy as np
from random import randint

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
    return result


img = cv.imread('assets/forest.jpg', 1) # 0 is grayscale and -1 is without alpha channel.
# img = cv.resize(img, (500, 500))
img = cv.resize(img, (0, 0), fx=2, fy=2)
# img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE) # You can also use the function rotate_image in this code to rotate in any angle: img = rotate_image(img, -12)

# cv.imwrite("imagem_alterada.jpg", img) # save the image

# Set random colors for pixels
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [randint(0, 255), randint(0, 255), randint(0, 255)]



cv.imshow('Forest', img)
cv.waitKey(0) # wait until any key is pressed
cv.destroyAllWindows()