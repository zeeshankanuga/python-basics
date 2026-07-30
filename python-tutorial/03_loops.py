"""
=============================================================================
FILE: 03_loops.py
TOPIC: Loops - For Loops, While Loops, Loop Control
LEVEL: Beginner
PREREQUISITES: 01_basics_syntax.py, 02_control_flow.py
=============================================================================

This file covers looping constructs in Python:
- For loops (iterating over sequences)
- While loops (condition-based iteration)
- Loop control statements (break, continue, else)
- Range function
- Enumerate, zip, reversed
- Nested loops
- List comprehensions

Run this file: python 03_loops.py
"""

# =============================================================================
# SECTION 1: FOR LOOPS
# =============================================================================

print("=" * 60)
print("SECTION 1: FOR LOOPS")
print("=" * 60)

# Iterating over a list
fruits = ["apple", "banana", "cherry", "date"]
print("Iterating over a list:")
for fruit in fruits:
    print(f"  {fruit}")

# Iterating over a string
print("\nIterating over a string:")
for char in "Python":
    print(f"  {char}")

# Iterating over a tuple
print("\nIterating over a tuple:")
coordinates = (10, 20, 30)
for coord in coordinates:
    print(f"  {coord}")

# Iterating over a dictionary
print("\nIterating over a dictionary:")
student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student:
    print(f"  Key: {key}, Value: {student[key]}")

# Better: items() for key-value pairs
print("\nUsing items():")
for key, value in student.items():
    print(f"  {key}: {value}")

# Iterating over a set
print("\nIterating over a set:")
unique_numbers = {1, 2, 3, 2, 1}  # Duplicates removed
for num in unique_numbers:
    print(f"  {num}")


# =============================================================================
# SECTION 2: RANGE FUNCTION
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: RANGE FUNCTION")
print("=" * 60)

# range(stop) - 0 to stop-1
print("range(5):")
for i in range(5):
    print(f"  {i}")

# range(start, stop) - start to stop-1
print("\nrange(2, 6):")
for i in range(2, 6):
    print(f"  {i}")

# range(start, stop, step)
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  {i}")

# Negative step (counting down)
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(f"  {i}")

# Practical: range with len() for index access
colors = ["red", "green", "blue"]
print("\nUsing range(len()):")
for i in range(len(colors)):
    print(f"  Index {i}: {colors[i]}")


# =============================================================================
# SECTION 3: USEFUL ITERATION TOOLS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: USEFUL ITERATION TOOLS")
print("=" * 60)

# enumerate() - get index and value
fruits = ["apple", "banana", "cherry"]
print("enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# enumerate with start parameter
print("\nenumerate(start=1):")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# zip() - iterate over multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

print("\nzip() - multiple sequences:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, {city}")

# zip with different lengths (stops at shortest)
print("\nzip() with different lengths:")
for a, b in zip([1, 2, 3], ['x', 'y']):
    print(f"  {a}, {b}")

# reversed() - iterate in reverse
print("\nreversed():")
for item in reversed([1, 2, 3, 4, 5]):
    print(f"  {item}")

# sorted() - iterate in sorted order
print("\nsorted():")
for item in sorted([3, 1, 4, 1, 5, 9, 2]):
    print(f"  {item}")


# =============================================================================
# SECTION 4: WHILE LOOPS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: WHILE LOOPS")
print("=" * 60)

# Basic while loop
count = 0
print("Basic while loop:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# While with else (executes when condition becomes False, not when break)
print("\nWhile with else:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1
else:
    print("  Loop completed normally (no break)")

# While True with break (common pattern for input validation)
print("\nWhile True with break (simulated):")
attempts = 0
while True:
    attempts += 1
    if attempts >= 3:
        print("  Max attempts reached")
        break
    print(f"  Attempt {attempts}")

# Practical example: countdown
import time
print("\nCountdown (simulated):")
countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  Liftoff!")


# =============================================================================
# SECTION 5: LOOP CONTROL STATEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: LOOP CONTROL STATEMENTS")
print("=" * 60)

# break - exit loop immediately
print("break statement:")
for i in range(10):
    if i == 5:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}")

# continue - skip to next iteration
print("\ncontinue statement:")
for i in range(5):
    if i == 2:
        print(f"  Skipping {i}")
        continue
    print(f"  {i}")

# else clause on loops (executes if no break)
print("\nfor-else (no break):")
for i in range(3):
    print(f"  {i}")
else:
    print("  Loop completed without break")

print("\nfor-else (with break):")
for i in range(3):
    if i == 1:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}")
else:
    print("  This won't print")

# Practical: Searching with break/else
print("\nPractical: Search in list:")
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7

for num in numbers:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    print(f"  {target} not found")

# Nested loop control
print("\nNested loop with break:")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"  Breaking inner loop at ({i}, {j})")
            break
        print(f"  ({i}, {j})")
    else:
        continue  # Only reached if inner loop didn't break
    break  # Break outer loop if inner loop broke


# =============================================================================
# SECTION 6: NESTED LOOPS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: NESTED LOOPS")
print("=" * 60)

