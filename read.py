import cv2 as cv

# read image
# img = cv.imread('Resources/Photos/cat_large.jpg')

# display the image
# cv.imshow('Cat', img) 

# reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()     

# Open up the window for infinite time
# cv.waitKey(0)

# Most of the time The error (-215:Assertion failed) happens when OpenCV can't find the specified file