# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:04:20 2018

@author: Ayushi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:57:06 2018

@author: Ayushi
"""

import cv2
import numpy as np
import sqlite3

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def insertOrUpdate(Id,name,age,gender):
    conn = sqlite3.connect("FaceBase.db")
    
    
    cmd = "SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(name)+",Age="+str(age)+",Gender="+str(gender)+" Where ID="+str(Id)
    else:
        cmd="INSERT INTO People(ID,Name,Age,Gender) Values("+str(Id)+","+str(name)+","+str(age)+","+str(gender)+")"
        
    conn.execute(cmd)
    conn.commit()
    conn.close()
        
        
    

Id = input('Enter ID: ')
name = input('Enter Name: ')
age = input('Enter Age: ')
gender = input('Enter Gender: ')


insertOrUpdate(Id,name,age,gender)
sampleNum = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        sampleNum += 1
        cv2.imwrite('E:/Forsk/MyProjects/projects/Face_Detection sqlite/dataSet/User.'+str(Id)+"."+str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        
        cv2.rectangle(img, (x,y), (x+w, y+h), (0 ,0,255), 2)
        
        cv2.waitKey(100)
        
    cv2.imshow('Face', img)
    cv2.waitKey(1)
    if sampleNum>100:
        break;
cap.release()
cv2.destroyAllWindows()

    
        
