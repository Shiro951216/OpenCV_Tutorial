import cv2
import numpy as np

img = cv2.imread('Resources/leadale.jpg')
kernel = np.ones((2,2),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(11,11),0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilate = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilate,kernel,iterations=1)

cv2.imshow('gray img', imgGray)
cv2.imshow('blur img', imgBlur)
cv2.imshow('canny img', imgCanny)
cv2.imshow('dilation img', imgDilate)
cv2.imshow('erosion img', imgEroded)

cv2.waitKey(0)