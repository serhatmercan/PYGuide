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

# Drop duplicate values in the "Math" column, keeping only the first occurrence
new_df = new_df.drop_duplicates(subset='Math', keep='first') # Output: DataFrame with duplicate values in the "Math" column removed

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

# Setting display options for floating-point numbers in Pandas
new_df.set_option('display.float_format', '{:.4f}'.format)

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

# Reading data from an Excel file into a DataFrame
excel_df = pd.read_excel('excel.xlsx')
# Output: DataFrame containing the data from the Excel file, e.g.,
#       Istanbul  New York  Amsterdam  Paris
# 0        20        10         15     12
# 1        21        10         17     14
# 2        20        13         18     15
# 3        22        14         19     18
# 4        25        15         15     20
# 5        28        13         22     16
# 6        15        12         15     15
# 7        20        15         14     14
# 8        22        16         16     16

# Displaying the first few rows of the DataFrame
excel_df.head() # Output: First 5 rows of the DataFrame, e.g.,
#       Istanbul  New York  Amsterdam  Paris
# 0        20        10         15     12
# 1        21        10         17     14
# 2        20        13         18     15
# 3        22        14         19     18
# 4        25        15         15     20   

# Displaying the last few rows of the DataFrame
excel_df.tail() # Output: Last 5 rows of the DataFrame, e.g.,
#       Istanbul  New York  Amsterdam  Paris
# 3        22        14         19     18
# 4        25        15         15     20
# 5        28        13         22     16
# 6        15        12         15     15
# 7        20        15         14     14

# Display the info and summary statistics of the DataFrame
excel_df.info() # Output: Information about the DataFrame, e.g.,
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 9 entries, 0 to 8
# Data columns (total 4 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Istanbul   9 non-null      int64
#  1   New York   9 non-null      int64
#  2   Amsterdam  9 non-null      int64
#  3   Paris      9 non-null      int64
# dtypes: int64(4)
# memory usage: 416.0 bytes

# Displaying summary statistics of the DataFrame
excel_df.describe() # Output: Summary statistics of the DataFrame, e.g.,
#         Istanbul  New York    Amsterdam  Paris
# count   9.000000   9.000000   9.000000    9.000000
# mean   21.666667  13.444444   17.000000  15.555556
# std     3.162278   1.966287    2.449490   2.449490
# min    15.000000  10.000000   14.000000  12.000000
# 25%    20.000000  12.000000   15.000000  14.000000
# 50%    21.000000  13.000000   17.000000  15.000000   
# 75%    22.000000  15.000000   18.000000  16.000000
# max    28.000000  16.000000   22.000000  20.000000

# Displaying the count of non-null values in each column of the DataFrame
excel_df.count() # Output: Count of non-null values in each column, e.g.,
# Istanbul     9
# New York     9
# Amsterdam    9
# Paris        9
# dtype: int64

# Display the number of missing values in each column of the DataFrame
excel_df.isna() # Output: DataFrame indicating the presence of NaN values, e.g.,
#      Istanbul  New York   Amsterdam   Paris
# 0     False      False      False     False
# 1     False      False      False     False
# 2     False      False      False     False
# 3     False      False      False     False
# 4     False      False      False     False  
# 5     False      False      False     False
# 6     False      False      False     False

# Reading data from an Excel file into a DataFrame with missing values
excel_na_df = pd.read_excel('excel_na.xlsx') # Output: DataFrame containing the data from the Excel file with missing values, e.g.,
#       Istanbul  New York  Amsterdam  Paris
# 0      20.0      10.0       15.0   12.0
# 1      21.0      10.0        NaN   14.0
# 2       NaN      13.0       18.0   15.0
# 3      22.0      14.0       19.0   18.0
# 4      25.0      15.0       15.0   20.0
# 5      28.0       NaN       22.0    NaN
# 6      15.0      12.0       15.0   15.0
# 7      20.0      15.0       14.0    NaN
# 8      22.0      16.0       16.0    NaN

# Display the number of missing values in each column of the DataFrame with missing values
excel_na_df.isna() # Output: DataFrame indicating the presence of NaN values, e.g.,
#      Istanbul  New York  Amsterdam  Paris
# 0     False     False      False  False
# 1     False     False       True  False
# 2      True     False      False  False
# 3     False     False      False  False
# 4     False     False      False  False
# 5     False      True      False   True
# 6     False     False      False  False
# 7     False     False      False   True
# 8     False     False      False   True

