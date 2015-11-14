import cv2

video = cv2.VideoCapture("test.mp4")

if not video.isOpened():
    print("The video couldn't be opened")
    exit(1)

frame_number = 0

while video.isOpened():
    rval, frame = video.read()

    cv2.imwrite('frames/frame_%d.jpg' % frame_number, frame)

    frame_number += 1

video.release()