import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size for the plots
plt.figure(figsize=(10, 6)) # This sets the size of the figure to 10 inches wide and 6 inches tall

# Load the tips dataset from Seaborn
tips = sns.load_dataset("tips") # The tips dataset contains information about restaurant bills and tips, including the total bill amount

# Display the column names of the dataset
tips.columns  # Output: Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='object')

# Show the correlation between numeric columns in the dataset 
tips.corr(numeric_only=True) 
# Output:   total_bill       tip      size
# total_bill  1.000000  0.675734  0.598315
# tip         0.675734  1.000000  0.489299
# size        0.598315  0.489299  1.000000  

# Display the unique values in the "sex" column
tips["sex"].unique() # Output: array(['Male', 'Female'], dtype=object)

# Set the style of the plot
sns.set_style("whitegrid") # Styles can be "darkgrid", "whitegrid", "dark", "white", and "ticks"

# Create a bar plot
sns.barplot(x="day", y="total_bill", data=tips) # To show the average total bill for each day of the week
sns.barplot(x="day", y="total_bill", hue="sex", data=tips) # Add hue to differentiate bars by sex 

# Create a box plot
sns.boxplot(x="total_bill", data=tips) # To show the distribution of total bills
sns.boxplot(x="day", y="total_bill", data=tips) # To show the distribution of total bills for each day of the week

# Create a catplot
sns.catplot(x="day", y="total_bill", hue="sex", col="time", data=tips, kind="bar") # Create a bar plot with separate columns for lunch and dinner

# Create a displot
sns.displot(x="total_bill", hue="day", data=tips, kde=True) # To show the distribution of total bills with a kernel density estimate

# Create a heatmap
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm") # To visualize the correlation between numeric columns in the dataset

# Create a line plot
sns.lineplot(x="total_bill", y="tip", data=tips) # To show the relationship between total bill and tip
sns.lineplot(x="total_bill", y="tip", hue="day", data=tips) # Add hue to differentiate lines by day of the week

# Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips) # With total_bill on the x-axis and tip on the y-axis
sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips) # Add hue to differentiate points by day of the week
sns.scatterplot(x="total_bill", y="tip", hue="sex", style="smoker", data=tips) # Add style to differentiate points by smoker status
sns.scatterplot(x="total_bill", y="tip", hue="sex", style="smoker", size="size", data=tips) # Add size to differentiate points by the size of the dining party

# Customize the plot with labels and title
plt.xlabel("Total Bill") # Set the x-axis label
plt.ylabel("Tip") # Set the y-axis label
plt.title("Total Bill vs Tip") # Set the title of the plot

# Display the plot
plt.show()