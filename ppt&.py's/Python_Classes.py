# Python Classes - Beginner Level
# --------------------------------
# A simple introduction to Python Classes and Objects

# 1. Defining a Class
class Student:
    # Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display information
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")


# 2. Creating Objects (Instances)
student1 = Student("Aisha", 21)
student2 = Student("Rahul", 22)

# Accessing attributes and methods
student1.display_info()
student2.display_info()


# 3. Another Example: Car Class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} car in {self.color} color is starting...")

# Creating an object
car1 = Car("Toyota", "Red")
car1.start()


# 4. Simple Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Using the Calculator
calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))


# 5. Summary
"""
Classes group data and behavior together.
Objects are instances of classes.
The __init__ method initializes object data.
Methods perform actions for an object.
"""
