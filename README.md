# Voice-Authentication-System
This project implements a simple voice authentication system which trains an SVM (Support Vector Machine) classifier to distinguish between a user's voice and others. The system supports user enrollment and voice-based authentication using .wav files.

# 🧑‍💻 Tech Stack Used
Programming Language: Python

Libraries:

librosa – for audio loading and MFCC feature extraction

scikit-learn – for feature scaling and SVM classification

joblib – for saving and loading models

numpy – for numerical operations

Google Colab – for easy file uploads and execution

# 🚀 Features
User Enrollment:
Uploads two .wav files (user and non-user), extracts features, and trains an SVM model.

Voice Authentication:
Authenticates a new voice sample against the trained model and returns success or failure with confidence.

Feature Extraction:
Uses MFCC along with delta and delta-delta features to enhance speaker recognition.

Persistence:
Saves both the trained model and scaler to disk for future use.

# 🔧 How It Works
Step 1: User Enrollment
Upload a voice sample of the user and a non-user.

The system extracts features and trains an SVM classifier.

Saves the model (voice_auth_model.pkl) and scaler (scaler.pkl).

Step 2: Authentication
Upload a test .wav voice sample.
The system compares it with the enrolled model.
Based on the predicted probability, it authenticates the speaker.
