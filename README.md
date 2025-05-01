# SnapNPlate

SnapNPlate is an AI-powered food image classification system that uses a Convolutional Neural Network (CNN) to classify images of food into 10 different categories. It leverages TensorFlow and Keras for model training, and is integrated with a FastAPI backend for real-time image uploads and predictions.

## Features
- **Real-time Food Classification**: Upload a food image and get the predicted food category.
- **10 Food Categories**: Supports classification of food items such as Donut, Samosa, Dhokla, Idli, etc.
- **Confidence Scores**: Provides confidence levels for predictions, helping users understand the certainty of the model.

## Installation
Follow these steps to get the project running locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/prasannask17/SnapNPlate.git

2.Navigate to the project directory and install the required dependencies:
    cd SnapNPlate
    pip install -r requirements.txt

3.Run the FastAPI server using uvicorn:
    uvicorn main:app --reload
    The API will be available at http://127.0.0.1:8000

## Usage
--Upload Image: Once the backend is running, open your browser and navigate to http://127.0.0.1:8000. The frontend allows you to upload food images.

--Predictions: After uploading an image, the model will predict the food category, such as:

Donut
Chapati
CheeseCake
Dhokla
Idli
Jalebi
KaathiRolls
Kulfi
MasalaDosa
Samosa

--Confidence Levels: The model will also provide a confidence score (e.g., "Jalebi - 90%") to show how confident it is in the prediction.

##Model Training
The model used for food image classification is a Convolutional Neural Network (CNN) built with TensorFlow/Keras. The model is trained on a dataset of food images using techniques such as data augmentation and transfer learning to optimize performance on limited data.

##Model Architecture:
--Convolutional Layers: Detect basic features like edges, textures, and shapes.

--Pooling Layers: Reduce the spatial dimensions and retain important features.

--Dense Layers: Make the final classification decision.

##Optimizer:
The model uses the Adam optimizer for training, which adapts learning rates for each parameter during training.
