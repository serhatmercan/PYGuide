# Unique Elements & Unordered Collections

# Define a set
mySet = {1, 2, 3, 4, 5}
mySet2 = {4, 5, 6, 7, 8}

# Add an element to the set
mySet.add(6)

# Create an empty set
myEmptySet = set() 
type(myEmptySet) # Output: <class 'set'>

# Convert a list to a set (removing duplicates)
myList = [1, 2, 2, 3, 4, 4, 1]
mySetFromList = set(myList) # Output: {1, 2, 3, 4}

# Length of the set
len(mySet) # Output: 6

# Intersection of two sets
mySet.intersection(mySet2) # Output: {4, 5, 6}

# Union of two sets
mySet.union(mySet2) # Output: {1, 2, 3, 4, 5, 6, 7, 8}