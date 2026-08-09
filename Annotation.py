# Variable Annotations
name : str = "Serhat"
age : int = 30
height : float = 1.80
is_student : bool = False

# Function Annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# The `int | str` union syntax (PEP 604) requires Python 3.10+;
# on older versions use `Union[int, str]` from the typing module instead.
def process_value(value: int | str) -> str:
    if isinstance(value, int):
        return f"Processing integer: {value}"
    elif isinstance(value, str):
        return f"Processing string: {value}"
    else:
        return "Unsupported type"
    
# List Annotations
from typing import List # Since Python 3.9, the built-in `list[int]` works directly and this import isn't needed

numbers: List[int] = [1, 2, 3, 4, 5]
numbers: list[int] = [1, 2, 3, 4, 5] # Modern equivalent (Python 3.9+)

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

sum_result = sum_numbers(numbers)

print(f"The sum of the numbers is: {sum_result}") # Output: The sum of the numbers is: 15

# Class Annotations
class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def introduce(self) -> str:
        return f"My name is {self.name} and I am {self.age} years old."

person = Person("Alice", 25)

print(greet(person.name)) # Output: Hello, Alice!
print(person.introduce()) # Output: My name is Alice and I am 25 years old.