import cv2 as cv

# img = cv.imread('Resources/Photos/cat.jpg')

def rescaleFrame(frame, scale=0.75):
    # For images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimenstions = (width, height)

    return cv.resize(frame, dimenstions, interpolation=cv.INTER_AREA)


# def changeRes(width, height) :
#     # Only for live videos
#     capture.set(3, width)
#     capture.set(4, height)

# reading images
# resized_img = rescaleFrame(img)
# cv.imshow('Cat', resized_img)

# reading videos
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     # cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)