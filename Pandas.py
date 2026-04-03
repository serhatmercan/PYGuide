import numpy as np
import pandas as pd

# Series: A one-dimensional labeled array capable of holding any data type.

# Creating a Series from a dictionary
grades = {"Math": 90, "Science": 85, "English": 88}

grades_series = pd.Series(grades)
# Output the Series 
# Math       90
# Science    85
# English    88
# dtype: int64

# Series with custom index
names = ["Alice", "Bob", "Charlie"]
grades = [90, 85, 88]
grades_series = pd.Series(data=grades, index=names)
# Alice      90
# Bob        85
# Charlie    88
# dtype: int64

# Creating Series
contest_result_1 = pd.Series(data=[75, 25, 80], index=["Alice", "Bob", "Charlie"])
contest_result_2 = pd.Series(data=[80, 30, 85], index=["Alice", "Bob", "Charlie"])
contest_result_3 = pd.Series(data=[85, 35, 90], index=["Alice", "Mike", "Charlie"])

# Accessing values in a Series
contest_result_1["Alice"] # Output: 75

# Adding two Series together
contest_result_1 + contest_result_2
# Output:
# Alice      155
# Bob         55
# Charlie    165
# dtype: int64    

# Adding two Series together with different indices
contest_result_1 + contest_result_3
# Output:
# Alice      160
# Bob        NaN
# Charlie    170
# dtype: int64

# DataFrame: A two-dimensional labeled data structure with columns of potentially different types.

# Creating a DataFrame from a 2D array
data = np.random.randint(1, 100, (4, 3 )) # Output: 4x3 array of random integers between 1 and 99, e.g., array([[83, 53, 70], [44, 60, 89], [12, 34, 56], [78, 90, 12]])

data_frame = pd.DataFrame(data) 
# Output: DataFrame with 4 rows and 3 columns, e.g.,
#     0   1   2
# 0  83  53  70
# 1  44  60  89
# 2  12  34  56
# 3  78  90  12

# Creating a DataFrame from a 2D array with custom index and columns
new_df = pd.DataFrame(data, index=["Alice", "Bob", "Charlie", "David"], columns=["Math", "Science", "English"])
# Output: DataFrame with 4 rows and 3 columns, e.g.,
#        Math  Science  English
# Alice    83       53       70
# Bob      44       60       89
# Charlie  12       34       56
# David    78       90       12

# Accessing columns in a DataFrame
new_df["Math"] # Output: Series with Math scores, e.g.,
# Alice      83
# Bob        44
# Charlie    12
# David      78

# Accessing multiple columns in a DataFrame
new_df[["Math", "Science"]] # Output: DataFrame with Math and Science scores, e.g.,
#        Math  Science
# Alice    83       53
# Bob      44       60
# Charlie  12       34
# David    78       90

# Accessing rows in a DataFrame with loc
new_df.loc["David"] # Output: Series with David's scores, e.g.,
# Math       78
# Science    90
# English    12
# Name: David, dtype: int64

# Accessing multiple rows in a DataFrame with loc
new_df.loc["Bob":"Charlie"] # Output: DataFrame with Bob and Charlie's scores, e.g.,
#        Math  Science  English
# Bob      44       60       89
# Charlie  12       34       56

# Accessing a specific value in a DataFrame with loc
new_df.loc["David", "Science"] # Output: 90

# Updating a specific value in a DataFrame with loc
new_df.loc["David", "Science"] = 95 # Update David's Science score to 95
# Output: DataFrame with updated Science score for David, e.g.,
#        Math  Science  English
# Alice    83       53       70
# Bob      44       60       89
# Charlie  12       34       56     
# David    78       95       12

# Accessing rows in a DataFrame with iloc
new_df.iloc[0] # Output: Series with Alice's scores, e.g.,
# Math       83
# Science    53
# English    70
# Name: Alice, dtype: int64

# Accessing multiple rows in a DataFrame with loc
new_df.loc["Bob":"Charlie"] # Output: DataFrame with Bob and Charlie's scores, e.g.,
new_df.iloc[1:3] # Output: DataFrame with Bob and Charlie's scores, e.g.,
#        Math  Science  English
# Bob      44       60       89
# Charlie  12       34       56

# Adding a new column to the DataFrame with assignment
new_df["Chemistry"] = [85, 90, 80, 95] 
# Output: DataFrame with a new column "Chemistry", e.g.,
#        Math  Science  English  Chemistry
# Alice    83       53       70         85
# Bob      44       60       89         90
# Charlie  12       34       56         80
# David    78       95       12         95

# Removing a column from the DataFrame with drop
new_df.drop("Chemistry", axis=1, inplace=True)
# Output: DataFrame with the "Chemistry" column removed, e.g.,
#        Math  Science  English 
# Alice    83       53       70
# Bob      44       60       89
# Charlie  12       34       56
# David    78       95       12

# Conditional selection in a DataFrame
new_df[new_df["Math"] > 50] 
# Output: DataFrame with rows where Math score is greater than 50, e.g.,
#        Math  Science  English
# Alice    83       53       70
# David    78       95       12

# Resetting the index of the DataFrame
new_df.reset_index(inplace=True)
# Output: DataFrame with the index reset to default integer index, e.g.,
#      index  Math  Science  English
# 0    Alice    83       53       70
# 1      Bob    44       60       89
# 2  Charlie    12       34       56
# 3    David    78       95       12

# Setting a new index for the DataFrame
new_indices = ["Student1", "Student2", "Student3", "Student4"]
new_df.set_index(new_indices, inplace=True)
# Output: DataFrame with the new index set to "Student1", "Student2", "Student3", "Student4", e.g.,
#           index  Math  Science  English
# Student1  Alice    83       53       70
# Student2    Bob    44       60       89   
# Student3 Charlie    12       34       56
# Student4   David    78       95       12

# Multi Indexing in a DataFrame
first_index = ["Group1", "Group1", "Group2", "Group2"]
inner_index = ["Alice", "Bob", "Charlie", "David"]
zipped_index = list(zip(first_index, inner_index)) # Output: [('Group1', 'Alice'), ('Group1', 'Bob'), ('Group2', 'Charlie'), ('Group2', 'David')]
multi_index = pd.MultiIndex.from_tuples(zipped_index) # Output: MultiIndex with two levels, e.g., MultiIndex([('Group1', 'Alice'), ('Group1', 'Bob'), ('Group2', 'Charlie'), ('Group2', 'David')], names=[None, None])
sample_values = np.ones((4, 2)) # Output: 4x2 array of ones, e.g., array([[1., 1.], [1., 1.], [1., 1.], [1., 1.]])
multi_index_df = pd.DataFrame(sample_values, index=multi_index, columns=["Value1", "Value2"])
# Output: DataFrame with MultiIndex and two columns "Value1" and "Value2 ", e.g.,
#                Value1  Value2
# Group1 Alice     1.0     1.0
#        Bob       1.0     1.0
# Group2 Charlie   1.0     1.0
#        David     1.0     1.0

# Accessing elements in a DataFrame with MultiIndex
multi_index_df.loc["Group1"]
# Output: DataFrame with rows corresponding to "Group1", e.g.,
#        Value1  Value2
# Alice     1.0     1.0
# Bob       1.0     1.0

# Accessing elements in a DataFrame with MultiIndex using multiple levels of indexing
multi_index_df.loc["Group1"].loc["Alice"]
# Output: Series with values corresponding to "Group1" and "Alice", e.g.,
# Value1    1.0
# Value2    1.0