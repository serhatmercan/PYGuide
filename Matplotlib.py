import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

age_list = [0, 10, 20, 30, 40, 50, 60, 70, 80]
weight_list = [3.5, 50, 65, 80, 85, 80, 82, 84, 80]

# Plotting the data
plt.plot(age_list, weight_list, "r") # Colors: "b" (blue), "g" (green), "r" (red), "c" (cyan), "m" (magenta), "y" (yellow), "k" (black), "w" (white) 
plt.plot(age_list, weight_list, "ro") # "ro" means red circles for the data points
plt.plot(age_list, weight_list, "ro-") # "ro-" means red circles connected by lines for the data points

# Adding labels and title
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs Weight")

# Displaying the plot
plt.show()

# Saving the plot as an image file
plt.savefig("age_weight_plot.png")

# Subplots: Creating multiple plots in a single figure
x = np.linspace(0, 10, 100) # 100 evenly spaced values between 0 and 10
y1 = np.sin(x) # Sine function values
y2 = np.cos(x) # Cosine function values

plt.title("Sine Function")
plt.subplot(2, 1, 1) # 2 rows, 1 column, first subplot
plt.plot(x, y1, "b") # Plotting sine function in blue   

plt.title("Cosine Function")
plt.subplot(2, 1, 2) # 2 rows, 1 column, second subplot
plt.plot(x, y2, "g") # Plotting cosine function in green

plt.show() # Displaying the subplots

# Figure: Creating a figure with specific size and resolution
plt.figure(figsize=(8, 6), dpi=100) # Figure size: 8 inches by 6 inches, Resolution: 100 dots per inch

plt.plot(x, y1, "b") # Plotting sine function in blue
plt.plot(x, y2, "g") # Plotting cosine function in green

plt.title("Sine and Cosine Functions")
plt.xlabel("x")
plt.ylabel("y")

plt.legend(["Sine", "Cosine"]) # Adding a legend to differentiate between the two functions

plt.show() # Displaying the figure

# Figure and Axes: Creating a figure and adding axes to it
fig = plt.figure(dpi=100) # Creating a new figure with specific size and resolution

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # Adding axes to the figure (left, bottom, width, height)

ax.plot(x, y1, "b", label="Sine") # Plotting sine function in blue on the axes
ax.plot(x, y2, "g", label="Cosine") # Plotting cosine function in green on the axes

ax.set_title("Sine and Cosine Functions")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend(loc="upper right") # Adding a legend to the axes and specifying its location (e.g., "upper right", "upper left", "lower right", "lower left", "center")

plt.show() # Displaying the figure with the axes and plots

# Shapes: Creating different shapes using Matplotlib
# Histogram: Plotting the distribution of data
data = np.random.randn(1000) # 1000 random values from a normal distribution

plt.hist(data, bins=30, color="blue", edgecolor="black") # Histogram with 30 bins, blue bars, and black edges

# Scatter plot: Plotting individual data points
x_scatter = np.random.rand(50) # 50 random values between 0 and 1 for x-axis
y_scatter = np.random.rand(50) # 50 random values between 0 and 1 for y-axis

plt.scatter(x_scatter, y_scatter, color="purple", marker="x") # Scatter plot with purple "x" markers

# Scatter plot w/ CSV: Plotting data from a CSV file
data = pd.read_csv('data.csv') # Assuming the CSV file has columns "Height" and "Weight"

plt.scatter("Height", "Weight", data=data) # Scatter plot using "Height" column for x-axis and "Weight" column for y-axis from the CSV data

# Styles: Using different styles for the plots
data1 = np.linspace(0, 10, 20) # 20 evenly spaced values between 0 and 10
data2 = data1 ** 2 # Squaring the data1 values to create data2

fig, ax = plt.subplots() # Creating a figure and a set of subplots (axes)

ax.plot(data1, data2, alpha=0.5) # Plotting data1 vs data2 with a specific transparency level (alpha) between 0 (fully transparent) and 1 (fully opaque)
ax.plot(data1, data2, color="#FF00FF") # Plotting data1 vs data2 with a specific color using hexadecimal color code (e.g., "#FF00FF" for magenta)
ax.plot(data1, data2, linestyle="-.") # Plotting data1 vs data2 with a specific line style (e.g., "-" for solid, "--" for dashed, "-." for dash-dot, ":" for dotted)
ax.plot(data1, data2, linewidth=2) # Plotting data1 vs data2 with a specific line width (e.g., 2 points)
ax.plot(data1, data2, marker="o", markersize=8, markerfacecolor="red", markeredgecolor="black") # Plotting data1 vs data2 with specific markers (e.g., "o" for circles, "s" for squares, "^" for triangles), marker size, marker face color, and marker edge color

plt.show() # Displaying the styled plot