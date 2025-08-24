import cv2
import numpy as np

img = cv2.imread("D:\cv_practice.jpg")
min_thresh=100
max_thresh=200
edge_detection=cv2.Canny(img,min_thresh,max_thresh)
cv2.imshow("original",img)
cv2.imshow("edge_detection",edge_detection)
cv2.waitKey(0)
cv2.destroyAllWindows()