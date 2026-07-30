"""
=============================================================================
FILE: 06_modules_packages.py
TOPIC: Modules and Packages - Importing, Creating, Best Practices
LEVEL: Intermediate
PREREQUISITES: 01-05 (basic Python concepts)
=============================================================================

This file covers Python modules and packages:
- What are modules and packages
- Import statements (import, from, as)
- Creating your own modules
- Package structure with __init__.py
- Standard library modules overview
- Virtual environments
- Best practices

Run this file: python 06_modules_packages.py
"""

# =============================================================================
# SECTION 1: UNDERSTANDING MODULES
# =============================================================================

print("=" * 60)
print("SECTION 1: UNDERSTANDING MODULES")
print("=" * 60)

print("""
A MODULE is a Python file (.py) containing:
- Functions
- Classes
- Variables
- Runnable code

A PACKAGE is a directory containing:
- Multiple modules
- An __init__.py file (can be empty)
- Subpackages

Benefits:
- Code organization and reusability
- Namespace management
- Collaboration (separate files)
- Standard library provides 200+ modules
""")

# Every .py file is a module
# This file is a module named "06_modules_packages"
print(f"This module's name: {__name__}")
print(f"This module's file: {__file__}")


# =============================================================================
# SECTION 2: IMPORT STATEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: IMPORT STATEMENTS")
print("=" * 60)

# 1. import module
import math
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")

# 2. import module as alias
import random as rnd
print(f"\nrnd.randint(1, 10) = {rnd.randint(1, 10)}")

