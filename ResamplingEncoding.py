import numpy as np
import pandas as pd

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