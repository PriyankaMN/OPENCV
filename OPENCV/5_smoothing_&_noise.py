import cv2
import numpy as np

#read an image
img=cv2.imread('S.jpg',1)

#mark the edges
edges=cv2.Canny(img,100,200)

# conversion of rgb2bgr and bgr2hsv
bgr=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#lower and upper range of red
lower_red=np.array([150,80,0])
upper_red=np.array([180,255,255])

#lower and upper range of blue
#lower_range=np.array([110,50,50])
#upper_range=np.array([130,255,255])

#masking 
mask=cv2.inRange(hsv,lower_red,upper_red)

#res from img and masking
res=cv2.bitwise_and(img,img,mask=mask)

kernel=np.ones((15,15),np.uint8)

# gaussian blur 
blur=cv2.GaussianBlur(res,(15,15),1)
#smoothing
smoothed=cv2.filter2D(res,-1,kernel)
#noise removal using median
median=cv2.bilateralFilter(res,15,75,75)
#??
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
#displaying windows
cv2.imshow('open',opening)
cv2.imshow('close',closing)
cv2.imshow('bgr',bgr)
cv2.imshow('median',median)
cv2.imshow('smoothed',smoothed)
cv2.imshow('blur',blur)
cv2.imshow('res',res)
cv2.imshow('mask',mask)
cv2.imshow('hsv',hsv)
cv2.imshow('edges',edges)
cv2.imshow('img',img)
cv2.waitKey(0)
destroyAllWindows()
