import cv2

img = cv2.imread("mandrill.jpg")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyWindow("image")
