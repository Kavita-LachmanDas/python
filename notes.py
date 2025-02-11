# 1. Data Types in Python
# Data types define the kind of values a variable can hold in Python.

# 1.1 Numeric Types
# Integer (int): Whole numbers, e.g., 10, -5
# Float (float): Decimal numbers, e.g., 3.14, -0.5
# Complex (complex): Numbers with real and imaginary parts, e.g., 2 + 3j


x = 10      # Integer
y = 3.14    # Float
z = 2 + 3j  # Complex
print(type(x), type(y), type(z))


# 1.2 Sequence Types
# String (str): Text enclosed in quotes, e.g., "Hello"
# List (list): Ordered, mutable collection, e.g., [1, 2, 3]
# Tuple (tuple): Ordered, immutable collection, e.g., (1, 2, 3)




text = "Python"
numbers = [1, 2, 3]
coordinates = (10, 20)

print(type(text), type(numbers), type(coordinates))


# 1.3 Set & Dictionary Types
# Set (set): Unordered, unique values, e.g., {1, 2, 3}
# Dictionary (dict): Key-value pairs, e.g., {"name": "Alice", "age": 25}



unique_nums = {1, 2, 3, 3}  # Set
person = {"name": "Alice", "age": 25}  # Dictionary

print(type(unique_nums), type(person))


# 1.4. Boolean Type
# Boolean (bool): Represents True or False.

is_active = True
is_logged_in = False
print(type(is_active))



# 2. Operators in Python
# Operators are symbols that perform operations on values and variables.

# 2.1 Arithmetic Operators
# Used for mathematical operations.

a = 10
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)



# 2.2 Comparison Operators
# Used for comparison, returns True or False.


x = 5
y = 3
print(x == y, x != y, x > y, x < y, x >= y, x <= y)


# 2.3 Logical Operators
# Used for logical operations.


a = True
b = False
print(a and b, a or b, not a)


# 2.4 Assignment Operators
# Used to assign values to variables.


x = 10
x += 5  # Same as x = x + 5
print(x)



# 2.6 Identity & Membership Operators
# Identity Operators
# is: Checks if two variables refer to the same object.
# is not: Checks if two variables do not refer to the same object.


x = [1, 2, 3]
y = [1, 2, 3]
print(x is y, x is not y)  # False, because they are different objects


# Membership Operators
# in: Checks if a value is present in a sequence.
# not in: Checks if a value is not present in a sequence.

numbers = [1, 2, 3, 4, 5]
print(3 in numbers, 10 not in numbers)
