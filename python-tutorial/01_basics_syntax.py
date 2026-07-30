"""
=============================================================================
FILE: 01_basics_syntax.py
TOPIC: Python Basics - Variables, Data Types, Basic Operations
LEVEL: Beginner
PREREQUISITES: None
=============================================================================

This file covers the fundamental building blocks of Python programming:
- Variables and assignment
- Basic data types (int, float, str, bool)
- Type conversion
- Basic operators (arithmetic, comparison, logical)
- String operations
- Input/Output basics

Run this file: python 01_basics_syntax.py
"""

# =============================================================================
# SECTION 1: VARIABLES AND ASSIGNMENT
# =============================================================================

print("=" * 60)
print("SECTION 1: VARIABLES AND ASSIGNMENT")
print("=" * 60)

# Variables are containers for storing data values
# Python uses dynamic typing - no need to declare type

# Variable naming rules:
# - Must start with letter or underscore
# - Can contain letters, numbers, underscores
# - Case-sensitive (name != Name != NAME)
# - Cannot use Python keywords (if, else, for, while, etc.)

# Valid variable names:
user_name = "Alice"          # snake_case (recommended by PEP 8)
userAge = 25                 # camelCase (works but not Pythonic)
_user_id = 1001              # leading underscore (internal use)
MAX_RETRIES = 3              # UPPER_SNAKE_CASE for constants

# Invalid variable names (will cause SyntaxError):
# 2user = "Bob"              # Can't start with number
# user-name = "Charlie"      # Can't use hyphen
# class = "student"          # Can't use keywords

print(f"user_name: {user_name}")
print(f"userAge: {userAge}")
print(f"_user_id: {_user_id}")
print(f"MAX_RETRIES: {MAX_RETRIES}")

# Multiple assignment
x = y = z = 0
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# Unpacking assignment
a, b, c = 1, 2, 3
print(f"Unpacking: a={a}, b={b}, c={c}")

# Swapping variables (Pythonic way)
a, b = b, a
print(f"After swap: a={a}, b={b}")


# =============================================================================
# SECTION 2: BASIC DATA TYPES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: BASIC DATA TYPES")
print("=" * 60)

# 1. Integer (int) - Whole numbers, unlimited precision
age = 25
temperature = -10
large_number = 10**100  # Python handles arbitrarily large integers
print(f"Integers: age={age}, temp={temperature}, large={large_number}")
print(f"Type of age: {type(age)}")

# 2. Float (float) - Decimal numbers
price = 19.99
pi = 3.14159
scientific = 1.5e-4  # Scientific notation (0.00015)
print(f"\nFloats: price={price}, pi={pi}, scientific={scientific}")
print(f"Type of price: {type(price)}")

# 3. String (str) - Text data, immutable sequence of characters
name = "Alice"
greeting = 'Hello, World!'
multiline = """This is a
multi-line string"""
raw_string = r"C:\Users\name"  # Raw string (backslash treated literally)
print(f"\nStrings:")
print(f"  name: {name}")
print(f"  greeting: {greeting}")
print(f"  multiline: {multiline}")
print(f"  raw_string: {raw_string}")
print(f"Type of name: {type(name)}")

# 4. Boolean (bool) - True or False
is_student = True
has_graduated = False
print(f"\nBooleans: is_student={is_student}, has_graduated={has_graduated}")
print(f"Type of is_student: {type(is_student)}")

# 5. None - Represents absence of value
result = None
print(f"\nNone: result={result}")
print(f"Type of result: {type(result)}")


# =============================================================================
# SECTION 3: TYPE CONVERSION (CASTING)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: TYPE CONVERSION")
print("=" * 60)

# Implicit conversion (automatic)
int_val = 10
float_val = 3.5
result = int_val + float_val  # int converted to float automatically
print(f"Implicit: {int_val} + {float_val} = {result} (type: {type(result)})")

# Explicit conversion (manual)
str_num = "42"
int_num = int(str_num)        # String to integer
float_num = float(str_num)    # String to float
str_from_int = str(42)        # Integer to string
bool_from_int = bool(0)       # Integer to boolean (0=False, non-zero=True)
bool_from_str = bool("")      # String to boolean (empty=False, non-empty=True)

