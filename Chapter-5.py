import cv2
import numpy as np

img = cv2.imread('Resources/cards.png')

width,height = 250,350  #size of the output img
pts1 = np.float32([[113,226],[302,192],[159,508],[374,462]])  # 4 vertices of the card
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])  # 4 vertices of the img for the card extracted
matrix = cv2.getPerspectiveTransform(pts1,pts2) # get the matrix transform for pts1 into pts 2
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) # get the img transformed


cv2.imshow('image',img)
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)