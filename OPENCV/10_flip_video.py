
import numpy as np
import cv2

# capture video
cap = cv2.VideoCapture(0)

#descripe a loop
#read video frame by frame
while True:
    ret,frame=cap.read()
    ret,img = cap.read()
    cv2.imshow('Original Video',img)
    #flip for truning(fliping) frames of video
    img2=cv2.flip(img,-1)#x axsis
    frame=cv2.flip(frame,1)#y axsis
    cv2.imshow('x_flipped_video',img2)
    cv2.imshow('y_flipped_video',frame)

    k=cv2.waitKey(30) & 0xff
    #once you inter Esc capturing will stop
    if k==27:
        break
cap.release()
cv2.destroyAllWindows() 
