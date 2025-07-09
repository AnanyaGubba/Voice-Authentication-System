# Voice-Authentication-System

# 📌 1. Project Description

This project implements a basic voice-based authentication system leveraging machine learning techniques. It uses audio feature extraction (MFCC and its derivatives) to model and recognize a specific speaker’s voice. The system enables a user to enroll with their voice and then authenticate future voice inputs using a trained Support Vector Machine (SVM) classifier.

The application is ideal for exploring the fundamentals of speaker recognition and machine learning-based audio processing.



# 🧑‍💻 2. Tech Stack Used
Programming Language: Python

Libraries:

1. librosa – for audio loading and MFCC feature extraction

2. scikit-learn – for feature scaling and SVM classification

3. joblib – for saving and loading models

4. numpy – for numerical operations

5. Google Colab – for easy file uploads and execution

# 🚀 3. Features
- User Enrollment:
Uploads two .wav files (user and non-user), extracts features, and trains an SVM model.

- Voice Authentication:
Authenticates a new voice sample against the trained model and returns success or failure with confidence.

- Feature Extraction:
Uses MFCC along with delta and delta-delta features to enhance speaker recognition.

- Persistence:
Saves both the trained model and scaler to disk for future use.

# 🔧 4. How It Works
1. User Enrollment:

- The user uploads:

  - Their own .wav voice sample

  - A non-user .wav sample

- MFCC + delta features are extracted from both.

- A binary SVM classifier is trained and saved.

2. Authentication:

- The user uploads a new .wav sample.

- The model extracts features and predicts whether it matches the enrolled user.

- Authentication success/failure is reported based on probability threshold.
