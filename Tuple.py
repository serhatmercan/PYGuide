# Immutable: Once a tuple is created, you cannot change its values.
# You can create a new tuple by concatenating two tuples or by slicing an existing tuple.

# Creating a Tuple
my_tuple = ("apple", "banana", "cherry")

# Accessing Element with Indexing
my_tuple[0]  # Output: 'apple'

# Get Number of Occurrences of an Element
my_tuple.count("cherry")  # Output: 1 

# Get Index of an Element
my_tuple.index("banana")  # Output: 1

# Type of the Tuple
type(my_tuple)  # Output: <class 'tuple'>