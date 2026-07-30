"""
=============================================================================
FILE: 05_data_structures.py
TOPIC: Data Structures - Lists, Tuples, Dictionaries, Sets
LEVEL: Beginner
PREREQUISITES: 01_basics_syntax.py, 02_control_flow.py, 03_loops.py, 04_functions.py
=============================================================================

This file covers Python's built-in data structures:
- Lists (mutable, ordered sequences)
- Tuples (immutable, ordered sequences)
- Dictionaries (key-value mappings)
- Sets (unique, unordered collections)
- Common operations and methods for each
- Choosing the right data structure

Run this file: python 05_data_structures.py
"""

# =============================================================================
# SECTION 1: LISTS
# =============================================================================

print("=" * 60)
print("SECTION 1: LISTS")
print("=" * 60)

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]
print(f"Empty: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# List indexing and slicing
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"\nOriginal: {fruits}")
print(f"First: {fruits[0]}")
print(f"Last: {fruits[-1]}")
print(f"Slice [1:4]: {fruits[1:4]}")
print(f"Slice [:3]: {fruits[:3]}")
print(f"Slice [2:]: {fruits[2:]}")
print(f"Every 2nd: {fruits[::2]}")
print(f"Reversed: {fruits[::-1]}")

# Modifying lists (mutable!)
fruits[0] = "apricot"
print(f"\nAfter fruits[0] = 'apricot': {fruits}")

# List methods
print("\nList methods:")
fruits.append("fig")              # Add to end
print(f"append('fig'): {fruits}")

fruits.insert(1, "blueberry")     # Insert at index
print(f"insert(1, 'blueberry'): {fruits}")

fruits.extend(["grape", "honeydew"])  # Extend with iterable
print(f"extend(['grape', 'honeydew']): {fruits}")

removed = fruits.pop()            # Remove and return last
print(f"pop(): removed '{removed}', list: {fruits}")

removed = fruits.pop(1)           # Remove at index
print(f"pop(1): removed '{removed}', list: {fruits}")

fruits.remove("cherry")           # Remove first occurrence of value
print(f"remove('cherry'): {fruits}")

index = fruits.index("date")      # Find index of value
print(f"index('date'): {index}")

count = fruits.count("apple")     # Count occurrences
print(f"count('apple'): {count}")

fruits.sort()                     # Sort in place
print(f"sort(): {fruits}")

fruits.reverse()                  # Reverse in place
print(f"reverse(): {fruits}")

# Copying lists
original = [1, 2, 3]
shallow_copy = original.copy()    # or list(original) or original[:]
shallow_copy[0] = 99
print(f"\nOriginal: {original}, Copy: {shallow_copy}")

# List comprehensions (review)
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
print(f"\nSquares: {squares}")
print(f"Evens: {evens}")


# =============================================================================
# SECTION 2: TUPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: TUPLES")
print("=" * 60)

# Creating tuples
empty_tuple = ()
single = (1,)           # Comma required for single element!
pair = (1, 2)
triple = (1, 2, 3)
print(f"Empty: {empty_tuple}")
print(f"Single: {single}")
print(f"Pair: {pair}")
print(f"Triple: {triple}")

# Tuple from iterable
from_list = tuple([1, 2, 3])
from_string = tuple("hello")
print(f"From list: {from_list}")
print(f"From string: {from_string}")

# Tuples are immutable
coordinates = (10, 20)
print(f"\nCoordinates: {coordinates}")
print(f"x: {coordinates[0]}, y: {coordinates[1]}")
# coordinates[0] = 5  # TypeError! Tuples are immutable

# But... if tuple contains mutable object, that object can be modified
mixed_tuple = (1, [2, 3], 4)
mixed_tuple[1].append(99)
print(f"Mutable element in tuple: {mixed_tuple}")

# Tuple unpacking
point = (3, 4)
x, y = point
print(f"\nUnpacking: x={x}, y={y}")

# Extended unpacking (Python 3+)
first, *middle, last = [1, 2, 3, 4, 5]
print(f"Extended: first={first}, middle={middle}, last={last}")

# Swapping variables (uses tuple packing/unpacking)
a, b = 10, 20
a, b = b, a
print(f"Swap: a={a}, b={b}")

