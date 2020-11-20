# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 02:41:28 2019

@author: ARPIT DHAMIJA
"""
import cv2
import numpy as np 

# initialise camera
cap = cv2.VideoCapture(0)

# face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

#skip=0

while True:
	ret,frame = cap.read()

	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    print(faces)  
#	if len(faces) == 0:
#		continue
    
    
    # store every 10th face

   # if(skip%10==0):
    #    pass



	for(x,y,w,h) in faces:
    
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)

	cv2.imshow("faces",frame)

	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()