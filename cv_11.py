import cv2

img = cv2.imread("D:\cv_practice.jpg")
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("original", img)
cv2.imshow("Bilateral", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()