# Tuple methods (only count and index)
colors = ("red", "green", "blue", "red")
print(f"\nTuple methods:")
print(f"count('red'): {colors.count('red')}")
print(f"index('blue'): {colors.index('blue')}")

# Named tuples (collections.namedtuple)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y", "z"])
p = Point(1, 2, 3)
print(f"\nNamed tuple: {p}")
print(f"  p.x={p.x}, p.y={p.y}, p.z={p.z}")
print(f"  p[0]={p[0]}, p[1]={p[1]}")


# =============================================================================
# SECTION 3: DICTIONARIES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: DICTIONARIES")
print("=" * 60)

# Creating dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"Empty: {empty_dict}")
print(f"Person: {person}")

# Alternative creation
person2 = dict(name="Bob", age=30, city="LA")
person3 = dict([("name", "Charlie"), ("age", 35)])
print(f"dict(): {person2}")
print(f"from list of tuples: {person3}")

# Accessing values
print(f"\nAccessing:")
print(f"person['name']: {person['name']}")
print(f"person.get('age'): {person.get('age')}")
print(f"person.get('country', 'USA'): {person.get('country', 'USA')}")  # Default

# Modifying dictionaries
person["age"] = 26                    # Update existing
person["email"] = "alice@example.com" # Add new
print(f"\nAfter modifications: {person}")

# Dictionary methods
print(f"\nMethods:")
print(f"keys(): {list(person.keys())}")
print(f"values(): {list(person.values())}")
print(f"items(): {list(person.items())}")

# pop, popitem, update
age = person.pop("age")
print(f"pop('age'): {age}, dict: {person}")

last = person.popitem()
print(f"popitem(): {last}, dict: {person}")

person.update({"age": 27, "country": "USA"})
print(f"update(): {person}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nDict comprehension: {squares_dict}")

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(f"Merge with |: {merged}")

# In-place merge (Python 3.9+)
dict1 |= dict2
print(f"In-place merge: {dict1}")


# =============================================================================
# SECTION 4: SETS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: SETS")
print("=" * 60)

# Creating sets
empty_set = set()          # {} creates empty dict!
numbers_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed
print(f"Empty: {empty_set}")
print(f"Numbers: {numbers_set}")
print(f"From list (dupes removed): {from_list}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\nSet a: {a}")
print(f"Set b: {b}")
print(f"Union (a | b): {a | b}")
print(f"Intersection (a & b): {a & b}")
print(f"Difference (a - b): {a - b}")
print(f"Symmetric diff (a ^ b): {a ^ b}")

# Set methods
s = {1, 2, 3}
s.add(4)
print(f"\nadd(4): {s}")

s.update([5, 6, 7])
print(f"update([5,6,7]): {s}")

s.remove(3)           # Raises KeyError if not found
print(f"remove(3): {s}")

s.discard(10)         # No error if not found
print(f"discard(10): {s}")

popped = s.pop()      # Remove and return arbitrary element
print(f"pop(): {popped}, remaining: {s}")

s.clear()
print(f"clear(): {s}")

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"\nSet comprehension: {even_squares}")

# Frozenset (immutable set)
frozen = frozenset([1, 2, 3, 4])
print(f"Frozenset: {frozen}")
# frozen.add(5)  # AttributeError!


# =============================================================================
# SECTION 5: COMMON OPERATIONS ACROSS TYPES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: COMMON OPERATIONS")
print("=" * 60)

# Length
print(f"len([1,2,3]): {len([1,2,3])}")
print(f"len((1,2,3)): {len((1,2,3))}")
print(f"len({{'a':1}}): {len({'a':1})}")
print(f"len({{1,2,3}}): {len({1,2,3})}")

# Membership testing
print(f"\nMembership:")
print(f"2 in [1,2,3]: {2 in [1,2,3]}")
print(f"'b' in ('a','b','c'): {'b' in ('a','b','c')}")
print(f"'name' in {{'name':'Alice'}}: {'name' in {'name':'Alice'}}")
print(f"3 in {{1,2,3}}: {3 in {1,2,3}}")

# Iteration
print(f"\nIteration:")
for item in [1, 2, 3]:
    print(f"  List: {item}")

for item in (1, 2, 3):
    print(f"  Tuple: {item}")

for key in {'a': 1, 'b': 2}:
    print(f"  Dict key: {key}")

for item in {1, 2, 3}:
    print(f"  Set: {item}")

