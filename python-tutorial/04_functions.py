"""
=============================================================================
FILE: 04_functions.py
TOPIC: Functions - Definitions, Parameters, Return Values, Scope
LEVEL: Beginner
PREREQUISITES: 01_basics_syntax.py, 02_control_flow.py, 03_loops.py
=============================================================================

This file covers functions in Python:
- Function definition and calling
- Parameters (positional, keyword, default, *args, **kwargs)
- Return values (single, multiple, None)
- Variable scope (local, global, nonlocal)
- Lambda functions
- Docstrings and type hints
- Higher-order functions
- Decorators (intro)

Run this file: python 04_functions.py
"""

# =============================================================================
# SECTION 1: BASIC FUNCTION DEFINITION AND CALLING
# =============================================================================

print("=" * 60)
print("SECTION 1: BASIC FUNCTION DEFINITION AND CALLING")
print("=" * 60)

# Simple function with no parameters
def greet():
    """Print a greeting message."""
    print("Hello, World!")

# Calling the function
greet()
greet()  # Can call multiple times

# Function with parameters
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with return value
def add(a, b):
    """Add two numbers and return result."""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple return values (returns tuple)
def get_coordinates():
    """Return x, y coordinates."""
    x = 10
    y = 20
    return x, y

x, y = get_coordinates()  # Tuple unpacking
print(f"Coordinates: ({x}, {y})")


# =============================================================================
# SECTION 2: FUNCTION PARAMETERS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: FUNCTION PARAMETERS")
print("=" * 60)

# 1. Positional parameters
def describe_pet(animal, name):
    """Describe a pet using positional arguments."""
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Rex")        # Positional
describe_pet("cat", "Whiskers")   # Order matters!

# 2. Keyword arguments
describe_pet(animal="hamster", name="Hammy")  # Order doesn't matter
describe_pet(name="Buddy", animal="dog")

# 3. Default parameter values
def greet_with_default(name, greeting="Hello"):
    """Greet with customizable greeting."""
    print(f"{greeting}, {name}!")

greet_with_default("Alice")           # Uses default
greet_with_default("Bob", "Hi")       # Overrides default
greet_with_default("Charlie", greeting="Hey")  # Keyword argument

# 4. *args - variable positional arguments
def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"\nsum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40, 50) = {sum_all(10, 20, 30, 40, 50)}")
print(f"sum_all() = {sum_all()}")

# 5. **kwargs - variable keyword arguments
def print_info(**details):
    """Print keyword arguments."""
    for key, value in details.items():
        print(f"  {key}: {value}")

print("\nprint_info(name='Alice', age=25, city='NYC'):")
print_info(name="Alice", age=25, city="NYC")

# 6. Combining all parameter types
def complex_function(required, default="default", *args, **kwargs):
    """Demonstrate all parameter types."""
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print("\ncomplex_function('req', 'def', 1, 2, 3, a=10, b=20):")
complex_function("req", "def", 1, 2, 3, a=10, b=20)

# 7. Keyword-only arguments (Python 3+)
def keyword_only(*, name, age):
    """Parameters after * must be keyword-only."""
    print(f"Name: {name}, Age: {age}")

keyword_only(name="Alice", age=25)
# keyword_only("Alice", 25)  # TypeError!


# =============================================================================
# SECTION 3: RETURN VALUES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: RETURN VALUES")
print("=" * 60)

# Implicit return (returns None)
def no_return():
    print("This function returns None")

result = no_return()
print(f"Return value: {result}")

# Explicit return None
def explicit_none():
    return None

# Multiple return values (actually returns tuple)
def min_max(numbers):
    """Return min and max of a list."""
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

nums = [5, 2, 9, 1, 7]
min_val, max_val = min_max(nums)
print(f"List: {nums}")
print(f"Min: {min_val}, Max: {max_val}")

# Early return pattern
def find_first_even(numbers):
    """Return first even number or None."""
    for num in numbers:
        if num % 2 == 0:
            return num
    return None  # Explicit, but optional

print(f"\nFirst even in [1, 3, 5, 6, 7]: {find_first_even([1, 3, 5, 6, 7])}")
print(f"First even in [1, 3, 5]: {find_first_even([1, 3, 5])}")


# =============================================================================
# SECTION 4: VARIABLE SCOPE
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: VARIABLE SCOPE")
print("=" * 60)

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Inside function: {global_var}")  # Can read global

scope_demo()
print(f"Outside function: {global_var}")
# print(local_var)  # NameError! Local not accessible

# Modifying global variable
counter = 0

def increment_global():
    global counter  # Declare intent to modify global
    counter += 1
    print(f"Counter: {counter}")

increment_global()
increment_global()
print(f"Global counter after calls: {counter}")

# Nonlocal (for nested functions)
def outer():
    x = "outer"
    
    def inner():
        nonlocal x  # Modify outer function's variable
        x = "inner"
        print(f"Inner: {x}")
    
    print(f"Before inner: {x}")
    inner()
    print(f"After inner: {x}")

outer()

# LEGB Rule: Local -> Enclosing -> Global -> Built-in
print("\nLEGB Rule demonstration:")
x = "global"

