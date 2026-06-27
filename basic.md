# Python Basics

## Introduction to Python

Python is a high-level, interpreted programming language known for its readability and simplicity. Created by Guido van Rossum and first released in 1991.

### Key Characteristics
- **Interpreted**: Code executes line by line
- **Dynamically typed**: No need to declare variable types
- **Object-oriented**: Everything is an object
- **Cross-platform**: Runs on Windows, macOS, Linux
- **Large standard library**: "Batteries included"

### Installation & Setup
```bash
# Check Python version
python --version
python3 --version

# Run Python script
python script.py

# Interactive mode
python
```

---

## Basic Syntax

### Variables and Data Types
```python
# Variables (no declaration needed)
name = "Alice"
age = 25
height = 5.6
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 10

# Type checking
type(name)    # <class 'str'>
type(age)     # <class 'int'>
type(height)  # <class 'float'>
type(is_student)  # <class 'bool'>
```

### Basic Data Types
| Type | Description | Example |
|------|-------------|---------|
| `int` | Integers | `42`, `-7`, `0` |
| `float` | Decimal numbers | `3.14`, `-0.5` |
| `str` | Text/strings | `"hello"`, `'world'` |
| `bool` | Boolean | `True`, `False` |
| `NoneType` | Null value | `None` |

### String Operations
```python
s = "Hello World"

# Indexing and slicing
s[0]        # 'H'
s[-1]       # 'd'
s[0:5]      # 'Hello'
s[::2]      # 'HloWrd' (every 2nd char)

# String methods
s.lower()           # 'hello world'
s.upper()           # 'HELLO WORLD'
s.strip()           # Remove whitespace
s.split()           # ['Hello', 'World']
s.replace('o', 'a') # 'Hella Warld'
len(s)              # 11

# Formatting
name = "Alice"
age = 25
f"Name: {name}, Age: {age}"     # f-string (Python 3.6+)
"Name: {}, Age: {}".format(name, age)
"Name: %s, Age: %d" % (name, age)
```

---

## Control Flow

### Conditionals
```python
# if-elif-else
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# Boolean operators
if age > 0 and age < 100:
    print("Valid age")
if age < 0 or age > 150:
    print("Invalid age")
```

### Loops
```python
# For loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Iterating over collections
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)

# Else clause (executes if loop completes normally)
for i in range(3):
    print(i)
else:
    print("Loop finished")
```

---

## Data Structures

### Lists (Mutable, Ordered)
```python
# Creation
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# Access
numbers[0]      # 1
numbers[-1]     # 5
numbers[1:4]    # [2, 3, 4]

# Modification
numbers.append(6)        # [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6]
numbers.extend([7, 8])   # [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers.remove(3)        # Remove first occurrence
popped = numbers.pop()   # Remove and return last
popped = numbers.pop(0)  # Remove and return at index
numbers[0] = 100         # Modify element

# Other operations
len(numbers)        # Length
3 in numbers        # Membership test
numbers.index(2)    # Index of first occurrence
numbers.count(2)    # Count occurrences
numbers.sort()      # Sort in place
numbers.reverse()   # Reverse in place
sorted(numbers)     # Return new sorted list

# List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(3)]
```

### Tuples (Immutable, Ordered)
```python
# Creation
coordinates = (10, 20)
point = (3, 4, 5)
single = (42,)      # Note the comma
empty = ()

# Access (same as lists)
coordinates[0]  # 10
coordinates[1]  # 20

# Unpacking
x, y = coordinates
a, b, c = point

# Tuples are immutable
# coordinates[0] = 5  # TypeError!

# Use cases: multiple return values, dictionary keys, fixed collections
```

