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

## Results 
Database Results :
![image](https://github.com/user-attachments/assets/b35022d8-b527-4fa4-8029-2ceec65888a7)

Company Stock Prices :
![image](https://github.com/user-attachments/assets/7ca8f80f-af3f-4bc7-90ba-621a2bffab9f)

Data Merging Results : 
![image](https://github.com/user-attachments/assets/4f3a7d66-f994-4b38-bfe4-8e48b64fbad2)

ROC Curve :
![image](https://github.com/user-attachments/assets/076efa19-63b2-4564-9adc-9630e45bec8a)

Final Layoff Prediction :
![image](https://github.com/user-attachments/assets/444609a2-6d46-46ba-9f79-aaba5dbf1f5b)


## Repository
[GitHub Link](https://github.com/HarshLahane78/Layoff_Prediction_System)

## Future Enhancements
- Deploying a Flask-based API for real-time predictions
- Expanding dataset to improve model accuracy
- Implementing deep learning techniques

## Author
**Harshwardhan Lahane**
