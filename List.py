# Creating an empty list
myList = list() # Output: []

# Defining a list
myList = [10, 20, 30, 40, 50]

# Types
type(myList) # Output: <class 'list'>

# Accessing elements in a list with indexing
myList[0] # Output: 10
myList[-1] # Output: 50

# Concatenating two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 # Output: [1, 2, 3, 4, 5, 6]

# Methods:
# Modifying an element in a list
myList.append(60) # Output: [10, 20, 30, 40, 50, 60]

# Removing an element from a list
myList.clear() # Output: []

# Count the number of occurrences of an element in a list
myList.count(20) # Output: 1

# Finding the index of an element in a list
myList.index(30) # Output: 2

# Inserting an element at a specific index in a list
myList.insert(2, 25) # Output: [10, 20, 25, 30, 40, 50, 60]

# Length of a list 
len(myList) # Output: 7

# Removing the last element from a list and returning it
myList.pop() # Output: 60
myList # Output: [10, 20, 25, 30, 40, 50]

# Removing a specific element from a list
myList.remove(25) # Output: [10, 20, 30, 40, 50]

# Reversing a list
myList.reverse() # Output: [50, 40, 30, 20, 10]

# Slicing a list [start:stop:step]
myList[3::] # Output: [40, 50]  
myList[:3:] # Output: [10, 20, 30]
myList[::2] # Output: [10, 30, 50]
myList[3:5] # Output: [40, 50]
myList[1:4:2] # Output: [20, 40]
myList[::-1] # Output: [50, 40, 30, 20, 10]

# Sorting a list
myList.sort() # Output: [10, 20, 30, 40, 50]
