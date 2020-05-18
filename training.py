import os
import cv2
import pickle
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean 
from insightface.embedder import InsightfaceEmbedder
import pickle

model_path = "models/model-r100-ii/model"
embedder = InsightfaceEmbedder(model_path=model_path, epoch_num='0000', image_size=(112, 112))

e_dict = {}

data_path = 'new/'

for filename in os.listdir(data_path):
    print(data_path+filename)
    img = cv2.imread(data_path+filename, 1)
    vector = embedder.embed_image(img)                    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    e_dict[filename]=vector
    print(vector)

with open('vmodev.pickle','wb') as f:
    data=pickle.dump(e_dict,f)
# with open('extracted_embeddings.pickle', 'rb') as f:
#     data = pickle.load(f)
# print(data)
# In[18]

