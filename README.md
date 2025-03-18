# Layoff Prediction System

## Project Overview
The **Layoff Prediction System** is a machine learning-based solution designed to analyze workforce data and predict potential layoffs. It leverages classification models to identify at-risk employees or companies based on various factors.

## Features
- Data preprocessing using Pandas and Scikit-learn
- Model training with multiple classifiers (Random Forest, Gradient Boosting, SVM, etc.)
- Evaluation using accuracy, confusion matrix, and ROC curves
- Interactive visualizations using Matplotlib and Seaborn
- Model serialization with Pickle for future inference

## Dataset
The project utilizes:
- **Employee Dataset** (`JobsDataset_Updated_Experience.csv`): Contains employment-related data
- **Stock Market Data** (`stock_data_100_rows_unique_companies.csv`): Includes financial insights into companies

## Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Flask (for potential API deployment)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/HarshLahane78/Layoff_Prediction_System.git
   cd Layoff_Prediction_System
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook to train and evaluate the models.

## Usage
1. Load the datasets
2. Preprocess data (encoding, scaling, feature selection)
3. Train machine learning models
4. Evaluate performance using classification metrics
5. Save and deploy the trained model

## Repository
[GitHub Link](https://github.com/HarshLahane78/Layoff_Prediction_System)

## Future Enhancements
- Deploying a Flask-based API for real-time predictions
- Expanding dataset to improve model accuracy
- Implementing deep learning techniques

## Author
**Harshwardhan Lahane**
