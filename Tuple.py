# Immutable: Once a tuple is created, you cannot change its values.
# You can create a new tuple by concatenating two tuples or by slicing an existing tuple.

# Creating a Tuple
myTuple = ("apple", "banana", "cherry")

# Accessing Element with Indexing
myTuple[0]  # Output: 'apple'

# Get Number of Occurrences of an Element
myTuple.count("cherry")  # Output: 1 

# Get Index of an Element
myTuple.index("banana")  # Output: 1

# Type of the Tuple
type(myTuple)  # Output: <class 'tuple'>