import cv2

video_capture = cv2.VideoCapture("D:/nature_cv_practice.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output =cv2.VideoWriter('output.mp4',fourcc, 23.98, (854,480))

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if ret:
        output.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == ord('s'):
            break

    else:
        break

cv2.destroyAllWindows()
