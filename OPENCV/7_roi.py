import cv2
import numpy as np

img=cv2.imread('s.jpg')

roi=img[100:200, 100:200]
cv2.rectangle(img,(100,100),(200,200),(0,255,0),2)

cv2.imshow('roi',roi)
cv2.imshow('img',img)
cv2.waitKey(0)
