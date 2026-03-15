import cv2
import numpy as np
import os
import pickle
from sklearn.ensemble import RandomForestClassifier

DATASET_PATH = "dataset"

# store features
X = []
y = []

def extract_features(image):

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mean_brightness = np.mean(gray)
    texture = np.std(gray)
    oil_reflection = np.mean(hsv[:,:,2])

    return [mean_brightness, texture, oil_reflection]


for skin_type in os.listdir(DATASET_PATH):

    folder = os.path.join(DATASET_PATH, skin_type)

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        img = cv2.imread(path)

        if img is None:
            continue

        img = cv2.resize(img,(200,200))

        features = extract_features(img)

        X.append(features)
        y.append(skin_type)


print("Training samples:",len(X))

model = RandomForestClassifier(n_estimators=100)

model.fit(X,y)

os.makedirs("model",exist_ok=True)

pickle.dump(model, open("model/skin_model.pkl","wb"))

print("Model trained successfully")