PCOS and PCOD Detection Using CNN Architecture
Project Overview

Polycystic Ovary Syndrome (PCOS) and Polycystic Ovarian Disease (PCOD) are common hormonal disorders affecting women. Early and accurate detection is important for effective treatment and health management.

This project presents a deep learning based system using Convolutional Neural Networks (CNN) to automatically analyze ovarian ultrasound images and classify them as PCOS, PCOD, or Normal.

The system assists doctors by providing fast, accurate, and automated diagnosis support.

Problem Statement

Detecting PCOS and PCOD using traditional medical analysis can be time-consuming and highly dependent on clinical expertise. Manual interpretation of ultrasound images may lead to delays and inconsistencies.

Therefore, an AI-based automated system is needed to analyze ultrasound images and detect PCOS/PCOD patterns efficiently.

Proposed Solution

The proposed system uses a CNN-based deep learning model to automatically analyze ovarian ultrasound images and identify cyst patterns related to PCOS/PCOD.

The model processes the images, extracts important features, and classifies them into the appropriate category.

This helps in:

Early detection of PCOS/PCOD

Reducing human diagnostic errors

Supporting doctors in medical decision-making

Features

Automated CNN-based ultrasound image analysis

Early and reliable PCOS/PCOD detection

Fast classification of images into PCOS / PCOD / Normal

Improved accuracy using data augmentation

Consistent and unbiased diagnostic results

Scalable system suitable for hospitals and clinics

Technologies Used
Google Technologies

Google Colab – Model training and experimentation

Google Drive – Dataset storage and management

Google Cloud Platform (Optional) – Model deployment

Programming & Frameworks

Python

TensorFlow / Keras

CNN Architecture

OpenCV

NumPy

Matplotlib

System Architecture

The system consists of the following modules:

1. Data Collection Module

Collects labeled ovarian ultrasound images categorized as:

PCOS

PCOD

Normal

2. Data Preprocessing Module

Image preprocessing techniques include:

Image resizing

Noise removal

Image normalization

Data augmentation

3. CNN Architecture Module

The CNN model extracts features from images using layers such as:

Convolution layers

Pooling layers

Flatten layer

Fully connected layers

4. Model Training Module

The model is trained using labeled data and optimized through backpropagation.

5. Model Evaluation Module

The model performance is evaluated using:

Accuracy

Precision

Recall

Confusion Matrix

6. Deployment Module

The trained model is saved as .h5 file and integrated into a web-based application using Django.

7. User Interaction Module

Users can upload ultrasound images and receive automated detection results.

Workflow

Collect ultrasound image dataset

Perform image preprocessing

Train CNN model on labeled dataset

Evaluate model performance

Save trained model

Deploy model for prediction

Upload ultrasound image for detection

Output

The system predicts one of the following results:

PCOS Detected

PCOD Detected

Normal Ovary

Future Enhancements

Integration with hospital management systems

Real-time diagnosis support

Mobile application for remote healthcare

Multilingual interface for rural accessibility

Secure patient data handling

Conclusion

This project demonstrates how Artificial Intelligence and Deep Learning can assist in early detection of PCOS and PCOD. The system provides an efficient, scalable, and reliable solution to support healthcare professionals in medical diagnosis.
