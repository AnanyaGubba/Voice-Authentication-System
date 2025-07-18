# -*- coding: utf-8 -*-
"""vas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17Ptw91_e-SWJLVZFSWbP0ykzO_IPbNc0
"""

import os
import numpy as np
import joblib
import librosa
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from google.colab import files

# Define model file paths
MODEL_FILE = "voice_auth_model.pkl"
SCALER_FILE = "scaler.pkl"

def load_audio(file_path, sr=22050):
    """Loads an audio file and returns the waveform with a fixed sample rate."""
    audio, _ = librosa.load(file_path, sr=sr, mono=True)
    return audio

def extract_features(audio, sr=22050, n_mfcc=13):
    """Extracts MFCC features + delta features for better speaker recognition."""
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    delta_mfcc = librosa.feature.delta(mfcc)
    delta2_mfcc = librosa.feature.delta(mfcc, order=2)

    # Flatten and concatenate all features
    features = np.hstack((np.mean(mfcc, axis=1), np.mean(delta_mfcc, axis=1), np.mean(delta2_mfcc, axis=1)))
    return features

def enroll_user():
    """Uploads a single WAV file for user and a single WAV file for non-user, extracts features, and trains a model."""
    if os.path.exists(MODEL_FILE):
        print("User already enrolled. Delete the model file to re-enroll.")
        return

    print("Upload a user voice sample:")
    uploaded_user = files.upload()
    user_file = list(uploaded_user.keys())[0]

    print("Upload a non-user voice sample:")
    uploaded_nonuser = files.upload()
    nonuser_file = list(uploaded_nonuser.keys())[0]

    user_features = extract_features(load_audio(user_file))
    nonuser_features = extract_features(load_audio(nonuser_file))

    X = np.array([user_features, nonuser_features])
    y = np.array([1, 0])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = SVC(kernel='rbf', probability=True, C=10, gamma='scale')
    model.fit(X_scaled, y)

    joblib.dump(model, MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)
    print("✅ User enrollment complete. Voice model trained.")

def authenticate_user():
    """Authenticates a user using a single audio sample."""
    if not os.path.exists(MODEL_FILE) or not os.path.exists(SCALER_FILE):
        print("❌ No enrolled user found. Please enroll first.")
        return

    print("Upload a voice sample for authentication:")
    uploaded_file = files.upload()
    test_file = list(uploaded_file.keys())[0]

    audio = load_audio(test_file)
    features = extract_features(audio)

    scaler = joblib.load(SCALER_FILE)
    model = joblib.load(MODEL_FILE)

    features_scaled = scaler.transform([features])
    prob = model.predict_proba(features_scaled)[0][1]

    if prob > 0.5:
        print(f"✅ Authentication successful! (Confidence: {prob:.2f})")
    else:
        print(f"❌ Authentication failed. (Confidence: {prob:.2f})")

def authenticate_user():
    """Uploads a test audio file and verifies the voice."""
    if not os.path.exists(MODEL_FILE):
        print("No user enrolled. Please enroll first.")
        return

    print("Upload a test voice sample (.wav)")
    uploaded = files.upload()

    file_path = next(iter(uploaded))  # Get uploaded filename
    audio = load_audio(file_path)
    features = extract_features(audio)

    # Load model and scaler
    model = joblib.load(MODEL_FILE)
    scaler = joblib.load(SCALER_FILE)

    # Scale the input
    features_scaled = scaler.transform([features])

    # Predict
    probability = model.predict_proba(features_scaled)[0, 1]
    if probability > 0.6:  # Threshold for authentication
        print("✅ Authentication Successful!")
    else:
        print("❌ Authentication Failed!")

while True:
    print("\n1. Enroll User\n2. Authenticate User\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        enroll_user()
    elif choice == '2':
        authenticate_user()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")

