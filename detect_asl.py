import cv2
import numpy as np
import tensorflow as tf
import serial
import time

model = tf.keras.models.load_model("asl_sign_model.h5")

try:
    arduino = serial.Serial(port="COM4", baudrate=9600, timeout=1)
    time.sleep(2)  
    print("✅ Connected to Arduino")
except Exception as e:
    arduino = None  

cap = cv2.VideoCapture(0)  

IMG_SIZE = 64  

def preprocess_frame(frame):
    """Convert frame to grayscale, resize, and normalize for the model."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (IMG_SIZE, IMG_SIZE))
    normalized = resized / 255.0
    return np.expand_dims(normalized, axis=(0, -1))  

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    processed_frame = preprocess_frame(frame)

    predictions = model.predict(processed_frame)
    confidence = np.max(predictions)
    predicted_label = np.argmax(predictions)
    
    print(f"Raw Predictions: {predictions}")
    print(f"Predicted Label: {predicted_label}, Confidence: {confidence:.2f}")

    if confidence > 0.5:
        print(f"✅ Detected sign: {predicted_label} (Confidence: {confidence:.2f})")
        if arduino:
            arduino.write(b'1')  
    else:
        print(f"❌ Uncertain prediction (Confidence: {confidence:.2f})")
        if arduino:
            arduino.write(b'0')  

    cv2.putText(frame, f"Sign: {predicted_label} ({confidence:.2f})", 
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("ASL Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