# Multiplication table
print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# Iterating over 2D list (matrix)
print("\n2D Matrix iteration:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(f"  {element}", end=" ")
    print()

# Pattern printing
print("\nPattern - Right triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("\nPattern - Pyramid:")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))


# =============================================================================
# SECTION 7: LIST COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: LIST COMPREHENSIONS")
print("=" * 60)

# Basic syntax: [expression for item in iterable]
numbers = [1, 2, 3, 4, 5]

# Simple transformation
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# With condition (filtering)
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# With if-else (ternary in expression)
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Labels: {labels}")

# Nested list comprehension (flatten matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# Dictionary comprehension
print("\nDictionary comprehension:")
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dict: {square_dict}")

# Set comprehension
print("\nSet comprehension:")
unique_squares = {x**2 for x in range(-5, 6)}
print(f"Unique squares: {unique_squares}")

# Generator expression (memory efficient)
print("\nGenerator expression:")
gen = (x**2 for x in range(10))
print(f"Generator: {gen}")
print(f"First 5: {[next(gen) for _ in range(5)]}")


# =============================================================================
# SECTION 8: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Find prime numbers
def find_primes(limit):
    """Find all prime numbers up to limit."""
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print("Prime numbers up to 50:")
print(f"  {find_primes(50)}")

# Example 2: Process list of dictionaries
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [70, 75, 80]},
    {"name": "Diana", "grades": [95, 98, 100]},
]

print("\nStudent averages:")
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    status = "Honors" if avg >= 90 else "Pass" if avg >= 60 else "Fail"
    print(f"  {student['name']}: {avg:.1f} ({status})")

# Example 3: Word frequency counter
text = "the quick brown fox jumps over the lazy dog the fox was quick"
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord frequency:")
for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

# Example 4: FizzBuzz with list comprehension
print("\nFizzBuzz (list comprehension):")
fizzbuzz = [
    "FizzBuzz" if i % 15 == 0 else
    "Fizz" if i % 3 == 0 else
    "Buzz" if i % 5 == 0 else
    str(i)
    for i in range(1, 21)
]
for i, val in enumerate(fizzbuzz, 1):
    print(f"  {i}: {val}")


# =============================================================================
# SECTION 9: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Sum of Even Numbers
-------------------------------
Calculate the sum of even numbers from 1 to 100 using:
- A for loop
- A while loop
- A list comprehension with sum()

EXERCISE 2: Multiplication Table Function
-----------------------------------------
Write a function print_multiplication_table(n) that prints
an n x n multiplication table.

EXERCISE 3: Find Common Elements
--------------------------------
Given two lists, find common elements without using sets:
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

EXERCISE 4: Password Generator
------------------------------
Generate a random password of length n containing:
- Uppercase letters
- Lowercase letters
- Digits
- Special characters

EXERCISE 5: Number Pattern
--------------------------
Print this pattern for n=5:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
""")

# Exercise Solutions
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
print("Exercise 1 - Sum of even numbers (1-100):")

# For loop
sum_for = 0
for i in range(2, 101, 2):
    sum_for += i

# While loop
sum_while = 0
i = 2
while i <= 100:
    sum_while += i
    i += 2

# List comprehension
sum_comp = sum([i for i in range(2, 101, 2)])

print(f"  For loop: {sum_for}")
print(f"  While loop: {sum_while}")
print(f"  List comprehension: {sum_comp}")

# Exercise 2
def print_multiplication_table(n):
    """Print n x n multiplication table."""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i*j:4}", end="")
        print()

print("\nExercise 2 - Multiplication table (5x5):")
print_multiplication_table(5)

# Exercise 3
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# Using nested loops (without sets)
common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print(f"\nExercise 3 - Common elements: {common}")

# Alternative with list comprehension
common_comp = [x for x in list1 if x in list2]
# Remove duplicates while preserving order
seen = set()
common_unique = [x for x in common_comp if not (x in seen or seen.add(x))]
print(f"  With list comprehension: {common_unique}")

# Exercise 4
import random
import string

def generate_password(length=12):
    """Generate a secure random password."""
    if length < 4:
        length = 4
    
    # Ensure at least one of each type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    
    # Fill rest randomly
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password.extend(random.choice(all_chars) for _ in range(length - 4))
    
    # Shuffle
    random.shuffle(password)
    return ''.join(password)

print("\nExercise 4 - Random passwords:")
for _ in range(3):
    print(f"  {generate_password(16)}")

# Exercise 5
def print_number_pattern(n):
    """Print number pattern."""
    num = 1
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(str(num))
            num += 1
        print(" ".join(row))

print("\nExercise 5 - Number pattern (n=5):")
print_number_pattern(5)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. For loops iterate over any iterable (list, tuple, string, dict, set, range)
2. Use range() for numeric sequences: range(stop), range(start, stop), range(start, stop, step)
3. enumerate() for index + value, zip() for parallel iteration
4. While loops repeat while condition is True
5. break exits loop, continue skips to next iteration
6. else clause on loops runs only if no break occurred
7. List comprehensions: [expr for item in iterable if condition]
8. Dictionary/set comprehensions: {key: val for ...}, {expr for ...}
9. Generator expressions: (expr for ...) - memory efficient
10. Nested loops for 2D data, patterns, combinations
11. Prefer for loops over while when iterating known sequences
""")

print("\n✅ File 03 complete! Run 'python 04_functions.py' next.")