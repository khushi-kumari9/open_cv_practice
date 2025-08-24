import cv2
import numpy as np

img=cv2.imread("D:\cv_practice.jpg")
threshold_value=200
_,binary_threshold=cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow("binary_threshold",binary_threshold)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()