# Arithmetic Methods

a = 3.3
b = 2
nums = [3, 1, 4, 22, 6, -5]

# Addition
print(a + b)

# subtraction
print(a - b)

# multiplication
print(a * b)

# division
print(a / b)

# integer division
print(a // b)

# exponent
print(a ** b)

# modulus
print(a % b)

# absolute value
print(abs(b-a))

# summation
print(sum(nums))

# maximum value
print(max(nums))

# minimum value
print(min(nums))


# String Operations

name = "Joe Chip"

# slicing
print(name[0:3])

# uppercase
print(name.upper())

# lowercase
print(name.lower())

# capitalize
print(name.capitalize())

# title
print(name.title())

# length
print(len(name))

# split
print(name.split())
print(name.split('o'))


# Print Formatting

print(f'My name is: {name}')

x = 77/13
print(f'The value of x is: {x:5.2f}')  # rounding to 2 decimal places
# {variable name:width.precision}


# List Methods:

lst = ['one', 2, True]

# append
lst.append('four')

# remove
lst.remove('one')

# pop
lst.pop()

# insert
lst.insert(1, 'two')

# concatenate
lst2 = ['five', False]
lst += lst2

# slicing
print(lst[::-1]) # reverse order

# count 
print(lst.count(2))

# index
print(lst.index(True))

# sort
#lst.sort() sorting in place (can't mix value types)

# Tuples and Sets are similar to lists 
# Tuples can't be modified, sets can't have duplicates & is fast to access


## Dictionary Methods:

dct = {'name': 'Joe', 'age': 20, 'location': 'North American Federation'}

print(dct['name']) # accessing value by key

dct['age'] = 21 # modifying value

print(dct.keys()) # returns keys

print(dct.values()) # returns values

print(dct.items()) # returns key-value pairs


## Loops -> pretty straightforward

# for loop
for i in range(10):
    print(i)

# while loop
i = 0
while i < 10:
    print(i)
    i += 1


## Functions

def add(a, b):
    return a + b

# args and kwargs
def func(*args, **kwargs):
    print(args) # can take an unspecified amount of arguments
    print(kwargs) # can take can unspecified amount of key,value arguments

# lambda functions
double = lambda x: x * 2
print(double(5))

# map
nums = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x * 2, nums))

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# list comprehension
squares = [x ** 2 for x in nums]

# generators
def gen():
    for i in range(10):
        yield i

print(list(gen()))

# decorators
def decorator(func):
    def wrapper(*args, **kwargs):
        print('Before function call')
        func(*args, **kwargs)
        print('After function call')
    return wrapper

@decorator
def myFunction(x, y):
    print (x + y)

myFunction(a,b)


## Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

    def __str__(self): # overriding str method
        return f"Name: {self.name}, Age: {self.age}"
    

# Inheritance

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying for grade {self.grade}.")


## Exceptions

try:
    raise("UHOH") # manually raising error  
except:
    print("An error occurred")
finally:
    print("This will always run")


## Useful Libraries

import math
import random
from collections import Counter
import os
import datetime
import re

# math
print(math.pi)

# random
print(random.randint(1, 10)) # this includes both ends

# counter
lst = [1, 2, 3, 4, 1, 2, 3, 4, 5]
print(Counter(lst))

# os
print(os.getcwd())

# datetime
print(datetime.datetime.now())

# re
# this is just a mess ;)
# just to https://regex101.com/
