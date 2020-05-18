from pyimagesearch.centroidtracker import CentroidTracker
from imutils.video import VideoStream
from collections import Counter
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean 
from insightface.embedder import InsightfaceEmbedder
import imutils
import time
import datetime
import cs2
from keras import backend as K
import sys,getopt
import pickle
import uuid
import os
import numpy as np
import argparse

os.environ['KERAS_BACKEND'] = 'tensorflow'
from keras.models import load_model
from keras.preprocessing import image

ct = CentroidTracker()
(H,W)= (None,None)
model_path = "models/model-r100-ii/model"
embedder = InsightfaceEmbedder(model_path=model_path, epoch_num='0000', image_size=(112, 112))


cascPatch= "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
threshold = 1.0
embeb = 'vmodev.pickle'

with open (embeb,'rb') as f :
	data =pickle.load(f)
print ("Starting recong")

# ret,frame = cap.read()
time.sleep(0.5)
font =cv2.FONT_HERSHEY_SIMPLEX
img= frame
img = img[...,::-1]#BGR 2 RGB
inputs = img.copy() / 255.0
timer = time.strftime("%c")
person = 0
frameNum =1
cap = cv2.VideoCapture(0)

def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()

while (True):
	ret,frame= cap.read()

	# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# fm2= variance_of_laplacian(gray)
	frame = imutils.resize(frame, width=400)
	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

	for (x, y, w, h) in faces:
		
		face_img = frame[y:y+h, x:x+w]
		# get blur:
		grayf = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
		fm = variance_of_laplacian(grayf)
		# get face size
		fh = (grayf.shape)[0]
		# embedding
		emb_me1 = embedder.embed_image(faceImg)

		if (len(emb_me1) == 0):
			continue
		# recognize
		bestTH = threshold + 0.1
		bestName = "Unknown"
		for key,emb_me2 in data.items():
			result = euclidean(emb_me1,emb_me2)
			if result < bestTH:
				bestTH = result
				bestName = key[:-5]
		# Name,Rect, Blur, Size
		cv2.putText(image, bestName, (x-10, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,250))		
		# cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)
		# cv2.putText(image,'Face:'+ str(int(fm))+'- Frame:'+str(int(fm2)), (x-10, y-15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,250))
		# cv2.putText(image, str(grayf.shape), (x-10, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,250))
		cv2.imshow("Checking", image)
		
		# name = 'outp_img/'+'Unknown:'+str(uuid.uuid4())+".jpg"
		# name = 'Unknown:'+str(uuid.uuid4())+".jpg"
		# # Saving and embding Img
		# if fm>200 and fm2>1000 and fh >120 and bestName =='Unknown' :
		# 	# cv2.imwrite(name,faceImg)
		# 	# print('Creating...',name)  
		# 	data[name]=emb_me1

		# 	with open(embed,'wb') as f:
		# 	    pickle.dump(data,f)



		# row = [Id_result,age_result,gender_result,emotion_result,str(timer)]

		# with open('result4.csv', 'a') as csvFile:
		# 	writer = csv.writer(csvFile)
		# 	print(row)
		# 	writer.writerow(row)
		# csvFile.close()


	cv2.imshow('Frame',frame)
# 		out.write(image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
out.release()
cap.release()