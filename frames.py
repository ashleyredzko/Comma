import cv2
import numpy as np

video = cv2.VideoCapture("test.mp4")

if not video.isOpened():
    print("The video couldn't be opened")
    exit(1)

frame_number = 1

more_frames = True

framesx = None
framesy = None
y = 0

while video.isOpened() and more_frames:
    more_frames, frame = video.read()

    if frame_number % 2 == 0:
        if frame is None or not frame.any():
            more_frames = False
            continue

        if framesx is None:
            framesx = frame
        else:
            framesx = np.concatenate((framesx, frame), axis=0)

        if frame_number % 5 == 0:

            if framesy is None:
                framesy = framesx
            else:
                framesy = np.concatenate((framesy, framesx), axis=1)

            y += 1

            if y == 2:
                cv2.imwrite('frames/frames_%d.jpg' % frame_number, framesy)
                framesy = None
                y = 0

            framesx = None

    frame_number += 1

if framesy is not None:
    cv2.imwrite('frames/frames_%d.jpg' % frame_number, framesy)

video.release()