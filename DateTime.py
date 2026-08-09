import pandas as pd

# Load the dataset
df = pd.read_csv('data/support_tickets.csv')

# Convert the 'Created Date' column to datetime format
df['Created Date'] = pd.to_datetime(df['Created Date']) # Converts text dates (e.g. "February 11, 2018") to datetime64 values (e.g. 2018-02-11)
df['Created Date']
# Output:
# 0   2018-02-11
# 1   2019-03-03
# 2   2020-07-22
# 3   2021-01-05
# 4   2022-11-30
# Name: Created Date, dtype: datetime64[us]
# Behaviour varies by version: pandas <2.0 defaults to datetime64[ns]
# instead of datetime64[us] - the dates themselves convert the same way.

# === Standard Library datetime ===
from datetime import datetime, timedelta

# Current date and time (non-deterministic - value depends on when you run it)
datetime.now() # Output: varies, e.g. datetime.datetime(2026, 8, 9, 14, 30, 5, 123456)

# Creating a specific date
my_date = datetime(2018, 2, 11) # Output: datetime.datetime(2018, 2, 11, 0, 0)

# Formatting a datetime as a string
my_date.strftime("%Y-%m-%d")   # Output: '2018-02-11'
my_date.strftime("%B %d, %Y")  # Output: 'February 11, 2018'

# Parsing a string into a datetime
datetime.strptime("February 11, 2018", "%B %d, %Y") # Output: datetime.datetime(2018, 2, 11, 0, 0)

# Date arithmetic with timedelta
my_date + timedelta(days=30) # Output: datetime.datetime(2018, 3, 13, 0, 0)
my_date - timedelta(days=10) # Output: datetime.datetime(2018, 2, 1, 0, 0)