# 3. from module import name
from datetime import datetime
now = datetime.now()
print(f"\nCurrent time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 4. from module import name as alias
from collections import Counter as Ctr
counts = Ctr("hello world")
print(f"\nCounter: {counts}")

# 5. from module import * (not recommended!)
# from math import *  # Pollutes namespace

# 6. Import specific functions
from os.path import join, exists, basename
print(f"\nPath operations:")
print(f"  join('home', 'user'): {join('home', 'user')}")
print(f"  basename('/home/user/file.txt'): {basename('/home/user/file.txt')}")


# =============================================================================
# SECTION 3: MODULE SEARCH PATH
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: MODULE SEARCH PATH (sys.path)")
print("=" * 60)

import sys
print("Python searches for modules in this order:")
for i, path in enumerate(sys.path):
    print(f"  {i}: {path}")

# Adding to path (temporary)
# sys.path.append('/custom/path')

# Adding to path (permanent) - use PYTHONPATH environment variable
# export PYTHONPATH=/custom/path:$PYTHONPATH


# =============================================================================
# SECTION 4: CREATING YOUR OWN MODULES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: CREATING YOUR OWN MODULES")
print("=" * 60)

print("""
To create a module:
1. Create a .py file (e.g., my_module.py)
2. Define functions, classes, variables
3. Import it in other files

Example my_module.py:
-------------------
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b

Usage:
------
import my_module
print(my_module.greet("Alice"))
print(my_module.PI)
calc = my_module.Calculator()
""")

# Let's create a simple module inline for demonstration
# (In practice, this would be a separate file)

# This demonstrates how __name__ works
print(f"\nCurrent module __name__: {__name__}")
print("When run directly: __name__ == '__main__'")
print("When imported: __name__ == 'module_name'")


# =============================================================================
# SECTION 5: PACKAGES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: PACKAGES")
print("=" * 60)

print("""
Package Structure:
------------------
my_package/
    __init__.py          # Makes it a package (can be empty)
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py

__init__.py can contain:
- Package initialization code
- Exports (__all__ = ['module1', 'module2'])
- Convenience imports
- Version info
""")

# Example package structure (conceptual)
# In real projects, this would be actual directories

# Simulating package imports
print("Package import examples:")
print("  import my_package")
print("  import my_package.module1")
print("  from my_package import module1")
print("  from my_package.module1 import my_function")
print("  from my_package.subpackage import module3")


# =============================================================================
# SECTION 6: __init__.py AND PACKAGE EXPORTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: __init__.py AND EXPORTS")
print("=" * 60)

print("""
__init__.py example:
--------------------
# my_package/__init__.py

# Make submodules available at package level
from .module1 import func1
from .module2 import ClassA

# Define public API
__all__ = ['func1', 'ClassA', 'module1', 'module2']

# Version
__version__ = '1.0.0'
""")

# Demonstrating __all__
print("Using __all__ to control 'from package import *':")
print("  __all__ = ['public_func', 'PublicClass']")
print("  Only names in __all__ are imported with *")


# =============================================================================
# SECTION 7: RELATIVE IMPORTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: RELATIVE IMPORTS")
print("=" * 60)

print("""
Relative imports (inside packages only):
----------------------------------------
from . import module           # Current package
from .module import func      # Sibling module
from .. import parent_module  # Parent package
from ..sibling import func    # Sibling package

Rules:
- Only work inside packages (not in scripts)
- Use dots: . = current, .. = parent, ... = grandparent
- Cannot go beyond top-level package
- Absolute imports preferred for clarity
""")


# =============================================================================
# SECTION 8: COMMON STANDARD LIBRARY MODULES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: COMMON STANDARD LIBRARY MODULES")
print("=" * 60)

# Let's demonstrate some commonly used modules

# 1. os - Operating system interface
import os
print("1. os module:")
print(f"  Current dir: {os.getcwd()}")
print(f"  Env var HOME: {os.environ.get('HOME', 'Not set')}")

# 2. sys - System-specific parameters
import sys
print(f"\n2. sys module:")
print(f"  Python version: {sys.version.split()[0]}")
print(f"  Platform: {sys.platform}")

# 3. pathlib - Object-oriented filesystem paths
from pathlib import Path
print(f"\n3. pathlib module:")
home = Path.home()
print(f"  Home: {home}")
print(f"  Name: {home.name}")
print(f"  Parent: {home.parent}")

# 4. json - JSON encoding/decoding
import json
print(f"\n4. json module:")
data = {"name": "Alice", "age": 25, "skills": ["Python", "SQL"]}
json_str = json.dumps(data, indent=2)
print(f"  To JSON:\n{json_str}")
parsed = json.loads(json_str)
print(f"  From JSON: {parsed}")

# 5. datetime - Date and time
from datetime import datetime, date, timedelta
print(f"\n5. datetime module:")
now = datetime.now()
print(f"  Now: {now}")
print(f"  Today: {date.today()}")
print(f"  Tomorrow: {date.today() + timedelta(days=1)}")
print(f"  Formatted: {now.strftime('%Y-%m-%d %H:%M')}")

# 6. random - Random numbers
import random
print(f"\n6. random module:")
print(f"  random(): {random.random()}")
print(f"  randint(1,6): {random.randint(1, 6)}")
print(f"  choice: {random.choice(['rock', 'paper', 'scissors'])}")
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"  shuffle: {items}")

# 7. collections - Specialized container datatypes
from collections import Counter, defaultdict, namedtuple, deque
print(f"\n7. collections module:")
# Counter
cnt = Counter("abracadabra")
print(f"  Counter: {cnt.most_common(3)}")
# defaultdict
dd = defaultdict(list)
dd['fruits'].append('apple')
print(f"  defaultdict: {dict(dd)}")
# namedtuple
Point = namedtuple('Point', 'x y')
p = Point(1, 2)
print(f"  namedtuple: {p.x}, {p.y}")
# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"  deque: {list(dq)}")

# 8. itertools - Iterator tools
import itertools
print(f"\n8. itertools module:")
print(f"  count: {list(itertools.islice(itertools.count(10, 2), 5))}")
print(f"  cycle: {list(itertools.islice(itertools.cycle('AB'), 6))}")
print(f"  combinations: {list(itertools.combinations('ABCD', 2))}")