# Display the values in the "Paris" column of the DataFrame with missing values
excel_na_df['Paris'] # Output: Series with the values in the "Paris" column, e.g.,
# 0    12.0
# 1    14.0
# 2    15.0
# 3    18.0
# 4    20.0
# 5     NaN
# 6    15.0 
# 7     NaN
# 8     NaN
# Name: Paris, dtype: float64

# Display the count of non-null values in the "Paris" column of the DataFrame with missing values
excel_na_df['Paris'].count() # Output: Count of non-null values in the "Paris" column, e.g., 6

# Display the number of missing values in the "Paris" column of the DataFrame with missing values
excel_na_df['Paris'].isna() # Output: Series indicating the presence of NaN values in the "Paris" column, e.g.,
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5     True
# 6    False
# 7     True
# 8     True

# Removing the "Paris" column from the DataFrame with missing values
excel_na_df.drop("Paris", axis=1) # Output: DataFrame with the "Paris" column removed, e.g.,
#       Istanbul  New York  Amsterdam
# 0        20        10         15
# 1        21        10         17
# 2        20        13         18
# 3        22        14         19
# 4        25        15         15
# 5        28        13         22
# 6        15        12         15
# 7        20        15         14
# 8        22        16         16

# Removing a specific row from the DataFrame with missing values
excel_na_df.drop(excel_na_df.index[2]) # Output: DataFrame with the row at index 2 removed

# Removing rows with NaN values from the DataFrame
excel_na_df.dropna() # Output: DataFrame with rows containing NaN values removed, e.g.,
#    Istanbul  New York  Amsterdam  Paris
# 0        20        10         15   12.0
# 1        21        10         17   14.0
# 2        20        13         18   15.0
# 3        22        14         19   18.0

# Filling NaN values in the DataFrame with a specific value
excel_na_df.fillna(20) # Output: DataFrame with NaN values filled with 20, e.g.,
#    Istanbul  New York  Amsterdam  Paris
# 0        20        10         15   12.0
# 1        21        10         17   14.0
# 2        20        13         18   15.0
# 3        22        14         19   18.0
# 4        25        15         15   20.0
# 5        28        13         22   20.0
# 6        15        12         15   15.0
# 7        20        15         14   20.0
# 8        22        16         16   20.0

# Filling NaN values in the DataFrame with the mean of each column
excel_na_df.fillna(excel_na_df.mean()) # Output: DataFrame with NaN values filled with the mean of each column, e.g.,
#    Istanbul    New York   Amsterdam  Paris
# 0  20.000000  10.000000   15.000000  12.000000
# 1  21.000000  10.000000   17.000000  14.000000
# 2  20.000000  13.000000   18.000000  15.000000
# 3  22.000000  14.000000   19.000000  18.000000
# 4  25.000000  15.000000   15.000000  20.000000
# 5  28.000000  13.000000   22.000000  15.555556
# 6  15.000000  12.000000   15.000000  15.000000
# 7  20.000000  15.000000   14.000000  15.555556
# 8  22.000000  16.000000   16.000000  15.555556

# Reading data from a CSV file into a DataFrame
csv_df = pd.read_csv('csv_df.csv') # Output: DataFrame containing the data from the CSV file, e.g.,
#    Department Employee  Salary  Experience           City
# 0   Marketing    Emp_1   53483           1       New York
# 1       Sales    Emp_2   78555           8         Austin
# 2     Finance    Emp_3   47159           3         Austin
# 3       Sales    Emp_4  110077           3  San Francisco
# 4       Sales    Emp_5   65920           1       New York
# 5          IT    Emp_6   97121          11        Chicago
# 6     Finance    Emp_7   99479           5        Chicago
# 7     Finance    Emp_8  119475          10       New York
# 8     Finance    Emp_9   49457           7        Chicago
# 9       Sales   Emp_10   96557          10        Chicago
# 10  Marketing   Emp_11  107189           9       New York
# 11    Finance   Emp_12  108953          12         Austin
# 12      Sales   Emp_13   82995           7       New York
# 13         IT   Emp_14   70757           9         Austin
# 14  Marketing   Emp_15   39692           8        Chicago
# 15         IT   Emp_16   75758          12        Chicago
# 16  Marketing   Emp_17  102409           2        Chicago
# 17      Sales   Emp_18  101211           1  San Francisco
# 18         HR   Emp_19   95697           7         Austin
# 19  Marketing   Emp_20   67065           7  San Francisco
# 20         IT   Emp_21   62606          14  San Francisco
# 21      Sales   Emp_22   41534           8       New York
# 22  Marketing   Emp_23   70397           5  San Francisco
# 23         HR   Emp_24   31016           3       New York
# 24         HR   Emp_25  119789          12       New York
# 25    Finance   Emp_26   85591           8  San Francisco
# 26    Finance   Emp_27  119812           6         Austin
# 27         IT   Emp_28   53247          11         Austin
# 28  Marketing   Emp_29   54300           3         Austin
# 29  Marketing   Emp_30  104065           1         Austin
# 30    Finance   Emp_31  112798           3         Austin
# 31  Marketing   Emp_32   39268           5  San Francisco
# 32  Marketing   Emp_33  116807          14  San Francisco
# 33         HR   Emp_34   42185           3        Chicago
# 34    Finance   Emp_35   93704           1         Austin
# 35      Sales   Emp_36  116779           5  San Francisco
# 36    Finance   Emp_37   69099          10        Chicago
# 37      Sales   Emp_38   38571           7         Austin
# 38         HR   Emp_39   68044          14       New York
# 39         IT   Emp_40   81214           7        Chicago
# 40  Marketing   Emp_41   91228          11  San Francisco
# 41         HR   Emp_42   78984           9       New York
# 42  Marketing   Emp_43   70774          10       New York
# 43         IT   Emp_44   32568          10       New York
# 44         IT   Emp_45   92592          12        Chicago
# 45         HR   Emp_46   97563          13  San Francisco
# 46         IT   Emp_47   32695           3       New York
# 47      Sales   Emp_48   78190           7         Austin
# 48         IT   Emp_49   35258           1       New York
# 49  Marketing   Emp_50  117538           4       New York

