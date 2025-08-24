import cv2

img = cv2.imread("D:/cv_practice.jpg")
print( "size in bytes" , img.size)

cv2.imshow("original", img)
# flip = cv2.flip(img, 1)
# cv2.imshow("horizontal", flip)
# flip = cv2.flip(img, 0)
# cv2.imshow("vertical", flip)

flip = cv2.flip(img, -1)
cv2.imshow("horizontal & vertical", flip)
cv2.waitKey(0)
cv2.destroyAllWindows()