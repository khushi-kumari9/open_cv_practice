import cv2
img= cv2.imread("D:/images.jpeg")

print("dimensions of image" , img.shape)


cv2.imshow("window", img)

cv2.waitKey(0)
cv2.destroyAllWindows()