import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
#img[200:300,100:300] = 255,0,0

cv2.line(img, (0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(100,300),(250,500),(0,0,255),2) #filled --> cv2.FILLED or -1
cv2.circle(img,(200,300),150,(255,255,0),3)
cv2.putText(img,'OPENCV',(200,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,200,0),3)

cv2.imshow('output',img)
cv2.waitKey(0)