print(f"Explicit conversions:")
print(f"  int('42') = {int_num} (type: {type(int_num)})")
print(f"  float('42') = {float_num} (type: {type(float_num)})")
print(f"  str(42) = '{str_from_int}' (type: {type(str_from_int)})")
print(f"  bool(0) = {bool_from_int}")
print(f"  bool('') = {bool_from_str}")
print(f"  bool('hello') = {bool('hello')}")

# Conversion errors (will raise ValueError)
# int("hello")  # ValueError: invalid literal for int()


# =============================================================================
# SECTION 4: BASIC OPERATORS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: BASIC OPERATORS")
print("=" * 60)

# Arithmetic Operators
a, b = 10, 3
print(f"Arithmetic (a={a}, b={b}):")
print(f"  Addition: a + b = {a + b}")
print(f"  Subtraction: a - b = {a - b}")
print(f"  Multiplication: a * b = {a * b}")
print(f"  Division: a / b = {a / b}")          # Always returns float
print(f"  Floor Division: a // b = {a // b}")  # Returns int (rounds down)
print(f"  Modulo: a % b = {a % b}")            # Remainder
print(f"  Exponentiation: a ** b = {a ** b}")  # Power

# Comparison Operators
x, y = 10, 20
print(f"\nComparison (x={x}, y={y}):")
print(f"  Equal: x == y = {x == y}")
print(f"  Not Equal: x != y = {x != y}")
print(f"  Greater Than: x > y = {x > y}")
print(f"  Less Than: x < y = {x < y}")
print(f"  Greater/Equal: x >= y = {x >= y}")
print(f"  Less/Equal: x <= y = {x <= y}")

# Logical Operators
p, q = True, False
print(f"\nLogical (p={p}, q={q}):")
print(f"  AND: p and q = {p and q}")
print(f"  OR: p or q = {p or q}")
print(f"  NOT: not p = {not p}")

# Short-circuit evaluation
# print(10 / 0) would raise ZeroDivisionError
# But: False and (10 / 0) returns False without evaluating second part
result = False and (10 / 0)  # Returns False, no error!
print(f"\nShort-circuit: False and (10/0) = {result}")

# Identity Operators (check if same object in memory)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"\nIdentity (list1=[1,2,3], list2=[1,2,3], list3=list1):")
print(f"  list1 is list2 = {list1 is list2}")   # False (different objects)
print(f"  list1 is list3 = {list1 is list3}")   # True (same object)
print(f"  list1 == list2 = {list1 == list2}")   # True (same values)

# Membership Operators (check if value in sequence)
fruits = ["apple", "banana", "cherry"]
print(f"\nMembership (fruits={fruits}):")
print(f"  'apple' in fruits = {'apple' in fruits}")
print(f"  'grape' not in fruits = {'grape' not in fruits}")


# =============================================================================
# SECTION 5: STRING OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: STRING OPERATIONS")
print("=" * 60)

text = "Hello, Python!"

# String indexing and slicing
print(f"Original: '{text}'")
print(f"  Length: len(text) = {len(text)}")
print(f"  First char: text[0] = '{text[0]}'")
print(f"  Last char: text[-1] = '{text[-1]}'")
print(f"  Slice [0:5]: text[0:5] = '{text[0:5]}'")
print(f"  Slice [:5]: text[:5] = '{text[:5]}'")
print(f"  Slice [7:]: text[7:] = '{text[7:]}'")
print(f"  Slice [::2]: text[::2] = '{text[::2]}' (every 2nd char)")
print(f"  Reverse: text[::-1] = '{text[::-1]}'")

# String methods
print(f"\nString Methods:")
print(f"  Upper: text.upper() = '{text.upper()}'")
print(f"  Lower: text.lower() = '{text.lower()}'")
print(f"  Title: text.title() = '{text.title()}'")
print(f"  Strip: '  hello  '.strip() = '{'  hello  '.strip()}'")
print(f"  Replace: text.replace('Python', 'World') = '{text.replace('Python', 'World')}'")
print(f"  Split: 'a,b,c'.split(',') = {'a,b,c'.split(',')}")
print(f"  Join: '-'.join(['a','b','c']) = '{'-'.join(['a','b','c'])}'")
print(f"  Startswith: text.startswith('Hello') = {text.startswith('Hello')}")
print(f"  Endswith: text.endswith('!') = {text.endswith('!')}")

