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

Dataset contains labeled grayscale images of ASL hand signs processed using MediaPipe, organized by class folders.

Example structure:
dataset/ ├── A/ │ ├── img1.jpg │ └── ... ├── B/ │ └── ... ...

yaml
Copy
Edit

---

## 📂 Project Structure

. ├── main.py # Preprocesses dataset and saves it as .npz ├── test.py # Trains CNN and saves model as .h5 ├── detect_asl.py # Real-time detection with optional Arduino support ├── requirements.txt # Project dependencies ├── .gitignore # Ignore files for version control └── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
2. Preprocess Dataset
Ensure your dataset is structured as shown above, then run:

bash
Copy
Edit
python main.py
3. Train the Model
bash
Copy
Edit
python test.py
This will generate asl_sign_model.h5.

4. Start Real-Time Detection
bash
Copy
Edit
python detect_asl.py
Arduino is optional and used for physical feedback. Detection works with or without it.

🛠 Arduino Integration (Optional)
If an Arduino is connected (default port: COM4):

b'1' is sent when a sign is confidently detected.

b'0' is sent when the prediction is uncertain.

🧾 License
For academic and personal research use.
