
import urllib
import cv2
import numpy as np
url="http://192.168.43.1:8080/shot.jpg"




face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
Id = input('Enter ID: ')
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
cap.release()
cv2.destroyAllWindows()

    
        
