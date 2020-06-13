import cv2
import numpy as np
###############################################
#image addition

x = np.uint8([250])
y = np.uint8([10])

#opencv_operation
print (cv2.add(x,y)) # 250+10 = 260 => 255

#numpy operation
print (x+y)          # 250+10 = 260 % 256 = 4

##################################################
#image blending

img1 = cv2.imread('red.jpg')
img2 = cv2.imread('s.jpg')

dst = cv2.addWeighted(img1,0.3,img2,0.8,70)
dst1 = cv2.addWeighted(img1,0.3,img2,0.8,0)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)

################################################
#bitwise operation

b1 = cv2.imread('opencv_logo.jpg')
b2 = cv2.imread('tq.jpg')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = b2.shape
roi = b1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
b2gray = cv2.cvtColor(b2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(b2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
b1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
b2_fg = cv2.bitwise_and(b2,b2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(b1_bg,b2_fg)
b1[0:rows, 0:cols ] = dst

cv2.imshow('res',b1)


cv2.waitKey(0)
cv2.destroyAllWindows()