# 9. functools - Higher-order functions
from functools import lru_cache, reduce, partial
print(f"\n9. functools module:")
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(f"  fib(10) with lru_cache: {fib(10)}")

# partial
def power(base, exp):
    return base ** exp
square = partial(power, exp=2)
cube = partial(power, exp=3)
print(f"  partial square(5): {square(5)}")
print(f"  partial cube(3): {cube(3)}")

# 10. typing - Type hints
from typing import List, Dict, Optional, Union
print(f"\n10. typing module:")
def process(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}
print(f"  Type hints example: {process(['a', 'bb', 'ccc'])}")


# =============================================================================
# SECTION 9: VIRTUAL ENVIRONMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: VIRTUAL ENVIRONMENTS")
print("=" * 60)

print("""
Why Virtual Environments?
-------------------------
- Isolate project dependencies
- Different projects, different package versions
- Avoid conflicts with system Python
- Reproducible environments

Creating:
---------
python -m venv venv          # Create venv in 'venv' folder
source venv/bin/activate     # Linux/Mac
venv\\Scripts\\activate      # Windows

Managing Packages:
------------------
pip install package          # Install
pip install package==1.0.0   # Specific version
pip freeze > requirements.txt # Save dependencies
pip install -r requirements.txt # Install from file

Deactivating:
-------------
deactivate
""")


# =============================================================================
# SECTION 10: PIP AND PACKAGE MANAGEMENT
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: PIP AND PACKAGE MANAGEMENT")
print("=" * 60)

print("""
Common pip Commands:
--------------------
pip install package              # Latest version
pip install package==2.0.0       # Specific version
pip install package>=1.0,<3.0    # Version range
pip install -r requirements.txt  # From file
pip uninstall package            # Remove package
pip list                         # List installed
pip show package                 # Package details
pip search query                 # Search PyPI (deprecated)
pip install --upgrade package    # Upgrade
pip install --upgrade pip        # Upgrade pip itself

requirements.txt example:
-------------------------
requests==2.31.0
numpy>=1.24.0,<2.0.0
pandas~=1.5.0          # Compatible release (>=1.5,<1.6)
flask

Setup.py / pyproject.toml (for distributing packages):
-----------------------------------------------------
# pyproject.toml (modern)
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "1.0.0"
description = "My awesome package"
dependencies = ["requests>=2.31.0"]
""")


# =============================================================================
# SECTION 11: BEST PRACTICES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 11: BEST PRACTICES")
print("=" * 60)

print("""
Import Best Practices:
----------------------
✓ Import at top of file
✓ Use absolute imports
✓ Group imports: standard, third-party, local
✓ One import per line (or grouped by module)
✓ Avoid wildcard imports (from x import *)
✓ Use 'import module' for clarity, 'from module import name' for brevity

File Organization:
------------------
project/
    src/
        my_package/
            __init__.py
            core.py
            utils.py
    tests/
        test_core.py
    requirements.txt
    README.md
    pyproject.toml

Naming Conventions:
-------------------
- Modules: lowercase, underscores (my_module.py)
- Packages: lowercase, short (my_package)
- Classes: CapWords (MyClass)
- Functions: snake_case (my_function)
- Constants: UPPER_SNAKE_CASE (MAX_SIZE)

Module Design:
--------------
- Single responsibility
- Clear public API (__all__)
- Minimize side effects on import
- Document with docstrings
- Handle circular imports carefully
""")


# =============================================================================
# SECTION 12: PRACTICAL EXAMPLE - CREATING A SIMPLE PACKAGE
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 12: PRACTICAL EXAMPLE")
print("=" * 60)

print("""
Let's create a simple package structure:

my_calculator/
    __init__.py
    basic.py
    advanced.py
    constants.py

__init__.py:
------------
from .basic import add, subtract
from .advanced import multiply, divide
from .constants import PI

__all__ = ['add', 'subtract', 'multiply', 'divide', 'PI']

basic.py:
---------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

advanced.py:
------------
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

constants.py:
-------------
PI = 3.14159265359

Usage:
------
from my_calculator import add, multiply, PI
result = add(5, 3) * multiply(2, 4)
""")