def test_legb():
    x = "local"
    print(f"Local x: {x}")

test_legb()
print(f"Global x: {x}")


# =============================================================================
# SECTION 5: LAMBDA FUNCTIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: LAMBDA FUNCTIONS")
print("=" * 60)

# Basic lambda
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
print(f"add(3, 4) = {add(3, 4)}")

# Lambda with default parameter
multiply = lambda a, b=2: a * b
print(f"multiply(5) = {multiply(5)}")
print(f"multiply(5, 3) = {multiply(5, 3)}")

# Lambda in built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter - keep items where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nEvens: {evens}")

# map - apply function to each item
squares = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squares}")

# sorted with key
words = ["apple", "pie", "banana", "kiwi", "cherry"]
by_length = sorted(words, key=lambda x: len(x))
print(f"Sorted by length: {by_length}")

# Lambda with conditional
max_of_two = lambda a, b: a if a > b else b
print(f"Max of 10 and 20: {max_of_two(10, 20)}")


# =============================================================================
# SECTION 6: DOCSTRINGS AND TYPE HINTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: DOCSTRINGS AND TYPE HINTS")
print("=" * 60)

def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
    
    Returns:
        The area (length * width).
    
    Raises:
        ValueError: If length or width is negative.
    
    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

print(f"Area: {calculate_area(5.0, 3.0)}")
print(f"Docstring:\n{calculate_area.__doc__}")
print(f"Annotations: {calculate_area.__annotations__}")

# Type hints for complex types
from typing import List, Dict, Optional, Union

def process_items(items: List[str]) -> Dict[str, int]:
    """Count occurrences of each item."""
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

result = process_items(["apple", "banana", "apple", "cherry"])
print(f"\nItem counts: {result}")

# Optional type hint
def find_user(user_id: int) -> Optional[str]:
    """Find user by ID, return None if not found."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(f"User 1: {find_user(1)}")
print(f"User 3: {find_user(3)}")


# =============================================================================
# SECTION 7: HIGHER-ORDER FUNCTIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: HIGHER-ORDER FUNCTIONS")
print("=" * 60)

# Functions that take functions as arguments
def apply_operation(func, a, b):
    """Apply a binary function to two arguments."""
    return func(a, b)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(f"apply_operation(add, 5, 3) = {apply_operation(add, 5, 3)}")
print(f"apply_operation(multiply, 5, 3) = {apply_operation(multiply, 5, 3)}")

# Functions that return functions
def create_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(f"\ndouble(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# Using lambda to return function
def create_power(exponent):
    return lambda base: base ** exponent

square_func = create_power(2)
cube_func = create_power(3)
print(f"square_func(4) = {square_func(4)}")
print(f"cube_func(4) = {cube_func(4)}")

# Built-in higher-order functions
numbers = [1, 2, 3, 4, 5]

# map
doubled = list(map(lambda x: x * 2, numbers))
print(f"\nmap double: {doubled}")

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter even: {evens}")

# reduce (from functools)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"reduce product: {product}")


# =============================================================================
# SECTION 8: DECORATORS (INTRODUCTION)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: DECORATORS (INTRODUCTION)")
print("=" * 60)

# Simple decorator
def my_decorator(func):
    """A simple decorator that adds behavior before/after function call."""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Say hello to someone."""
    print(f"Hello, {name}!")

print("Calling decorated function:")
say_hello("Alice")

# Decorator with arguments
def repeat(times):
    """Decorator that repeats function call."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Call {i+1}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"  Hi, {name}!")

print("\nCalling @repeat(3) decorated function:")
greet("Bob")

# Practical decorator: timing
import time

def timer(func):
    """Decorator to measure execution time."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done"

print("\nTiming a function:")
slow_function()


# =============================================================================
# SECTION 9: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Calculator with functions
def calculator(a: float, operator: str, b: float) -> float:
    """Simple calculator function."""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",
        '//': lambda x, y: x // y if y != 0 else "Error: Division by zero",
        '%': lambda x, y: x % y,
        '**': lambda x, y: x ** y,
    }
    
    if operator not in operations:
        raise ValueError(f"Unknown operator: {operator}")
    
    return operations[operator](a, b)

print("Calculator:")
for a, op, b in [(10, '+', 5), (10, '-', 5), (10, '*', 5), (10, '/', 5),
                 (10, '//', 3), (10, '%', 3), (2, '**', 10)]:
    try:
        result = calculator(a, op, b)
        print(f"  {a} {op} {b} = {result}")
    except Exception as e:
        print(f"  {a} {op} {b} = Error: {e}")

# Example 2: Data validation functions
def validate_email(email: str) -> bool:
    """Simple email validation."""
    return '@' in email and '.' in email.split('@')[-1]

def validate_age(age: int) -> bool:
    """Validate age is reasonable."""
    return isinstance(age, int) and 0 <= age <= 150

