import cv2
import numpy as np

#reading the img
img=cv2.imread('tth.jpg',0)
kernel=np.ones((5,5),np.uint8)
#erosion
erosion=cv2.erode(img,kernel,iterations=1)
#dilation
dilation=cv2.dilate(img,kernel,iterations=1)
#displaying the windows
cv2.imshow('img',img)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)
destroyAllWindows()
