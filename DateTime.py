import pandas as pd

# Load the dataset
df = pd.read_csv('abc.csv')

# Convert the 'Created Date' column to datetime format 
df['Created Date'] = pd.to_datetime(df['Created Date']) # Convert to datetime format e.g. (February 11, 2018 -> 2018-02-11)