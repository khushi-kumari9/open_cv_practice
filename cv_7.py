import cv2
img=cv2.imread("D:\cv_practice.jpg")
row=img.shape[0]
col=img.shape[1]
center=(col/2,row/2)
angle=90
r=cv2.getRotationMatrix2D(center,angle,1)
rotate=cv2.warpAffine(img,r,(col,row))
cv2.imshow("rotate",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()