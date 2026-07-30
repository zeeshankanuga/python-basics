"""
=============================================================================
FILE: 02_control_flow.py
TOPIC: Control Flow - If/Elif/Else, Comparison & Logical Operators
LEVEL: Beginner
PREREQUISITES: 01_basics_syntax.py
=============================================================================

This file covers conditional statements and control flow in Python:
- if, elif, else statements
- Comparison operators
- Logical operators (and, or, not)
- Truthy/Falsy values
- Ternary conditional operator
- Match-case statements (Python 3.10+)

Run this file: python 02_control_flow.py
"""

# =============================================================================
# SECTION 1: BASIC IF STATEMENTS
# =============================================================================

print("=" * 60)
print("SECTION 1: BASIC IF STATEMENTS")
print("=" * 60)

# Simple if statement
age = 18
if age >= 18:
    print(f"Age {age}: You are an adult")

# if with else
temperature = 25
if temperature > 30:
    print("It's hot!")
else:
    print("It's not hot")

# if-elif-else chain
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score {score}: Grade {grade}")


# =============================================================================
# SECTION 2: COMPARISON OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: COMPARISON OPERATORS")
print("=" * 60)

x, y = 10, 20

# Equality and inequality
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")   # Equal
print(f"x != y: {x != y}")   # Not equal

# Ordering
print(f"x < y: {x < y}")     # Less than
print(f"x > y: {x > y}")     # Greater than
print(f"x <= y: {x <= y}")   # Less than or equal
print(f"x >= y: {x >= y}")   # Greater than or equal

# Chained comparisons (Pythonic!)
print(f"\nChained comparisons:")
print(f"0 < x < 100: {0 < x < 100}")        # True
print(f"5 < x < 15: {5 < x < 15}")           # True
print(f"x < y < 30: {x < y < 30}")           # True
print(f"x > y > 5: {x > y > 5}")             # False


# =============================================================================
# SECTION 3: LOGICAL OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: LOGICAL OPERATORS")
print("=" * 60)

# and - both must be True
has_license = True
has_car = False
can_drive = has_license and has_car
print(f"has_license={has_license}, has_car={has_car}")
print(f"can_drive (and): {can_drive}")

# or - at least one must be True
is_weekend = False
is_holiday = True
day_off = is_weekend or is_holiday
print(f"\nis_weekend={is_weekend}, is_holiday={is_holiday}")
print(f"day_off (or): {day_off}")

# not - inverts boolean
is_raining = False
print(f"\nis_raining={is_raining}")
print(f"not is_raining: {not is_raining}")

# Short-circuit evaluation
print("\nShort-circuit evaluation:")
# Second part not evaluated if first determines result
result = True or (print("This won't print") or True)
print(f"True or (something): {result}")

result = False and (print("This won't print either") and False)
print(f"False and (something): {result}")


# =============================================================================
# SECTION 4: TRUTHY AND FALSY VALUES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: TRUTHY AND FALSY VALUES")
print("=" * 60)

# Falsy values (evaluate to False in boolean context)
falsy_values = [
    False,
    None,
    0,
    0.0,
    "",
    [],
    {},
    set(),
    range(0)
]

# Truthy values (evaluate to True)
truthy_values = [
    True,
    1,
    -1,
    3.14,
    "hello",
    [1, 2, 3],
    {"key": "value"},
    {1, 2, 3}
]

print("Falsy values:")
for val in falsy_values:
    print(f"  {repr(val):20} -> {bool(val)}")

print("\nTruthy values:")
for val in truthy_values:
    print(f"  {repr(val):20} -> {bool(val)}")

# Practical usage
user_input = ""
if user_input:
    print(f"\nUser entered: {user_input}")
else:
    print("\nNo input provided (empty string is falsy)")

# Checking for None explicitly vs truthy check
value = None
if value is None:
    print("Value is None (explicit check)")

if not value:
    print("Value is falsy (includes None, 0, '', [], etc.)")


