# Define a function that takes a name as input and prints a greeting message.
def greet(name, surname="Mercan"): 
    print(f"Hello, {name} {surname}! Welcome to Python programming.")

greet("John") # Output: Hello, John Mercan! Welcome to Python programming.
greet("Alice", "Smith") # Output: Hello, Alice Smith! Welcome to Python

# Define a function that takes two numbers as input and returns their sum.
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 10)
print(result) # Output: 15

# args and kwargs
def print_arguments(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

print_arguments(1, 2, 3, name="Alice", age=30)
# Output:
# Positional arguments (args): (1, 2, 3)
# Keyword arguments (kwargs): {'name': 'Alice', 'age': 30}

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

# Filter Function
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers)) # The filter function takes a function and an iterable and returns an iterator that produces only the elements of the iterable for which the function returns True. 
print(even_numbers) # Output: [2, 4, 6]

# Global Variable
counter = 0 # This is a global variable that can be accessed and modified from anywhere in the code.

def increment_counter():
    global counter # The global keyword is used to indicate that we want to modify the global variable counter inside the function.
    counter += 1    

increment_counter()
print(counter) # Output: 1

# Lambda Function
# A lambda function is an anonymous function that can take any number of arguments but can only have one expression. It is often used for short, simple functions that are not reused elsewhere in the code.
numbers = [1, 2, 3, 4, 5]   
squared_numbers = list(map(lambda x: x ** 2, numbers)) # The lambda function takes a single argument x and returns its square. The map function applies this lambda function to each element in the numbers list.
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

# Map Function
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers)) # The map function takes a function and an iterable and applies the function to each element of the iterable, returning an iterator with the results.
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

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

zipped_lists = list(zip(list1, list2, list3))  # The zip function takes multiple iterables (in this case, list1, list2, and list3) and returns an iterator that produces tuples containing elements from each iterable at the same index. 
print(zipped_lists) # Output: [(1, 'a', 10), (2, 'b', 20), (3, 'c', 30)]