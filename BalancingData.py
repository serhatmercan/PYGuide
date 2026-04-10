from imblearn.over_sampling import SMOTE
import numpy as np
import pandas as pd
import sklearn.utils as resample

# Resampling and Encoding Example
# Create a sample imbalanced dataset
set1no = 900
set2no = 100

# Generate synthetic data for two classes
df1 = pd.DataFrame({
    "feature_1": np.random.normal(loc=0, scale=1, size=set1no),
    "feature_2": np.random.normal(loc=0, scale=1, size=set1no),
    "target": [0] * set1no
})

df2 = pd.DataFrame({
    "feature_1": np.random.normal(loc=0, scale=1, size=set2no),
    "feature_2": np.random.normal(loc=0, scale=1, size=set2no),
    "target": [1] * set2no
})

# Combine the two datasets to create an imbalanced dataset
df = pd.concat([df1, df2]).reset_index(drop=True)
 
# Upsampling
# Increase the number of samples in the minority class
df_minority = df[df['target'] == 1]
df_majority = df[df['target'] == 0]

# Perform upsampling
df_minority_upsampled = resample(df_minority,                   # DataFrame containing the minority class samples
                                 replace=True,                  # Sample with replacement
                                 n_samples=len(df_majority),    # Match the number of majority class samples
                                 random_state=42)               # Set a random state for reproducibility

# Combine the upsampled minority class with the majority class
df_upsampled = pd.concat([df_majority, df_minority_upsampled]).reset_index(drop=True) 

# Check the class distribution after upsampling
df_upsampled['target'].value_counts() 
# Output:
# Class distribution after upsampling: 
# 0    900
# 1    900

# Downsampling
# Decrease the number of samples in the majority class
df_majority_downsampled = resample(df_majority,                  # DataFrame containing the majority class samples
                                   replace=False,                # Sample without replacement
                                   n_samples=len(df_minority),   # Match the number of minority class samples
                                   random_state=42)              # Set a random state for reproducibility

# Combine the downsampled majority class with the minority class
df_downsampled = pd.concat([df_majority_downsampled, df_minority]).reset_index(drop=True)

# Check the class distribution after downsampling
df_downsampled['target'].value_counts()
# Output:
# Class distribution after downsampling:
# 0    100
# 1    100

# SMOTE (Synthetic Minority Over-sampling Technique)
# Generate synthetic samples for the minority class
oversample = SMOTE()

# Apply SMOTE to the features and target variable
(X, y) = oversample.fit_resample(df[["feature_1", "feature_2"]], df["target"]) 

# Combine the features and target variable into a new DataFrame
oversampled_df = pd.concat([X, y], axis=1) 

# Check the class distribution after SMOTE
oversampled_df['target'].value_counts()
# Output:
# Class distribution after SMOTE:
# 0    900
# 1    900