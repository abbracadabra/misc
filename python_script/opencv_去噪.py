import cv2
import numpy as np

im = cv2.imread(r'D:\Users\yl_gong\Desktop\abc.jpg')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

thresh,im = cv2.threshold(im, 100, 255, cv2.THRESH_BINARY)

im2, contours, hierarchy = cv2.findContours(im, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    if cv2.contourArea(contour) < 40:
        cv2.fillPoly(im,[contour],(255, 255, 255))

# cv2.imshow('image',im)
# cv2.waitKey()
cv2.imwrite('01.jpg',im)