def validate_password(password: str) -> list:
    """Return list of validation errors."""
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters")
    if not any(c.isupper() for c in password):
        errors.append("Uppercase letter")
    if not any(c.islower() for c in password):
        errors.append("Lowercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("Digit")
    return errors

print("\nValidation:")
emails = ["test@example.com", "invalid", "user@domain"]
for email in emails:
    print(f"  {email}: {'Valid' if validate_email(email) else 'Invalid'}")

ages = [25, -5, 200, "thirty"]
for age in ages:
    print(f"  Age {age}: {'Valid' if validate_age(age) else 'Invalid'}")

passwords = ["weak", "StrongPass1", "StrongPass1!"]
for pwd in passwords:
    errors = validate_password(pwd)
    status = "Valid" if not errors else f"Invalid: {', '.join(errors)}"
    print(f"  '{pwd}': {status}")

# Example 3: Function composition
def compose(*functions):
    """Compose multiple functions: compose(f, g)(x) = f(g(x))"""
    def composed(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed

add_one = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

add_one_then_double = compose(double, add_one)
print(f"\nFunction composition:")
print(f"  (x+1)*2 for x=5: {add_one_then_double(5)}")
print(f"  ((x+1)*2)^2 for x=5: {compose(square, double, add_one)(5)}")


# =============================================================================
# SECTION 10: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Factorial Function
------------------------------
Write a function factorial(n) that returns n!
- Handle edge cases (negative, 0)
- Implement both recursive and iterative versions

EXERCISE 2: Fibonacci Sequence
------------------------------
Write a function fibonacci(n) that returns first n Fibonacci numbers
as a list. Use a generator version too.

EXERCISE 3: String Utilities
----------------------------
Create functions:
- count_vowels(s) - count vowels in string
- is_palindrome(s) - check if string reads same backwards
- word_count(s) - count words in string

EXERCISE 4: List Processing
---------------------------
Write functions:
- flatten(nested_list) - flatten one level
- unique(lst) - return list with duplicates removed (preserve order)
- chunk(lst, size) - split list into chunks of given size

EXERCISE 5: Decorator Practice
------------------------------
Create a decorator @log_calls that prints function name, 
arguments, and return value each time function is called.
""")

# Exercise Solutions
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
def factorial_iterative(n: int) -> int:
    """Calculate factorial iteratively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """Calculate factorial recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print("Exercise 1 - Factorial:")
for n in [0, 1, 5, 10]:
    print(f"  {n}! = {factorial_iterative(n)} (iterative), {factorial_recursive(n)} (recursive)")

# Exercise 2
def fibonacci_list(n: int) -> list:
    """Return first n Fibonacci numbers as list."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def fibonacci_generator(n: int):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nExercise 2 - Fibonacci:")
print(f"  List (10): {fibonacci_list(10)}")
print(f"  Generator (10): {list(fibonacci_generator(10))}")

# Exercise 3
def count_vowels(s: str) -> int:
    """Count vowels in string (case-insensitive)."""
    return sum(1 for c in s.lower() if c in 'aeiou')

def is_palindrome(s: str) -> bool:
    """Check if string is palindrome (ignoring case, spaces)."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def word_count(s: str) -> int:
    """Count words in string."""
    return len(s.split())

print("\nExercise 3 - String utilities:")
test_strings = ["Hello World", "A man a plan a canal Panama", "Python", ""]
for s in test_strings:
    print(f"  '{s}': vowels={count_vowels(s)}, palindrome={is_palindrome(s)}, words={word_count(s)}")

# Exercise 4
def flatten(nested_list: list) -> list:
    """Flatten one level of nesting."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

def unique(lst: list) -> list:
    """Remove duplicates preserving order."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def chunk(lst: list, size: int) -> list:
    """Split list into chunks of given size."""
    return [lst[i:i+size] for i in range(0, len(lst), size)]

print("\nExercise 4 - List processing:")
nested = [1, [2, 3], 4, [5, 6, 7]]
print(f"  Flatten {nested}: {flatten(nested)}")

with_dupes = [1, 2, 2, 3, 1, 4, 2]
print(f"  Unique {with_dupes}: {unique(with_dupes)}")

numbers = list(range(1, 11))
print(f"  Chunk {numbers} by 3: {chunk(numbers, 3)}")

# Exercise 5
def log_calls(func):
    """Decorator to log function calls."""
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def multiply(a, b):
    return a * b

print("\nExercise 5 - Decorator @log_calls:")
add(3, 4)
multiply(5, 6)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Define functions with def, call with parentheses
2. Parameters: positional, keyword, default, *args, **kwargs
3. Return values with return (implicit None if omitted)
4. Multiple returns = tuple unpacking
5. Scope: LEGB (Local, Enclosing, Global, Built-in)
6. Use global/nonlocal to modify outer scope variables
7. Lambda: anonymous functions for simple operations
8. Type hints: def func(x: int) -> str: (Python 3.5+)
9. Docstrings: document purpose, args, returns, exceptions
10. Higher-order functions: take/return functions
11. Decorators: @decorator syntax to modify function behavior
12. Pure functions: same input -> same output, no side effects
""")

print("\n✅ File 04 complete! Run 'python 05_data_structures.py' next.")