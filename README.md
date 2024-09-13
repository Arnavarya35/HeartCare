# Harnessing Data Analytics for Early Detection of Heart Stroke
A Machine learning-based project for detecting heart disease using various classification algorithms. The project involves data cleaning, training, comparing, and tuning multiple models to predict heart disease, and deploying a web application using Streamlit for prediction.

##**Dataset**
Can be found on Kaggle

##**Models**
The following machine learning models were trained and compared for heart disease detection:

* K-Nearest Neighbors (KNN)
* Logistic Regression
* Random Forest Classifier
* Support Vector Machine (SVM)
* XGBoost

##**Model Comparison and Tuning**
The performance of each model was evaluated using metrics such as accuracy, precision, recall, and F1-score. Based on the results, the top-performing models (KNN, Logistic Regression, and Random Forest) were selected for hyperparameter tuning using GridSearchCV.

##**Model Deployment**
The tuned Random Forest model was used to generate a pickle file, which was then deployed as a web application using Streamlit. The web application allows users to input patient data and receive a prediction of heart disease likelihood.

##**Repository Structure**
data: contains the dataset used for training and testing (heart_disease2.csv)
models: contains the Python scripts for training and tuning each model
deployment: contains the Streamlit web application code and the pickle file generated by the tuned Random Forest model
results: contains the results of model comparison and tuning