### Sets (Mutable, Unordered, Unique Elements)
```python
# Creation
fruits = {"apple", "banana", "cherry"}
empty = set()       # {} creates empty dict!

# Operations
fruits.add("orange")
fruits.remove("banana")    # Raises KeyError if not found
fruits.discard("banana")   # No error if not found
fruits.pop()               # Remove arbitrary element
fruits.clear()

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # Union: {1, 2, 3, 4, 5, 6}
a & b   # Intersection: {3, 4}
a - b   # Difference: {1, 2}
a ^ b   # Symmetric difference: {1, 2, 5, 6}

# Membership
3 in a      # True
7 not in a  # True
```

### Dictionaries (Mutable, Key-Value Pairs)
```python
# Creation
person = {"name": "Alice", "age": 25, "city": "NYC"}
empty = {}

# Access
person["name"]        # "Alice" (KeyError if missing)
person.get("name")    # "Alice" (None if missing)
person.get("job", "Unknown")  # Default value

# Modification
person["email"] = "alice@example.com"
person["age"] = 26
person.update({"job": "Engineer", "city": "LA"})

# Deletion
del person["city"]
email = person.pop("email")
last = person.popitem()  # Remove last inserted (Python 3.7+)

# Iteration
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

for value in person.values():
    print(value)

# Dictionary comprehensions
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Other
len(person)
"name" in person
list(person.keys())
list(person.values())
```

---

## Functions

### Basic Functions
```python
# Definition
def greet(name):
    return f"Hello, {name}!"

# Calling
greet("Alice")  # "Hello, Alice!"

# Parameters and arguments
def add(a, b):
    return a + b

add(2, 3)           # Positional
add(a=2, b=3)       # Keyword
add(b=3, a=2)       # Keyword (order doesn't matter)

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")           # "Hello, Alice!"
greet("Alice", "Hi")     # "Hi, Alice!"
greet(name="Alice")      # "Hello, Alice!"

# *args and **kwargs
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Combined
def func(a, b, *args, **kwargs):
    pass
```

### Return Values
```python
def divide(a, b):
    if b == 0:
        return None
    return a / b

# Multiple return values (tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 3, 9, 2])
```

### Lambda Functions
```python
# Anonymous functions
square = lambda x: x**2
square(5)  # 25

# With map, filter, sorted
numbers = [1, 2, 3, 4, 5]
list(map(lambda x: x*2, numbers))     # [2, 4, 6, 8, 10]
list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
sorted([3, 1, 4, 1, 5], key=lambda x: -x)    # [5, 4, 3, 1, 1]
```

### Scope
```python
x = 10  # Global

def func():
    y = 5  # Local
    print(x)  # Can read global
    # x = 20  # This creates local x!
    
    global x
    x = 20   # Modifies global

def outer():
    z = 10
    def inner():
        nonlocal z
        z = 20  # Modifies outer's z
    inner()
    print(z)  # 20
```

---

## Modules and Packages

### Importing
```python
# Standard library
import math
import random
import datetime
import os
import sys
import json

math.sqrt(16)        # 4.0
random.randint(1, 6) # Random 1-6
datetime.date.today()

# Specific imports
from math import sqrt, pi
sqrt(16)  # 4.0

# Aliases
import numpy as np
import pandas as pd

# All (not recommended)
from math import *
```

### Creating Modules
```python
# my_module.py
def hello():
    return "Hello from module!"

PI = 3.14159

# Usage
import my_module
my_module.hello()
my_module.PI

from my_module import hello, PI
```

### Virtual Environments
```bash
# Create
python -m venv venv

# Activate
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

# Deactivate
deactivate

# Install packages
pip install requests
pip install -r requirements.txt

# Freeze dependencies
pip freeze > requirements.txt
```

---

## File I/O

### Reading Files
```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read lines
with open("file.txt", "r") as f:
    lines = f.readlines()

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Different modes
# 'r'  - read (default)
# 'w'  - write (truncates)
# 'a'  - append
# 'x'  - exclusive creation
# 'b'  - binary mode
# 't'  - text mode (default)
```