# =============================================================================
# SECTION 5: TERNARY CONDITIONAL OPERATOR
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: TERNARY CONDITIONAL OPERATOR")
print("=" * 60)

# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# Multiple conditions (nested ternary - use sparingly)
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F"))
print(f"Score {score}: Grade {grade}")

# Using with print
name = "Alice"
greeting = f"Hello, {name}" if name else "Hello, Guest"
print(greeting)

# Assignment with default
user_name = None
display_name = user_name if user_name else "Anonymous"
print(f"Display name: {display_name}")


# =============================================================================
# SECTION 6: MATCH-CASE STATEMENTS (PYTHON 3.10+)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: MATCH-CASE STATEMENTS (Python 3.10+)")
print("=" * 60)

# Note: Match-case requires Python 3.10+
import sys
print(f"Python version: {sys.version.split()[0]}")

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case 301 | 302 | 303 | 307 | 308:  # Multiple patterns (OR)
            return "Redirect"
        case 400 | 401 | 403:
            return "Client Error"
        case _:  # Wildcard (default case)
            return "Unknown Status"

print(f"Status 200: {http_status(200)}")
print(f"Status 404: {http_status(404)}")
print(f"Status 301: {http_status(301)}")
print(f"Status 999: {http_status(999)}")

# Pattern matching with data structures
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Quitting..."
        case ["load", filename]:
            return f"Loading {filename}..."
        case ["save", filename]:
            return f"Saving {filename}..."
        case ["copy", src, dest]:
            return f"Copying {src} to {dest}"
        case ["move", src, dest]:
            return f"Moving {src} to {dest}"
        case _:
            return "Unknown command"

print(f"\nCommands:")
print(f"  {process_command('quit')}")
print(f"  {process_command('load data.txt')}")
print(f"  {process_command('save report.pdf')}")
print(f"  {process_command('copy file1.txt file2.txt')}")
print(f"  {process_command('move old.txt new.txt')}")
print(f"  {process_command('delete file.txt')}")

# Pattern matching with guards (conditions)
def check_number(n):
    match n:
        case x if x < 0:
            return "Negative"
        case 0:
            return "Zero"
        case x if x % 2 == 0:
            return "Positive Even"
        case _:
            return "Positive Odd"

print(f"\nNumber checks:")
for num in [-5, 0, 2, 7]:
    print(f"  {num}: {check_number(num)}")


# =============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Grade Calculator
def calculate_grade(score):
    """Calculate letter grade from numeric score."""
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Score out of range"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Grade Calculator:")
test_scores = [95, 87, 72, 65, 45, 105, -5, "ninety"]
for s in test_scores:
    print(f"  Score {s}: {calculate_grade(s)}")

# Example 2: Simple Calculator
def calculator(a, operator, b):
    """Perform basic arithmetic operations."""
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Error: Division by zero"
            return a / b
        case "//":
            if b == 0:
                return "Error: Division by zero"
            return a // b
        case "%":
            return a % b
        case "**":
            return a ** b
        case _:
            return f"Error: Unknown operator '{operator}'"

print("\nCalculator:")
operations = [(10, "+", 5), (10, "-", 5), (10, "*", 5), (10, "/", 5),
              (10, "//", 3), (10, "%", 3), (2, "**", 10), (10, "^", 2)]
for a, op, b in operations:
    print(f"  {a} {op} {b} = {calculator(a, op, b)}")

# Example 3: FizzBuzz
print("\nFizzBuzz (1-20):")
for i in range(1, 21):
    if i % 15 == 0:
        result = "FizzBuzz"
    elif i % 3 == 0:
        result = "Fizz"
    elif i % 5 == 0:
        result = "Buzz"
    else:
        result = str(i)
    print(f"  {i}: {result}")


# =============================================================================
# SECTION 8: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Age Category
------------------------
Write a function that takes an age and returns:
- "Infant" (0-1)
- "Toddler" (2-3)
- "Child" (4-12)
- "Teenager" (13-19)
- "Adult" (20-64)
- "Senior" (65+)
Handle invalid ages (negative, >150)

