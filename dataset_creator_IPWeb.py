
import urllib
import cv2
import numpy as np
import sqlite3

url="http://192.168.43.1:8080/shot.jpg"




face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def insertOrUpdate(Id,name,age,gender):
    conn = sqlite3.connect("FaceBase.db")
    
    
    cmd = "SELECT * FROM People WHERE ID="+str(Id)
    cmd1 = "SELECT * FROM Attendence WHERE ID="+str(Id)
    
    cursor=conn.execute(cmd)
    cursor1=conn.execute(cmd1)
    
    isRecordExist=0
    isRecordExist1=0
    
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(name)+",Age="+str(age)+",Gender="+str(gender)+" Where ID="+str(Id)
    else:
        cmd="INSERT INTO People(ID,Name,Age,Gender) Values("+str(Id)+","+str(name)+","+str(age)+","+str(gender)+")"
        
    conn.execute(cmd)
    for row in cursor1:
        isRecordExist1=1
    if(isRecordExist1==1):
        cmd1="UPDATE Attendence SET Name="+str(name)+" Where ID="+str(Id)
    else:
        cmd1="INSERT INTO Attendence(ID,Name) Values("+str(Id)+","+str(name)+")"
        
    conn.execute(cmd1)
    
    conn.commit()
    conn.close()
        
        
    

Id = input('Enter ID: ')
name = input('Enter Name: ')
age = input('Enter Age: ')
gender = input('Enter Gender: ')


insertOrUpdate(Id,name,age,gender)
sampleNum = 0
while True:
    imgResp=urllib.request.urlopen(url)
    
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    
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

cv2.destroyAllWindows()


    

    
        
