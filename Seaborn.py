import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size for the plots
plt.figure(figsize=(10, 6)) # This sets the size of the figure to 10 inches wide and 6 inches tall

# Load the tips dataset from Seaborn
tips = sns.load_dataset("tips") # The tips dataset contains information about restaurant bills and tips, including the total bill amount

# === Inspecting the Data ===
# Display the column names of the dataset
tips.columns  # Output: Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='str')
# Behaviour varies by version: pandas 3.x gives an Index of strings dtype
# 'str'; on older pandas this reads dtype='object' instead.

# Show the correlation between numeric columns in the dataset
tips.corr(numeric_only=True)
# Output:   total_bill       tip      size
# total_bill  1.000000  0.675734  0.598315
# tip         0.675734  1.000000  0.489299
# size        0.598315  0.489299  1.000000

# duplicated() marks every occurrence of a value after its first as a
# duplicate row - it doesn't ask "are there any duplicates" as a yes/no.
# "smoker" only has 2 distinct values (Yes/No) across 244 rows, so 242 of
# them are "duplicates" of an earlier row in this sense.
tips["smoker"].duplicated().sum() # Output: 242

# Display the unique values in the "sex" column
tips["sex"].unique() # Output: ['Female', 'Male']
# Categories (2, str): ['Male', 'Female']

# Count the occurrences of each unique value in the "tip" column
tips["tip"].value_counts()
# Output:
# tip
# 2.0    33
# 3.0    23
# 4.0    12
# Name: count, dtype: int64

# === Plots ===
# Set the style of the plot
sns.set_style("whitegrid") # Styles can be "darkgrid", "whitegrid", "dark", "white", and "ticks"

# Create a bar plot
sns.barplot(x="day", y="total_bill", data=tips) # Renders: bars showing the average total bill for each day of the week
sns.barplot(x="day", y="total_bill", hue="sex", data=tips) # Renders: the same bars, split into two per day by sex

# Create a box plot
sns.boxplot(x="total_bill", data=tips) # Renders: a box plot of the total bill distribution
sns.boxplot(x="day", y="total_bill", data=tips) # Renders: a separate total-bill box plot for each day of the week

# Create a catplot
sns.catplot(x="day", y="total_bill", hue="sex", col="time", data=tips, kind="bar") # Renders: a bar plot with separate columns for lunch and dinner

# Create a displot
sns.displot(x="total_bill", hue="day", data=tips, kde=True) # Renders: a total-bill distribution histogram with a kernel density estimate overlay

# Create a heatmap
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm") # Renders: a colour-coded correlation matrix with the numeric values annotated on each cell

# Create a line plot
sns.lineplot(x="total_bill", y="tip", data=tips) # Renders: a line showing the relationship between total bill and tip
sns.lineplot(x="total_bill", y="tip", hue="day", data=tips) # Renders: the same relationship as a separate line per day of the week

# Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips) # Renders: a scatter plot with total_bill on the x-axis and tip on the y-axis
sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips) # Renders: the same scatter, points colored by day of the week
sns.scatterplot(x="total_bill", y="tip", hue="sex", style="smoker", data=tips) # Renders: the same scatter, points colored by sex and shaped by smoker status
sns.scatterplot(x="total_bill", y="tip", hue="sex", style="smoker", size="size", data=tips) # Renders: the same scatter, with point size also scaled by dining party size

# Customize the plot with labels and title
plt.xlabel("Total Bill") # Set the x-axis label
plt.ylabel("Tip") # Set the y-axis label
plt.title("Total Bill vs Tip") # Set the title of the plot

# Create a histogram with KDE
df = sns.load_dataset("tips") # Load the tips dataset again for histogram plotting
col = "total_bill" # Specify the column to plot
ax = plt.gca() # Get the current axes for plotting

sns.histplot(data=df, x=col, kde=True, ax=ax, bins=30) # Renders: a total-bill histogram (30 bins) with a kernel density estimate overlay, on the current axes

# Display the plot
plt.show() # Renders: the current figure in a window