# String formatting (multiple ways)
name = "Alice"
age = 25
print(f"\nString Formatting:")
print(f"  f-string: f'Name: {name}, Age: {age}' = 'Name: {name}, Age: {age}'")
print(f"  .format(): 'Name: {{}}, Age: {{}}'.format(name, age) = 'Name: {name}, Age: {age}'")
print(f"  % formatting: 'Name: %s, Age: %d' % (name, age) = 'Name: %s, Age: %d' % (name, age)")

# Escape sequences
print(f"\nEscape Sequences:")
print(f"  Newline: 'Line1\\nLine2' = ")
print('Line1\nLine2')
print(f"  Tab: 'Col1\\tCol2' = 'Col1\tCol2'")
print(f"  Quote: 'He said \\\"Hi\\\"' = 'He said \"Hi\"'")
print(f"  Raw string: r'C:\\Users\\name' = {r'C:\Users\name'}")


# =============================================================================
# SECTION 6: BASIC INPUT/OUTPUT
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: BASIC INPUT/OUTPUT")
print("=" * 60)

# print() function - output to console
print("Simple print")
print("Multiple", "arguments", "separated", "by", "space")
print("Custom separator:", "a", "b", "c", sep=" | ")
print("No newline:", "Hello", end=" ")
print("World")

# input() function - read from user (commented out for auto-run)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}, you are {age} years old")

# For demo purposes, we'll simulate input
print("\n[Input simulation - normally would prompt user]")


# =============================================================================
# SECTION 7: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Variables and Types
-------------------------------
Create variables for:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- Whether you're a student (boolean)
Print all variables with their types.

EXERCISE 2: Type Conversion
---------------------------
Convert the string "3.14" to:
- A float
- An integer (what happens?)
- A boolean

EXERCISE 3: String Operations
-----------------------------
Given: message = "  Python Programming  "
- Remove whitespace
- Convert to uppercase
- Replace "Python" with "Java"
- Check if it starts with "PYTHON"

EXERCISE 4: Arithmetic
----------------------
Calculate:
- Area of circle with radius 5 (π * r²)
- Compound interest: P(1+r)^t where P=1000, r=0.05, t=3
- How many minutes in a year?

EXERCISE 5: Formatting
----------------------
Create a formatted string showing:
"Student: [name], Age: [age], GPA: [gpa:.2f]"
where name="John", age=20, gpa=3.75
""")

# Exercise Solutions (uncomment to run)
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
student_name = "Alex"
student_age = 22
student_height = 1.75
is_student = True
print(f"Exercise 1: name={student_name} ({type(student_name)}), "
      f"age={student_age} ({type(student_age)}), "
      f"height={student_height} ({type(student_height)}), "
      f"is_student={is_student} ({type(is_student)})")

# Exercise 2
pi_str = "3.14"
pi_float = float(pi_str)
pi_int = int(float(pi_str))  # Must convert to float first!
pi_bool = bool(pi_str)
print(f"Exercise 2: float={pi_float}, int={pi_int}, bool={pi_bool}")

# Exercise 3
message = "  Python Programming  "
cleaned = message.strip()
uppered = cleaned.upper()
replaced = uppered.replace("PYTHON", "JAVA")
starts_with = uppered.startswith("PYTHON")
print(f"Exercise 3: cleaned='{cleaned}', uppered='{uppered}', "
      f"replaced='{replaced}', starts_with={starts_with}")

# Exercise 4
import math
radius = 5
area = math.pi * radius ** 2
compound_interest = 1000 * (1 + 0.05) ** 3
minutes_in_year = 365 * 24 * 60
print(f"Exercise 4: area={area:.2f}, compound_interest={compound_interest:.2f}, "
      f"minutes_in_year={minutes_in_year}")

# Exercise 5
name, age, gpa = "John", 20, 3.75
formatted = f"Student: {name}, Age: {age}, GPA: {gpa:.2f}"
print(f"Exercise 5: {formatted}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Python is dynamically typed - variables don't need type declarations
2. Use snake_case for variable names (PEP 8 convention)
3. Four basic data types: int, float, str, bool (plus None)
4. Type conversion: int(), float(), str(), bool()
5. Operators: arithmetic, comparison, logical, identity, membership
6. Strings are immutable - methods return new strings
7. f-strings (f"...") are the preferred formatting method (Python 3.6+)
8. Use print() for output, input() for user input
9. Practice: type code manually, experiment with variations
""")

print("\n✅ File 01 complete! Run 'python 02_control_flow.py' next.")