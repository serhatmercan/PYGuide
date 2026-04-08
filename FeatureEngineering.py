import seaborn as sns

# Load the Titanic dataset
df = sns.load_dataset("titanic")

# Check for missing values in the dataset
df.isnull().sum() 
# Output: 
# age         177
# embarked      2
# deck         688
# embark_town   2
# dtype: int64

# Drop the 'deck' column due to high number of missing values
df.drop(columns=["deck"], inplace=True)  

# Imputation: Fill missing values in 'age' with the median age
# Mean Imputation
df["age_mean"] = df["age"].fillna(df["age"].mean()) # Fill missing values in 'age' with the mean age

# Median Imputation
df["age_median"] = df["age"].fillna(df["age"].median()) # Fill missing values in 'age' with the median age

# Mode Imputation (for categorical variables)
df["embarked_mode"] = df["embarked"].fillna(df["embarked"].mode()[0]) # Fill missing values in 'embarked' with the mode