# min, max, sum
numbers = [5, 2, 9, 1, 7]
print(f"\nMin/Max/Sum:")
print(f"min: {min(numbers)}")
print(f"max: {max(numbers)}")
print(f"sum: {sum(numbers)}")

# sorted (returns new list)
print(f"sorted: {sorted(numbers)}")
print(f"sorted reverse: {sorted(numbers, reverse=True)}")

# any, all
print(f"\nany/all:")
print(f"any([False, False, True]): {any([False, False, True])}")
print(f"all([True, True, True]): {all([True, True, True])}")


# =============================================================================
# SECTION 6: NESTED DATA STRUCTURES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: NESTED DATA STRUCTURES")
print("=" * 60)

# List of dictionaries (common for records)
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [70, 75, 80]},
]

print("Students:")
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"  {student['name']}: grades={student['grades']}, avg={avg:.1f}")

# Dictionary of lists (grouping)
grades_by_subject = {
    "Math": [85, 92, 70],
    "Science": [90, 88, 75],
    "English": [78, 95, 80],
}
print(f"\nGrades by subject:")
for subject, grades in grades_by_subject.items():
    print(f"  {subject}: {grades}")

# Nested dictionary
company = {
    "engineering": {
        "backend": ["Alice", "Bob"],
        "frontend": ["Charlie"],
    },
    "sales": {
        "domestic": ["Diana"],
        "international": ["Eve", "Frank"],
    },
}
print(f"\nCompany structure:")
for dept, teams in company.items():
    print(f"  {dept}:")
    for team, members in teams.items():
        print(f"    {team}: {members}")

# Accessing nested data
print(f"\nAccessing nested:")
print(f"  Backend team: {company['engineering']['backend']}")
print(f"  First backend dev: {company['engineering']['backend'][0]}")


# =============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Frequency counter
text = "the quick brown fox jumps over the lazy dog"
words = text.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word frequency:")
for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

# Example 2: Grouping data
from collections import defaultdict

data = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("vegetable", "carrot"),
    ("fruit", "cherry"),
    ("vegetable", "broccoli"),
]

grouped = defaultdict(list)
for category, item in data:
    grouped[category].append(item)

print(f"\nGrouped data:")
for category, items in grouped.items():
    print(f"  {category}: {items}")

# Example 3: Removing duplicates while preserving order
def unique_preserve_order(seq):
    """Remove duplicates, preserve order."""
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

original = [1, 2, 2, 3, 1, 4, 2, 5]
print(f"\nRemove duplicates: {original} -> {unique_preserve_order(original)}")

# Example 4: Flattening nested structures
def flatten(nested):
    """Flatten arbitrarily nested lists."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [1, [2, [3, 4], 5], 6, [[7], 8]]
print(f"Flatten: {nested} -> {flatten(nested)}")


# =============================================================================
# SECTION 8: CHOOSING THE RIGHT DATA STRUCTURE
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: CHOOSING THE RIGHT DATA STRUCTURE")
print("=" * 60)

print("""
Data Structure Selection Guide:

LIST - Use when:
  ✓ Ordered collection
  ✓ Need index access
  ✓ Allow duplicates
  ✓ Frequent append/pop at end
  ✗ Not: frequent insert/delete at front, membership testing

TUPLE - Use when:
  ✓ Immutable sequence
  ✓ Fixed structure (records, coordinates)
  ✓ Dictionary keys (if all elements hashable)
  ✓ Return multiple values from function
  ✗ Not: need to modify after creation

DICTIONARY - Use when:
  ✓ Key-value mapping
  ✓ Fast lookup by key (O(1))
  ✓ Unique keys
  ✓ Need to associate related data
  ✗ Not: ordered by insertion (Python 3.7+ preserves order)

SET - Use when:
  ✓ Unique elements only
  ✓ Fast membership testing (O(1))
  ✓ Set operations (union, intersection)
  ✗ Not: need order, need duplicates, need index access

COMMON PATTERNS:
  - List of dicts: Records/rows (like CSV, DB results)
  - Dict of lists: Grouping by category
  - Dict of dicts: Nested lookup (e.g., config)
  - Set for deduplication, membership
  - Tuple for fixed records, coordinates, DB rows
