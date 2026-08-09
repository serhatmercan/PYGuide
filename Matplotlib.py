import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

age_list = [0, 10, 20, 30, 40, 50, 60, 70, 80]
weight_list = [3.5, 50, 65, 80, 85, 80, 82, 84, 80]

# === Basic Plotting ===
# Colors: "b" (blue), "g" (green), "r" (red), "c" (cyan), "m" (magenta), "y" (yellow), "k" (black), "w" (white)
plt.plot(age_list, weight_list, "r") # Renders: a red line connecting the (age, weight) points
plt.plot(age_list, weight_list, "ro") # Renders: red circles at each (age, weight) point, unconnected
plt.plot(age_list, weight_list, "ro-") # Renders: red circles connected by a line

# Adding labels and title
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs Weight")

# Adding a grid to the plot for better visibility of data points
plt.grid(True)

# Displaying the plot
plt.show() # Renders: the current figure in a window

# Saving the plot as an image file
plt.savefig("age_weight_plot.png") # Renders: writes the current figure to age_weight_plot.png

# === Subplots ===
# Creating multiple plots in a single figure
x = np.linspace(0, 10, 100) # 100 evenly spaced values between 0 and 10
y1 = np.sin(x) # Sine function values
y2 = np.cos(x) # Cosine function values

# title() must come after subplot() - calling it first sets the title on
# whatever axes are current at that moment (an empty default axes the first
# time, then the previous subplot the second time), not the subplot you're
# about to plot into
plt.subplot(2, 1, 1) # 2 rows, 1 column, first subplot
plt.title("Sine Function")
plt.plot(x, y1, "b") # Renders: a blue sine curve in the top subplot

plt.subplot(2, 1, 2) # 2 rows, 1 column, second subplot
plt.title("Cosine Function")
plt.plot(x, y2, "g") # Renders: a green cosine curve in the bottom subplot

plt.show() # Renders: the figure with both subplots stacked vertically

# === Figure ===
# Creating a figure with specific size and resolution
plt.figure(figsize=(8, 6), dpi=100) # Figure size: 8 inches by 6 inches, Resolution: 100 dots per inch

plt.plot(x, y1, "b") # Renders: a blue sine curve
plt.plot(x, y2, "g") # Renders: a green cosine curve, on the same axes as the sine curve

plt.title("Sine and Cosine Functions")
plt.xlabel("x")
plt.ylabel("y")

plt.legend(["Sine", "Cosine"]) # Renders: a legend box labelling the two curves

plt.show() # Renders: the figure with both curves and the legend

# === Figure and Axes ===
# Creating a figure and adding axes to it
fig = plt.figure(dpi=100) # Creating a new figure with specific size and resolution

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # Adding axes to the figure (left, bottom, width, height)

ax.plot(x, y1, "b", label="Sine") # Renders: a blue sine curve on the manually placed axes
ax.plot(x, y2, "g", label="Cosine") # Renders: a green cosine curve on the same axes

ax.set_title("Sine and Cosine Functions")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend(loc="upper right") # Renders: a legend box in the upper-right corner (e.g. "upper right", "upper left", "lower right", "lower left", "center")

plt.show() # Renders: the figure with the manually placed axes, curves, and legend

# === Shapes ===
# Histogram: Plotting the distribution of data
data = np.random.randn(1000) # 1000 random values from a normal distribution

plt.hist(data, bins=30, color="blue", edgecolor="black") # Renders: a histogram with 30 blue bars outlined in black

# Scatter plot: Plotting individual data points
x_scatter = np.random.rand(50) # 50 random values between 0 and 1 for x-axis
y_scatter = np.random.rand(50) # 50 random values between 0 and 1 for y-axis

plt.scatter(x_scatter, y_scatter, color="purple", marker="x") # Renders: purple "x" markers at each (x, y) point

# Scatter plot w/ DataFrame: Plotting data loaded from a DataFrame
tips = sns.load_dataset("tips") # Originally read a local data.csv with "Height"/"Weight" columns; swapped to seaborn's tips dataset (approved 2026-08-09) so this file is self-contained

plt.scatter("total_bill", "tip", data=tips) # Renders: a scatter plot of total bill vs tip amount

# === Styles ===
# Using different styles for the plots
data1 = np.linspace(0, 10, 20) # 20 evenly spaced values between 0 and 10
data2 = data1 ** 2 # Squaring the data1 values to create data2

fig, ax = plt.subplots() # Creating a figure and a set of subplots (axes)

ax.plot(data1, data2, alpha=0.5) # Renders: the curve at 50% opacity (alpha between 0 fully transparent and 1 fully opaque)
ax.plot(data1, data2, color="#FF00FF") # Renders: the curve in magenta, set via hex color code
ax.plot(data1, data2, linestyle="-.") # Renders: the curve as a dash-dot line (e.g. "-" solid, "--" dashed, "-." dash-dot, ":" dotted)
ax.plot(data1, data2, linewidth=2) # Renders: the curve drawn 2 points wide
ax.plot(data1, data2, marker="o", markersize=8, markerfacecolor="red", markeredgecolor="black") # Renders: the curve with circular markers (red fill, black edge, size 8) at each point

plt.show() # Renders: the styled plot with all five line variants overlaid

plt.tight_layout() # Adjusts the layout of the current figure to prevent labels, titles, and legends from overlapping