EXERCISE 2: Leap Year
---------------------
Write a function is_leap_year(year) that returns True if:
- Year divisible by 4 AND not divisible by 100
- OR year divisible by 400

EXERCISE 3: Triangle Type
-------------------------
Given three side lengths, determine if they form a valid triangle and type:
- Not a triangle (triangle inequality violated)
- Equilateral (all sides equal)
- Isosceles (two sides equal)
- Scalene (all sides different)

EXERCISE 4: Number Guessing Game Logic
--------------------------------------
Write logic for a number guessing game:
- Generate random number 1-100
- User guesses
- Tell them "Too high", "Too low", or "Correct!"
- Count attempts

EXERCISE 5: Password Validator
------------------------------
Write a function that validates password strength:
- At least 8 characters
- Contains uppercase, lowercase, digit, special char
- Returns list of missing requirements
""")

# Exercise Solutions
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
def age_category(age):
    if not isinstance(age, (int, float)) or age < 0 or age > 150:
        return "Invalid age"
    if age <= 1:
        return "Infant"
    elif age <= 3:
        return "Toddler"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"

print("Exercise 1 - Age Categories:")
for age in [-5, 0, 1, 3, 7, 15, 25, 65, 100, 151]:
    print(f"  Age {age}: {age_category(age)}")

# Exercise 2
def is_leap_year(year):
    if not isinstance(year, int) or year <= 0:
        return False
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("\nExercise 2 - Leap Years:")
for year in [2000, 2004, 1900, 2021, 2024, 2100]:
    print(f"  {year}: {is_leap_year(year)}")

# Exercise 3
def triangle_type(a, b, c):
    # Check triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print("\nExercise 3 - Triangle Types:")
test_triangles = [(3, 3, 3), (3, 4, 5), (5, 5, 8), (1, 2, 3), (2, 2, 5)]
for a, b, c in test_triangles:
    print(f"  Sides ({a}, {b}, {c}): {triangle_type(a, b, c)}")

# Exercise 4
import random

def number_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    guesses = [50, 75, 60, 68, 65]  # Simulated guesses
    
    print("\nExercise 4 - Number Guessing (simulated):")
    print(f"  Secret number: {secret}")
    for guess in guesses:
        attempts += 1
        if guess < secret:
            result = "Too low"
        elif guess > secret:
            result = "Too high"
        else:
            result = f"Correct! Found in {attempts} attempts"
            break
        print(f"  Guess {guess}: {result}")
    else:
        print(f"  Failed to guess in {attempts} attempts. Number was {secret}")

number_guessing_game()

# Exercise 5
def validate_password(password):
    """Returns list of missing requirements."""
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters")
    if not any(c.isupper() for c in password):
        errors.append("Uppercase letter")
    if not any(c.islower() for c in password):
        errors.append("Lowercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("Digit")
    if not any(not c.isalnum() for c in password):
        errors.append("Special character")
    return errors

print("\nExercise 5 - Password Validator:")
test_passwords = ["weak", "StrongPass", "StrongPass1", "StrongPass1!", "short1!"]
for pwd in test_passwords:
    issues = validate_password(pwd)
    status = "VALID" if not issues else f"INVALID: {', '.join(issues)}"
    print(f"  '{pwd}': {status}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Use if/elif/else for conditional logic
2. Python uses indentation (4 spaces) for blocks - no braces!
3. Comparison operators: ==, !=, <, >, <=, >=
4. Chained comparisons: a < b < c (evaluates left to right)
5. Logical operators: and, or, not (short-circuit evaluation)
6. Truthy/Falsy: None, 0, "", [], {} are falsy; most else are truthy
7. Ternary: value_if_true if condition else value_if_false
8. Match-case (3.10+): powerful pattern matching for complex conditions
9. Always handle edge cases (invalid input, boundary values)
10. Keep conditions readable - extract complex logic to functions
""")

print("\n✅ File 02 complete! Run 'python 03_loops.py' next.")