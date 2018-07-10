# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:05:21 2018

@author: Ayushi
"""

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
import sqlite3

faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer\\trainingData.yml')


#recognizer.load("recognizer\\trainingData.yml")
path = 'E:/Forsk/MyProjects/projects/Face_Detection sqlite/dataSet'

def getProfile(Id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile



def insertDetails(profile):
    conn = sqlite3.connect("FaceBase.db")
    
    
    cmd = "SELECT * FROM Info WHERE ID="+str(profile[0])
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE Info SET Name='"+str(profile[1])+"' Where ID="+str(profile[0])
    else:
        cmd="INSERT INTO Info(ID,Name) Values("+str(profile[0])+",'"+str(profile[1])+"')"        
    conn.execute(cmd)
    conn.commit()
    conn.close()

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
        profile = getProfile(Id)
        #insertDetails(profile) 
        if(profile!=None):
            #insertDetails(profile)
            insertDetails(profile)
            cv2.putText(img, "ID : "+str(profile[0]),(x, y+h+30),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            cv2.putText(img, "Name : "+str(profile[1]),(x, y+h+60),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            cv2.putText(img, "Age : "+str(profile[2]),(x, y+h+90),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
            cv2.putText(img, "Gender: "+str(profile[3]),(x, y+h+120),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
        
       
    
    cv2.imshow('Face',img) 
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
