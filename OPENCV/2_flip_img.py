import cv2
import numpy as np

#reading an img 
img=cv2.imread('th.jpg')

#fliping an img in x-axsis by taking the flipy
flipx=cv2.flip(img,-1)

#fliping an img in x-axsis by taking the original img
flipxx=cv2.flip(img,0)

#fliping an img in y-axsis
flipy=cv2.flip(img,1)

#displaying windows
cv2.imshow('xx',flipxx)
cv2.imshow('img',img)
cv2.imshow('x',flipx)
cv2.imshow('y',flipy)
cv2.waitKey(0)
destroyAllWindows
