import cv2

video_capture = cv2.VideoCapture("D:/nature_cv_practice.mp4")

while video_capture.isOpened():
    _, frame = video_capture.read()
    frame=cv2.resize(frame,(540,480))
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()