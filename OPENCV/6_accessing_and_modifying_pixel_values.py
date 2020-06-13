import cv2
import numpy as np

img=cv2.imread('AA.jpg')

#pixel(bgr) value at 100*100
px = img[100,100]
print (px)


# accessing only blue pixel(0--for blue pixel)
blue = img[100,100,0]
print (blue)

#modify the pixcel values
img[100,100] = [255,255,255]
print (img[100,100])


# accessing RED value (assesing all bgr values in img.item())
img.item(10,10,2)


# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

#img shape
print (img.shape)

#img size
print (img.size)

#img datatype
print (img.dtype)

#print(img)
cv2.imshow('img',img)
cv2.waitKey(0)

