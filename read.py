import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg') # read image
cv.imshow('Cat', img) # display the image

cv.waitKey(0) # Open up the window for infinite time