# Unique Elements & Unordered Collections

# Define a set
my_set = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}

# Add an element to the set
my_set.add(6)

# Create an empty set
myEmptySet = set() 
type(myEmptySet) # Output: <class 'set'>

# Convert a list to a set (removing duplicates)
myList = [1, 2, 2, 3, 4, 4, 1]
my_setFromList = set(myList) # Output: {1, 2, 3, 4}

# Length of the set
len(my_set) # Output: 6

# Intersection of two sets
my_set.intersection(my_set2) # Output: {4, 5, 6}

# Union of two sets
my_set.union(my_set2) # Output: {1, 2, 3, 4, 5, 6, 7, 8}