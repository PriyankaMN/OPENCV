import cv2
import numpy as np

cap=cv2.VideoCapture(0)
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret, frame=cap.read()
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret12,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  #binary convertion
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('threshold',thresh1)
    cv2.imshow('hsv',hsv)
    cv2.imshow('rgb',rgb)
   
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
