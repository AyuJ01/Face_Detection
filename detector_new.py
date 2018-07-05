# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:40:01 2018

@author: Ayushi
"""

import cv2
import os
import PIL
from PIL import Image
import numpy as np


faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer.load("recognizer\\trainingData.yml")
#path = 'E:/Forsk/MyProjects/Face_Detection'
recognizer.read('recognizer\\trainingData.yml')
id=0
#font=cv2.FONT_HERSHEY_COMPLEX_SMALL,5,1,0,1

while True:
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        #cv2.putText(img,str(id),(x,y+h),font,255)
        if(Id==1):    
                cv2.putText(img, "Ayushi",(x, y+h),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
        elif (Id == 2):
                cv2.putText(img, "Prashita",(x, y+h),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
        elif (Id == 3):
                cv2.putText(img, "Priyam",(x, y+h),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))    
                
        """     
        if(conf<50):
            if(Id==0):    
                cv2.putText(im, "Aman",(100, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 1):
                cv2.putText(im, "Rahul",(125, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 2):
                cv2.putText(im, "Ayushi",(150, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 3):
                cv2.putText(im, "Jagrati",(200, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 4):
                cv2.putText(im, "Prashita",(220, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 5):
                cv2.putText(im, "Ayu",(250, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            elif (Id == 6):
                cv2.putText(im, "Priyam",(300, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))    
            else:
                cv2.putText(im, "unknown",(350, 100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))    
    """
    cv2.imshow('Face',img) 
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
