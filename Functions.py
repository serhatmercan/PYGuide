# Enumerate Function
my_list = [10, 20, 30, 40, 50]
# The enumerate function takes an iterable (in this case, my_list) and returns an iterator that produces pairs of index and value for each element in the iterable. 
# The variable i will hold the index of the current element, and value will hold the corresponding value from the list.
for i, value in enumerate(my_list): 
    print(f"Index: {i}, Value: {value}") 
# Output: 
# Index: 0, Value: 10
# Index: 1, Value: 20   
# Index: 2, Value: 30
# Index: 3, Value: 40
# Index: 4, Value: 50

# Random Function
from random import randint # The randint function generates a random integer between the specified range (inclusive). In this case, it generates a random integer between 1 and 100.
random_number = randint(1, 100) # Output: A random integer between 1 and 100 (e.g., 42)

from random import shuffle # The shuffle function takes a list as input and randomly shuffles its elements in place. It modifies the original list.
my_list = [1, 2, 3, 4, 5]
shuffle(my_list) # Output: The elements of my_list will be randomly shuffled (e.g., [3, 1, 5, 2, 4])

# Range Function
range(5) # This creates a range object that represents the sequence of numbers from 0 to 4. It can be used in loops or converted to a list for further manipulation.
list(range(5)) # Output: [0, 1, 2, 3, 4]

range(5,15) # This creates a range object that represents the sequence of numbers from 5 to 14.
list(range(5,15)) # Output: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

range(5,15,2) # This creates a range object that represents the sequence of numbers from 5 to 14, with a step of 2.
list(range(5,15,2)) # Output: [5, 7, 9, 11, 13]

# Zip Function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]

# The zip function takes multiple iterables (in this case, list1, list2, and list3) and returns an iterator that produces tuples containing elements from each iterable at the same index.
zipped_lists = list(zip(list1, list2, list3)) 

print(zipped_lists) # Output: [(1, 'a', 10), (2, 'b', 20), (3, 'c', 30)]
