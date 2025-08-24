import cv2
import numpy as np

img = cv2.imread("D:/new.jpg")


kernel = np.ones((5, 5), np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# gradiant = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("original", img)
# cv2.imshow("opening", opening)
# cv2.imshow("closing", closing)
# cv2.imshow("gradiant", gradiant)
cv2.imshow("tophat", tophat)
cv2.imshow("blackhat", blackhat)


cv2.waitKey(0)
cv2.destroyAllWindows()

