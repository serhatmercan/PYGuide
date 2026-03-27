# Object-Oriented Programming (OOP) in Python
class Person():
    job = "Software Engineer" #class variable

    def __init__(self, name, age, gender): #constructor method
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self): #string representation of the object
        return f"Person(name={self.name}, age={self.age}, gender={self.gender})"
    
    def display(self): 
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

person1 = Person("Alice", 30, "Female")
person1.display() # Output: Name: Alice, Age: 30, Gender: Female

print(person1.job) # Output: Software Engineer
print(str(person1)) # Output: Person(name=Alice, age=30, gender=Female)

# Inheritance
class Employee(Person):
    min_salary = 30000 #class variable

    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender) #call the constructor of the parent class
        self.salary = salary

    def calculate_difference(self):
        return self.salary - self.min_salary

employee1 = Employee("Bob", 40, "Male", 50000)
employee1.display() # Output: Name: Bob, Age: 40, Gender: Male

print(employee1.salary) # Output: 50000
print(employee1.calculate_difference()) # Output: 20000

# Encapsulation
class BankAccount():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance #private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
    
account1 = BankAccount("123456789", 1000)
account1.deposit(500)
account1.withdraw(200)

print(account1.get_balance()) # Output: 1300

# Polymorphism
class Shape():
    def area(self):
        pass #abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(circle.area()) # Output: 78.5
print(rectangle.area()) # Output: 24

# Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
dog = Dog()
cat = Cat()

print(dog.sound()) # Output: Woof
print(cat.sound()) # Output: Meow