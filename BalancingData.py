from imblearn.over_sampling import SMOTE
import numpy as np
import pandas as pd
from sklearn.utils import resample

# Resampling and Encoding Example
# Note: in a real ML workflow, split the data first and resample the training
# set only. Resampling before the split leaks duplicated or synthetic minority
# samples into the test set and inflates the reported scores.

# Seed NumPy's global RNG so the synthetic features below are reproducible
np.random.seed(42)

# Create a sample imbalanced dataset
n_majority = 900
n_minority = 100

# Generate synthetic data for two classes
df1 = pd.DataFrame({
    "feature_1": np.random.normal(loc=0, scale=1, size=n_majority),
    "feature_2": np.random.normal(loc=0, scale=1, size=n_majority),
    "target": [0] * n_majority
})

df2 = pd.DataFrame({
    "feature_1": np.random.normal(loc=0, scale=1, size=n_minority),
    "feature_2": np.random.normal(loc=0, scale=1, size=n_minority),
    "target": [1] * n_minority
})

# Combine the two datasets to create an imbalanced dataset
df = pd.concat([df1, df2]).reset_index(drop=True)
 
# === Upsampling ===
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

# === Downsampling ===
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

# === SMOTE (Synthetic Minority Over-sampling Technique) ===
# Generate synthetic samples for the minority class
# random_state fixes the synthetic samples SMOTE generates, so repeated runs
# produce the same result
oversample = SMOTE(random_state=42)

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