from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
import pandas as pd
import seaborn as sns

# Load the Titanic dataset
df = sns.load_dataset("titanic")

# Check for missing values in the specified columns
df[["sex", "class", "embark_town"]].isna().sum() 
# Output:
# sex           0
# class         0
# embark_town   2

# Drop rows with missing values in 'embark_town'
df = df.dropna(subset=["embark_town"]) 

# === One-Hot Encoding ===
df_one_hot = pd.get_dummies(df, columns=["sex", "embark_town"], drop_first=True)

# Display the columns of the resulting DataFrame
# Only 'sex' and 'embark_town' were one-hot encoded; every other original
# column (including 'deck', 'embarked', 'alive', 'alone') passes through unchanged
df_one_hot.columns
# Output:
# Index(['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare', 'embarked',
#        'class', 'who', 'adult_male', 'deck', 'alive', 'alone', 'sex_male',
#        'embark_town_Queenstown', 'embark_town_Southampton'],
#       dtype='str')
# Behaviour varies by version: pandas 3.x reports dtype='str' for this
# Index; older pandas reports dtype='object' instead.

# === Label Encoding ===
# Create a copy of the original DataFrame to avoid modifying it directly
df_label_encoded = df.copy()

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Encode the 'sex' column and add it as a new column in the DataFrame
df_label_encoded["sex_encoded"] = label_encoder.fit_transform(df_label_encoded["sex"])

# Display the first few rows of the resulting DataFrame
df_label_encoded.head()
# Output:
#    survived  pclass   age     sibsp  parch     fare       class      who   adult_male     embark_town  sex_encoded
# 0         0       3   22.0      1      0      7.2500      Third       man     True        Southampton            1
# 1         1       1   38.0      1      0      71.2833     First       woman   False       Cherbourg              0
# 2         1       3   26.0      0      0      7.9250      Third       woman   False       Southampton            0

# === Ordinal Encoding ===
# Create a copy of the original DataFrame to avoid modifying it directly
df_ordinal_encoded = df.copy()

# Define the order for the 'class' column - position in this list is the
# encoded value, so Third=0, Second=1, First=2
class_order = ["Third", "Second", "First"]

# Initialize the OrdinalEncoder with the specified order for the 'class' column
ordinal_encoder = OrdinalEncoder(categories=[class_order])

# Encode the 'class' column and add it as a new column in the DataFrame
df_ordinal_encoded["class_encoded"] = ordinal_encoder.fit_transform(df_ordinal_encoded[["class"]])

# Display the first few rows of the resulting DataFrame
df_ordinal_encoded.head()
# Output:
#    survived  pclass   age     sibsp  parch     fare       class      who   adult_male     embark_town  class_encoded
# 0         0       3   22.0      1     0      7.2500      Third       man     True        Southampton            0.0
# 1         1       1   38.0      1     0      71.2833     First       woman   False       Cherbourg              2.0
# 2         1       3   26.0      0     0      7.9250      Third       woman   False       Southampton            0.0