import numpy
import cv2
hsv_min = numpy.array((0, 100, 20), numpy.uint8)
hsv_max = numpy.array((200, 250, 200), numpy.uint8)
img = cv2.imread('apple.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
th = cv2.inRange(hsv, hsv_min, hsv_max)
contours, hiarchy = cv2.findContours(th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255, 0, 0), 5, cv2.LINE_AA, hiarchy, 1)
cv2.imshow('th', th)
cv2.waitKey()
cv2.destroyWindow()