csv_df.describe() # Output: Summary statistics of the DataFrame, e.g.,
# Output: Summary statistics of the DataFrame, e.g.,
#              Salary  Experience
# count      50.000000   50.000000
# mean    78344.500000    7.060000
# std     27817.603904    3.966235
# min     31016.000000    1.000000
# 25%     53687.250000    3.000000
# 50%     78769.500000    7.000000
# 75%    100778.000000   10.000000
# max    119812.000000   14.000000

# Calculating the mean of the "Salary" column in the DataFrame
csv_df['Salary'].mean() # Output: Mean of the "Salary" column, e.g., 78344.5

csv_df[['Salary', 'Experience']].mean() # Output: Mean of the "Salary" and "Experience" columns, e.g., 
# Salary        78344.5
# Experience    7.06

# Experience greater than 5 
csv_df[csv_df['Experience'] > 5].count() # Output: Count of non-null values in each column for rows where Experience is greater than 5, e.g.,
# Department    28
# Employee      28
# Salary        28
# Experience    28
# City          28

# Grouping the DataFrame by the "Department" column
csv_df_department_grouped = csv_df.groupby('Department') # Output: DataFrameGroupBy object grouped by the "Department" column

# Displaying the count of non-null values in each column for each department
csv_df_department_grouped.count() # Output: Count of non-null values in each column for each department, e.g.,
#              Employee  Salary  Experience  City
# Department
# HR              6       6           6     6
# IT              8       8           8     8
# Finance         9       9           9     9
# Marketing       10      10          10    10
# Sales           17      17          17    17

# Concatenating two DataFrames vertically (stacking them on top of each other)
csv_df_1 = pd.read_csv('csv_df_1.csv')
csv_df_2 = pd.read_csv('csv_df_2.csv')

# Concatenating the two DataFrames while ignoring the index to create a new DataFrame with a continuous index
df_concat = pd.concat([csv_df_1, csv_df_2], ignore_index=True) # Output: DataFrame resulting from concatenating csv_df_1 and csv_df_2

# Merging two DataFrames based on a common column using an inner join to create a new DataFrame that includes only the rows with matching values in the "Employee_ID" column
df_merged = pd.merge(csv_df_1, csv_df_2, on="Employee_ID", how="inner") # Output: DataFrame resulting from merging csv_df_1 and csv_df_2 on the "Employee_ID" column

# Merging two DataFrames based on a common column using an outer join to include all rows from both DataFrames
df_merged = pd.merge(csv_df_1, csv_df_2, on="Employee_ID", how="outer") # Output: DataFrame resulting from merging csv_df_1 and csv_df_2 on the "Employee_ID" column using an outer join

# Merging two DataFrames based on a common column using a left join to include all rows from the left DataFrame (csv_df_1) and matching rows from the right DataFrame (csv_df_2)
df_merged = pd.merge(csv_df_1, csv_df_2, on="Employee_ID", how="left") # Output: DataFrame resulting from merging csv_df_1 and csv_df_2 on the "Employee_ID" column using a left join