""")


# =============================================================================
# SECTION 9: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: List Manipulation
-----------------------------
Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Create list of squares
- Filter even numbers
- Sum all numbers
- Find max and min

EXERCISE 2: Dictionary Operations
---------------------------------
Create a phonebook dict with name->phone mappings:
- Add 3 entries
- Look up a number
- Update a number
- Delete an entry
- Print all entries sorted by name

EXERCISE 3: Set Operations
--------------------------
Given two sets:
  set_a = {1, 2, 3, 4, 5}
  set_b = {4, 5, 6, 7, 8}
Find: union, intersection, difference, symmetric difference

EXERCISE 4: Nested Data Processing
----------------------------------
Given list of student dicts with name and grades:
- Calculate average for each student
- Find student with highest average
- Group students by grade range (A: 90+, B: 80-89, etc.)

EXERCISE 5: Data Transformation
-------------------------------
Convert list of tuples to dictionary:
  data = [("a", 1), ("b", 2), ("c", 3)]
Then convert back to list of tuples
""")

# Exercise Solutions
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
numbers = list(range(1, 11))
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)

print("Exercise 1:")
print(f"  Numbers: {numbers}")
print(f"  Squares: {squares}")
print(f"  Evens: {evens}")
print(f"  Sum: {total}, Max: {maximum}, Min: {minimum}")

# Exercise 2
phonebook = {}
phonebook["Alice"] = "555-1234"
phonebook["Bob"] = "555-5678"
phonebook["Charlie"] = "555-9012"

print("\nExercise 2:")
print(f"  Initial: {phonebook}")
print(f"  Alice's number: {phonebook['Alice']}")
phonebook["Bob"] = "555-0000"
print(f"  After update: {phonebook}")
del phonebook["Charlie"]
print(f"  After delete: {phonebook}")
for name in sorted(phonebook):
    print(f"  {name}: {phonebook[name]}")

# Exercise 3
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\nExercise 3:")
print(f"  Set A: {set_a}")
print(f"  Set B: {set_b}")
print(f"  Union: {set_a | set_b}")
print(f"  Intersection: {set_a & set_b}")
print(f"  Difference (A-B): {set_a - set_b}")
print(f"  Symmetric diff: {set_a ^ set_b}")

# Exercise 4
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [70, 75, 80]},
    {"name": "Diana", "grades": [95, 98, 100]},
]

print("\nExercise 4:")
# Calculate averages
for s in students:
    s["avg"] = sum(s["grades"]) / len(s["grades"])
    print(f"  {s['name']}: avg={s['avg']:.1f}")

# Highest average
top = max(students, key=lambda s: s["avg"])
print(f"  Top student: {top['name']} ({top['avg']:.1f})")

# Group by grade range
groups = {"A": [], "B": [], "C": [], "D": [], "F": []}
for s in students:
    avg = s["avg"]
    if avg >= 90:
        groups["A"].append(s["name"])
    elif avg >= 80:
        groups["B"].append(s["name"])
    elif avg >= 70:
        groups["C"].append(s["name"])
    elif avg >= 60:
        groups["D"].append(s["name"])
    else:
        groups["F"].append(s["name"])

print("  Grade groups:")
for grade, names in groups.items():
    if names:
        print(f"    {grade}: {names}")

# Exercise 5
data = [("a", 1), ("b", 2), ("c", 3)]

# To dict
d = dict(data)
print(f"\nExercise 5:")
print(f"  List of tuples: {data}")
print(f"  To dict: {d}")

# Back to list of tuples
back = list(d.items())
print(f"  Back to list: {back}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Lists: mutable, ordered, allow duplicates - [1, 2, 3]
2. Tuples: immutable, ordered, allow duplicates - (1, 2, 3)
3. Dictionaries: key-value, unique keys, O(1) lookup - {"a": 1}
4. Sets: unique, unordered, O(1) membership - {1, 2, 3}

Key methods:
- List: append, extend, insert, pop, remove, sort, reverse
- Tuple: count, index (immutable!)
- Dict: get, keys, values, items, pop, update
- Set: add, update, remove, discard, pop, union, intersection

Choosing guide:
- Need order + index? -> List
- Need immutability? -> Tuple
- Need key-value lookup? -> Dict
- Need uniqueness + membership? -> Set

Comprehensions work for all: [x for x], {x: x}, {x for x}
""")

print("\n✅ File 05 complete! Run 'python 06_modules_packages.py' next.")