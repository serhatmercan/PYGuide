# Creating an empty list
my_list = list() # Output: []

# Defining a list
my_list = [10, 20, 30, 40, 50]

# === Types ===
type(my_list) # Output: <class 'list'>

# Accessing elements in a list with indexing
my_list[0] # Output: 10
my_list[-1] # Output: 50

# === Comprehension ===
squared_list = [x**2 for x in my_list] # Output: [100, 400, 900, 1600, 2500]

# Concatenating two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 # Output: [1, 2, 3, 4, 5, 6]

# === Methods ===
# Modifying an element in a list
my_list.append(60) # Output: [10, 20, 30, 40, 50, 60]

# Removing an element from a list
my_list.clear() # Output: []

# Count the number of occurrences of an element in a list
my_list.count(20) # Output: 1

# Finding the index of an element in a list
my_list.index(30) # Output: 2

# Inserting an element at a specific index in a list
my_list.insert(2, 25) # Output: [10, 20, 25, 30, 40, 50, 60]

# Length of a list 
len(my_list) # Output: 7

# Removing the last element from a list and returning it
my_list.pop() # Output: 60
my_list # Output: [10, 20, 25, 30, 40, 50]

# Removing a specific element from a list
my_list.remove(25) # Output: [10, 20, 30, 40, 50]

# Reversing a list
my_list.reverse() # Output: [50, 40, 30, 20, 10]

# Slicing a list [start:stop:step]
my_list[3::] # Output: [40, 50]  
my_list[:3:] # Output: [10, 20, 30]
my_list[::2] # Output: [10, 30, 50]
my_list[3:5] # Output: [40, 50]
my_list[1:4:2] # Output: [20, 40]
my_list[::-1] # Output: [50, 40, 30, 20, 10]

# Sorting a list
my_list.sort() # Output: [10, 20, 30, 40, 50]
