import numpy                     #library for high level mathematical function
import cv2                       #open cv
img=cv2.imread('a.png')          #reading a image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      #gray scale convertion
retval2,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  #binary convertion
retval2,thresh2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV)
cv2.imshow('col',img)  #display image
cv2.imshow('gray',gray)
#cv2.imshow('1',thresh2)
cv2.imshow('bin',thresh1)
cv2.waitKey(0)  #keyboad input from user
cv2.destroyAllWindows()  # destroys all windows created