# Merging two DataFrames based on a common column using a right join to include all rows from the right DataFrame (csv_df_2) and matching rows from the left DataFrame (csv_df_1)
df_merged = pd.merge(csv_df_1, csv_df_2, on="Employee_ID", how="right") # Output: DataFrame resulting from merging csv_df_1 and csv_df_2 on the "Employee_ID" column using a right join

# Apply: Defining a function to categorize salaries as "Low", "Medium", or "High" based on the salary amount
def salary_status(salary):
    if salary < 50000:
        return "Low"
    elif salary < 100000:
        return "Medium"
    else:
        return "High"
    
# Applying the salary_status function to the "Salary" column of the DataFrame to create a new column "Salary_Status" that categorizes salaries as "Low", "Medium", or "High"
csv_df['Salary_Status'] = csv_df['Salary'].apply(salary_status) # Output: DataFrame with a new column "Salary_Status" that categorizes salaries based on the salary_status function, e.g.,
#    Department Employee  Salary  Experience           City Salary_Status
# 0   Marketing    Emp_1   53483           1       New York         Medium
# 1       Sales    Emp_2   78555           8         Austin         Medium
# 2     Finance    Emp_3   47159           3         Austin         Medium
# 3       Sales    Emp_4  110077           3  San Francisco         High
# 4       Sales    Emp_5   65920           1       New York         Medium
# 5          IT    Emp_6   97121          11        Chicago         High

# Apply: Defining a function to calculate an extra bonus based on the performance score and experience of an employee
def performance_extra_bonus(row):
    if row["Experience"] > 10:
        return row["Performance_Score"] * 1.5
    else:
        return row["Performance_Score"]

# Applying the performance_extra_bonus function to each row of the DataFrame to create a new column "Extra_Bonus" that calculates the extra bonus based on the performance_extra_bonus function, e.g.,
csv_df['Extra_Bonus'] = csv_df.apply(performance_extra_bonus, axis=1) # Output: DataFrame with a new column "Extra_Bonus" that calculates the extra bonus based on the performance_extra_bonus function, e.g.,    
#    Department Employee  Salary  Experience           City Salary_Status  Performance_Score  Extra_Bonus
# 0   Marketing    Emp_1   53483           1       New York         Medium                 3          3.0
# 1       Sales    Emp_2   78555           8         Austin         Medium                 4          4.0
# 2     Finance    Emp_3   47159           3         Austin         Medium                 2          2.0
# 3       Sales    Emp_4  110077           13  San Francisco        High                   5          7.5
# 4       Sales    Emp_5   65920           1       New York         Medium                 3          3.0
# 5          IT    Emp_6   97121           11        Chicago        High                   4          6.0

csv_df["Formatted_Name"] = csv_df["Employee"].apply(lambda x: x.replace("_", " ")) # Output: DataFrame with a new column "Formatted_Name" that contains the employee names with underscores replaced by spaces, e.g.,
#    Department Employee  Salary  Experience           City Salary_Status  Performance_Score  Extra_Bonus Formatted_Name
# 0   Marketing    Emp_1   53483           1       New York         Medium                 3          3.0       Emp 1
# 1       Sales    Emp_2   78555           8         Austin         Medium                 4          4.0       Emp 2
# 2     Finance    Emp_3   47159           3         Austin         Medium                 2          2.0       Emp 3    
# 3       Sales    Emp_4  110077           13  San Francisco        High                   5          7.5       Emp 4
# 4       Sales    Emp_5   65920           1       New York         Medium                 3          3.0       Emp 5
# 5          IT    Emp_6   97121           11        Chicago        High                   4          6.0       Emp 6

# Displaying the count of numeric values in the 'X' column of the DataFrame
csv_df['X'].str.isnumeric().sum() # Output: Count of numeric values in the 'X' column, e.g., 10

# ~ operator is used to negate the boolean values returned by str.isnumeric() to filter out non-numeric values in the 'X' column of the DataFrame
csv_df[~csv_df['X'].str.isnumeric()]['X'] # Output: Series containing non-numeric values in the 'X' column

# str.replace method is used to replace occurrences of "M" with "000" in the 'X' column of the DataFrame, effectively converting values like "5M" to "5000"
csv_df["X"] = csv_df["X"].str.replace("M", "000") # Output: DataFrame with the 'X' column updated by replacing "M" with "000", e.g.,

# astype method is used to convert the data type of the 'X' column to numeric, with errors='coerce' to convert non-numeric values to NaN
csv_df['X'] = csv_df['X'].astype(int, errors='coerce') # Output: DataFrame with the 'X' column converted to numeric data type, with non-numeric values replaced by NaN