# Simulating the package inline
PI = 3.14159265359

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print("Testing our inline 'package':")
print(f"  PI = {PI}")
print(f"  add(10, 5) = {add(10, 5)}")
print(f"  subtract(10, 5) = {subtract(10, 5)}")
print(f"  multiply(10, 5) = {multiply(10, 5)}")
print(f"  divide(10, 5) = {divide(10, 5)}")


# =============================================================================
# SECTION 13: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 13: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Create a Module
---------------------------
Create a file math_utils.py with:
- function factorial(n)
- function is_prime(n)
- function gcd(a, b)
- constant GOLDEN_RATIO = 1.618033988749895
Import and use it

EXERCISE 2: Package Structure
-----------------------------
Create a package 'geometry' with:
- shapes/
    __init__.py
    circle.py (area, circumference)
    rectangle.py (area, perimeter)
- __init__.py (export all)
Use the package

EXERCISE 3: Using Standard Library
----------------------------------
Write a script that:
- Reads a JSON config file
- Logs to a file using logging module
- Uses pathlib for file paths
- Uses datetime for timestamps

EXERCISE 4: Virtual Environment
-------------------------------
Create a venv, install requests, write a script that
fetches a webpage, save requirements.txt

EXERCISE 5: Publishable Package
-------------------------------
Create a minimal pyproject.toml for a package with:
- Name, version, description
- Dependencies
- Entry point (console script)
""")

# Exercise Solutions (simulated)
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
print("\nExercise 1 - math_utils module (inline):")
GOLDEN_RATIO = 1.618033988749895

def factorial(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(f"  GOLDEN_RATIO = {GOLDEN_RATIO}")
print(f"  factorial(5) = {factorial(5)}")
print(f"  is_prime(17) = {is_prime(17)}")
print(f"  is_prime(18) = {is_prime(18)}")
print(f"  gcd(48, 18) = {gcd(48, 18)}")

# Exercise 2
print("\nExercise 2 - geometry package (inline):")

def circle_area(r):
    return PI * r * r

def circle_circumference(r):
    return 2 * PI * r

def rectangle_area(w, h):
    return w * h

def rectangle_perimeter(w, h):
    return 2 * (w + h)

print(f"  Circle area (r=5): {circle_area(5):.2f}")
print(f"  Circle circumference (r=5): {circle_circumference(5):.2f}")
print(f"  Rectangle area (3x4): {rectangle_area(3, 4)}")
print(f"  Rectangle perimeter (3x4): {rectangle_perimeter(3, 4)}")

# Exercise 3
print("\nExercise 3 - Standard library usage (demo):")
import json
from pathlib import Path
from datetime import datetime
import tempfile

# Create temp JSON config
config = {"app_name": "DemoApp", "version": "1.0", "debug": True}
with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
    json.dump(config, f, indent=2)
    config_path = f.name

print(f"  Created config: {config_path}")

# Read with pathlib
path = Path(config_path)
content = path.read_text()
parsed = json.loads(content)
print(f"  Read config: {parsed}")

# Cleanup
path.unlink()
print(f"  Cleaned up temp file")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Module = .py file; Package = directory with __init__.py
2. Import styles: import, from ... import, import ... as
3. sys.path determines where Python looks for modules
4. Create modules by saving .py files
5. Create packages with directories + __init__.py
6. Use __all__ in __init__.py to control public API
7. Relative imports (.) only work inside packages
8. Standard library has 200+ modules (os, sys, json, datetime, etc.)
9. Virtual environments isolate dependencies
10. pip manages packages; requirements.txt pins versions
11. Best practices: absolute imports, organize by type, document
12. pyproject.toml for modern package configuration
""")

print("\n✅ File 06 complete! Run 'python 07_file_io.py' next.")