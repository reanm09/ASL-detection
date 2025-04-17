import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

dataset_path = r"E:\Arduino\dataset\processed_combine_asl_dataset"

IMG_SIZE = 64 

images = []
labels = []

classes = sorted([f for f in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, f))])
class_to_index = {cls: i for i, cls in enumerate(classes)}  
print("Classes found:", classes)

for label in classes:
    folder_path = os.path.join(dataset_path, label)

    if not os.path.exists(folder_path):  
        print(f"Skipping missing directory: {folder_path}")
        continue

    print(f"Loading images from: {folder_path}")

    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)

        if not image_name.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        if not os.path.exists(image_path): 
            print(f"Skipping missing file: {image_path}")
            continue

        image = cv2.imread(image_path)

        if image is None:
            print(f"Warning: Unable to load {image_path}")
            continue  

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

        images.append(image / 255.0)
        labels.append(class_to_index[label])

if not images:
    print("Error: No images loaded. Check dataset path and file structure.")
    exit()

images = np.array(images).reshape(-1, IMG_SIZE, IMG_SIZE, 1)  
labels = np.array(labels)

labels = to_categorical(labels, num_classes=len(classes))

X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

np.savez("processed_data.npz", X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

print("✅ Data saved as 'processed_data.npz'. Ready for training!")
print(f"Training samples: {X_train.shape}, Testing samples: {X_test.shape}")
