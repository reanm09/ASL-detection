# 🤟 ASL Sign Language Recognition with Real-Time Inference

This project implements an American Sign Language (ASL) recognition system using a custom-trained Convolutional Neural Network (CNN) and live webcam input. The system optionally supports Arduino integration for external feedback based on the detected sign.

---

## 📌 Overview

- Trains a CNN model on a processed ASL dataset for static gesture classification.
- Performs real-time sign detection using OpenCV and TensorFlow.
- Arduino integration (optional) enables signal transmission via serial port.

---

## 🧠 Dataset

The model is trained using the **MediaPipe Processed ASL Dataset**, available here:  
🔗 [Kaggle Dataset Link](https://www.kaggle.com/datasets/vignonantoine/mediapipe-processed-asl-dataset/discussion/367326)

---

## ⚙️ How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```
2. Preprocess Dataset
run:
```
python main.py
```
3. Train the Model
```
python test.py
```
This will generate asl_sign_model.h5.

4. Start Real-Time Detection
```
python detect_asl.py
```
Arduino is optional and used for physical feedback. Detection works with or without it.

🛠 Arduino Integration (Optional)
If an Arduino is connected (default port: COM4):

b'1' is sent when a sign is confidently detected.

b'0' is sent when the prediction is uncertain.
