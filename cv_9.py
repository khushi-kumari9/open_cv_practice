import cv2

img = cv2.imread("D:\cv_practice.jpg")
blurred = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("original",img)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
