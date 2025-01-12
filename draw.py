import cv2 as cv
import numpy as np

# blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Pain the image in a certain colour
# blank[100:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)