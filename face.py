# from pyimagesearch.centroidtracker import CentroidTracker
from imutils.video import VideoStream
from collections import Counter
from scipy.spatial.distance import euclidean
from insightface.embedder import InsightfaceEmbedder
import imutils
import datetime
import cv2
import sys
import pickle
import os
import numpy as np
# ct = CentroidTracker()    
(H, W) = (None, None)
model_path = "models/model-r100-ii/model"
embedder = InsightfaceEmbedder(
    model_path=model_path, epoch_num='0000', image_size=(112, 112))
cascPatch = r"haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPatch)
threshold = 1.0
embeb = 'vmodev.pickle'

with open(embeb, 'rb') as f:
    data = pickle.load(f)


cap = cv2.VideoCapture("/home/vuong/Downloads/Ring/video2.mp4")


def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

ret, frame = cap.read()
img = frame
img = img[..., ::-1]  # BGR 2 RGB
inputs = img.copy() / 255.0

while (True):
    ret, frame = cap.read()
    image = frame
    nameId = {}

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    print(gray)
    fm2 = variance_of_laplacian(gray)
    print ("oki")
    frame = imutils.resize(frame, width=400)
    faces = faceCascade.detectMultiScale(

        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    print ("oki")
    for (x, y, w, h) in faces:
        print ('oki')
        face_img = image[y:y+h, x:x+w]
        startX = x
        startY = y
        endX = x+w
        endY = y+h
        print ('oki')
        cX = int((startX + endX) / 2.0)
        cY = int((startY + endY) / 2.0)

    # get blur:
        print ("oki")
        grayf = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(grayf)  # face blur
        emb_me1 = embedder.embed_image(face_img)
        fh = (grayf.shape)[0]  # Size img
        print ("oki")
        if (len(emb_me1) == 0):
            continue
        # print ("oki")
    # recognize
        bestTH = threshold + 0.1
        bestName = "Unknown"
        for key, emb_me2 in data.items():
            result = euclidean(emb_me1, emb_me2)
            if result < bestTH:
                bestTH = result
                bestName = key[:-5]

    # save if name is not unknown
        if bestTH < threshold + 0.1:
            nameId[str(cX) + '-'+str(cY)] = bestName
            print("_____" + bestName)
    # Name, Blur, Size
        # cv2.putText(frame, bestName, (x-10, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,250))
        # # cv2.putText(frame,'Face:'+ str(int(fm))+'- Frame:'+str(int(fm2)), (x-10, y-15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,250))
  #       # cv2.putText(image, str(grayf.shape), (x-10, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,250))
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

    # cv2.imshow('Frame', frame)
# 		out.write(image)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
