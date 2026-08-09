import numpy as np
import seaborn as sns

# Load the dataset
# Originally read a local CSV ('...csv', a broken placeholder path); swapped
# to seaborn's tips dataset (approved 2026-08-09) so this file is self-contained
df = sns.load_dataset("tips")

# Independent and Dependent Features
X = df[['total_bill']]
y = df['tip']

# === 1. Model Selection ===
# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split

# 20% of the data will be used for testing, and the random_state is set to 42 for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === 2. Feature Scaling ===
from sklearn.preprocessing import StandardScaler

# Create an instance of the StandardScaler
scaler = StandardScaler()

# Fit the scaler to the training data and transform both the training and testing data
X_train = scaler.fit_transform(X_train) # Fit the scaler to the training data and transform it
X_test = scaler.transform(X_test) # Transform the testing data using the same scaler fitted on the training data

# === 3. Model Training ===
# Train the Linear Regression model
from sklearn.linear_model import LinearRegression

regression = LinearRegression() # Create an instance of the LinearRegression model
regression.fit(X_train, y_train) # Fit the model to the training data

print("Coefficient : ", regression.coef_) # Output: Coefficient :  [0.93571714]
print("Intercept : ", regression.intercept_) # Output: Intercept :  3.0877948717948724

# === 4. Model Evaluation ===
# Import the mean_squared_error, mean_absolute_error, and r2_score functions from the sklearn.metrics module
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Predict the tip amounts for the testing data using the trained model
y_pred_test = regression.predict(X_test)

mse = mean_squared_error(y_test, y_pred_test) # Output: 0.5688142529229538
mae = mean_absolute_error(y_test, y_pred_test) # Output: 0.6208580000398983
rmse = np.sqrt(mse) # Output: 0.7541977545199626
r2 = r2_score(y_test, y_pred_test) # Output: 0.5449381659234664
adjusted_r2 = 1 - (1-r2)*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1) # Output: 0.535255999240987
