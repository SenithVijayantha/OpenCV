import cv2 as cv
from rescale import rescaleFrame

img = cv.imread('Resources/Photos/IMG_0213.jpg')

resized_image = rescaleFrame(img, scale=0.3)
cv.imshow('Image', resized_image)


# Bilateral
bilateral = cv.bilateralFilter(resized_image, 5, 50, 50)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)