### Writing Files
```python
# Write string
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Second line")

# Write multiple lines
with open("output.txt", "w") as f:
    f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

# Using print
with open("output.txt", "w") as f:
    print("Hello", file=f)
    print("World", file=f)
```

### JSON
```python
import json

data = {"name": "Alice", "age": 25, "skills": ["Python", "SQL"]}

# Write
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read
with open("data.json", "r") as f:
    loaded = json.load(f)

# String conversion
json_str = json.dumps(data)
parsed = json.loads(json_str)
```

---

## Exception Handling

### Try-Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No error occurred")
finally:
    print("Cleanup always runs")
```

### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age too high")
    return age

# Custom exceptions
class CustomError(Exception):
    pass

raise CustomError("Something went wrong")
```

---

## Classes and Objects (OOP Basics)

### Basic Class
```python
class Person:
    # Class attribute
    species = "Human"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age
    
    # Instance method
    def greet(self):
        return f"Hi, I'm {self.name}"
    
    # Property
    @property
    def is_adult(self):
        return self.age >= 18
    
    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import date
        return cls(name, date.today().year - birth_year)
    
    # Static method
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 150
```

### Inheritance
```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self):
        return f"{super().greet()}, student #{self.student_id}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

### Special Methods (Dunder Methods)
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
```

---

## Type Hints (Python 3.5+)

```python
from typing import List, Dict, Tuple, Optional, Union, Any

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}"

def process(items: List[int]) -> Dict[str, int]:
    return {"count": len(items), "sum": sum(items)}

# Variables
age: int = 25
name: str = "Alice"
scores: List[float] = [95.5, 87.0, 92.3]

# Optional (can be None)
def find_user(id: int) -> Optional[str]:
    pass

# Union (multiple types)
def process_id(id: Union[int, str]) -> str:
    return str(id)

# Type aliases
UserId = int
UserDict = Dict[str, Any]
```

---

## Common Standard Library Modules

| Module | Purpose |
|--------|---------|
| `os` | Operating system interface |
| `sys` | System-specific parameters |
| `pathlib` | Object-oriented filesystem paths |
| `datetime` | Date and time manipulation |
| `random` | Random number generation |
| `math` | Mathematical functions |
| `statistics` | Statistical calculations |
| `collections` | Specialized container datatypes |
| `itertools` | Iterator utilities |
| `functools` | Higher-order functions |
| `json` | JSON encoding/decoding |
| `csv` | CSV file reading/writing |
| `re` | Regular expressions |
| `argparse` | Command-line argument parsing |
| `logging` | Logging framework |
| `unittest` | Unit testing framework |

---

## Useful Tips and Best Practices

### List/Dict/Set Comprehensions
```python
# List
[x*2 for x in range(5)]

# Dict
{x: x*2 for x in range(5)}

# Set
{x*2 for x in range(5)}

# Generator (memory efficient)
(x*2 for x in range(5))
```

### Enumerate and Zip
```python
# Enumerate
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")

# Zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### Context Managers
```python
# Custom context manager
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")

with timer():
    # do something
    pass
```

### Common Gotchas
```python
# Mutable default argument (AVOID!)
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

# Correct way
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# Shallow vs deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()        # or list(original)
deep = copy.deepcopy(original)
```

---

## Quick Reference Cheatsheet

| Operation | Syntax |
|-----------|--------|
| Comment | `# comment` |
| Multi-line string | `"""text"""` or `'''text'''` |
| Type check | `type(x)` or `isinstance(x, int)` |
| Length | `len(obj)` |
| Range | `range(start, stop, step)` |
| Help | `help(obj)` or `obj?` in REPL |
| Dir | `dir(obj)` |
| Main guard | `if __name__ == "__main__":` |

---

## Next Steps
- Practice with exercises
- Explore standard library modules
- Learn about testing (`unittest`, `pytest`)
- Study advanced topics: decorators, generators, async/await
- Build projects!