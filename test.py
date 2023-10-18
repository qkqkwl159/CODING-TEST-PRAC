import cv2

imgs = cv2.imread("./222.png",0)


cv2.imshow("TEST",imgs)
cv2.waitKey()
cv2.destroyAllWindows()
