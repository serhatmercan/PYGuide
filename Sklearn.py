import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the dataset
df = pd.read_csv('...csv')

# Independent and Dependent Features
X = df[['Study Hours']]
y = df['Exam Score']

# 1- Model Selection
# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split

# 20% of the data will be used for testing, and the random_state is set to 42 for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2- Data Visualization
# Feature Scaling
from sklearn.preprocessing import StandardScaler

# Create an instance of the StandardScaler
scaler = StandardScaler()

# Fit the scaler to the training data and transform both the training and testing data
X_train = scaler.fit_transform(X_train) # Fit the scaler to the training data and transform it
X_test = scaler.transform(X_test) # Transform the testing data using the same scaler fitted on the training data

# 3- Model Training
# Train the Linear Regression model
from sklearn.linear_model import LinearRegression

regression = LinearRegression() # Create an instance of the LinearRegression model
regression.fit(X_train, y_train) # Fit the model to the training data

print("Coefficient : ", regression.coef_) # Print the coefficient (slope) of the linear regression model -> Coefficient :  [17.77325513]
print("Intercept : ", regression.intercept_) # Print the intercept of the linear regression model -> Intercept :  71.58461538461538

# 4- Model Evaluation
# Import the mean_squared_error, mean_absolute_error, and r2_score functions from the sklearn.metrics module
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 

# Predict the exam scores for the testing data using the trained model
y_pred_test = regression.predict(X_test) 

mse = mean_squared_error(y_test, y_pred_test) # Calculate the mean squared error between the actual exam scores (y_test) and the predicted exam scores (y_pred_test) for the testing data
mae = mean_absolute_error(y_test, y_pred_test) # Calculate the mean absolute error between the actual exam scores (y_test) and the predicted exam scores (y_pred_test) for the testing data
rmse = np.sqrt(mse) # Calculate the root mean squared error between the actual exam scores (y_test) and the predicted exam scores (y_pred_test) for the testing data
r2 = r2_score(y_test, y_pred_test) # Calculate the R-squared score between the actual exam scores (y_test) and the predicted exam scores (y_pred_test) for the testing data
adjusted_r2 = 1 - (1-r2)*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1) # Calculate the adjusted R-squared score for the testing data