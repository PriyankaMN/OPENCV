import cv2
import numpy as np

#creating a black_image of 512*512
img=np.zeros((512,512,3),np.uint8)

#creating a black image of 256*256
img2=np.zeros((256,256,3),np.uint8)

#coverting the black_image of 256*256 into  white_image
img2[:]=(255,255,255)

#drawing a line
img=cv2.line(img,(151,151),(208,208),(0,0,150),15)# diagonal
img2=cv2.line(img2,(50,30),(50,80),(155,0,0),15) # straight line y

#drawing a circle
img=cv2.circle(img,(250,250),40,(0,255,0),-1)#filled
img=cv2.circle(img,(50,50),40,(0,0,255),2)#outline

#drawing ellipse
img2=cv2.ellipse(img2,(150,100),(50,80),60,0,360,(255,0,0),-1)#filled
img2-cv2.ellipse(img2,(150,100),(50,80),60,0,360,(0,0,255),5)#outline

#drawing rectangle
img=cv2.rectangle(img,(400,200),(290,300),(255,0,0),0)#outline
img=cv2.rectangle(img,(40,50),(20,30),(255,0,0),-1)#filled

#drawing polygon
pts = np.array([[50,150],[120,130],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

#writing a text
img=cv2.putText(img,'PYTHON',(10,500),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,3,(255,255,255),2,cv2.LINE_AA)#aliasing_antialiasing
img=cv2.putText(img,'PYTHON',(10,400),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,3,(255,255,255),2)#plain text

#displaying the windows
cv2.imshow('512',img)
cv2.imshow('256',img2)
cv2.waitKey(0)
destroyAllWindows()
