# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:18:02 2018

@author: Ayushi
"""

import os
import cv2
import numpy as np

import PIL
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()


path = 'E:\Forsk\MyProjects\Face_Detection\dataSet'

def getImagesWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    #print(imagePaths)
    
    

    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')

        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNp)
        IDs.append(Id)

        cv2.imshow('training',faceNp)

        cv2.waitKey(10)
    return faces, np.array(IDs)

faces, Ids = getImagesWithID(path)
recognizer.train(faces,np.array(Ids))

recognizer.save('recognizer/trainingData.yml')

print('done training')
cv2.destroyAllWindows()
