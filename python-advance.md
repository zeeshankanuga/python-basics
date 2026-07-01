# Python Advanced Concepts

## Advanced Data Structures

### Named Tuples
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x, p.y  # 1, 2
p[0], p[1]  # 1, 2

# Typed named tuples (Python 3.6+)
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int
    label: str = "origin"

p = Point(1, 2, "start")
```

### Data Classes (Python 3.7+)
```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int
    skills: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

# With options
@dataclass(order=True, frozen=True)
class ImmutablePoint:
    x: int
    y: int
```

### Collections Module
```python
from collections import Counter, defaultdict, OrderedDict, ChainMap, deque

# Counter
cnt = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})
cnt.most_common(2)  # [('a', 3), ('b', 2)]

# defaultdict
dd = defaultdict(list)
dd['key'].append(1)  # No KeyError

# OrderedDict (preserves insertion order, Python 3.7+ dict does too)
od = OrderedDict([('a', 1), ('b', 2)])

# ChainMap (multiple dicts as one)
d1 = {'a': 1}
d2 = {'b': 2}
cm = ChainMap(d1, d2)
cm['a']  # 1
cm['b']  # 2

# deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
dq.popleft()
```

---

## Iterators and Generators

### Iterators
```python
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in CountDown(3):
    print(num)  # 3, 2, 1
```

### Generators
```python
# Generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

list(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator expression
squares = (x**2 for x in range(10))

# Send values to generator
def counter():
    count = 0
    while True:
        val = yield count
        if val is not None:
            count = val
        else:
            count += 1

gen = counter()
next(gen)        # 0
next(gen)        # 1
gen.send(10)     # 10
next(gen)        # 11

# yield from
def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()
    yield 3

list(gen2())  # [1, 2, 3]
```

### itertools
```python
import itertools

# Infinite iterators
itertools.count(10, 2)      # 10, 12, 14, ...
itertools.cycle([1, 2, 3])  # 1, 2, 3, 1, 2, 3, ...
itertools.repeat(5, 3)      # 5, 5, 5

# Finite iterators
list(itertools.accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]
list(itertools.chain([1, 2], [3, 4]))     # [1, 2, 3, 4]
list(itertools.compress('ABCDEF', [1,0,1,0,1,1]))  # ['A', 'C', 'E', 'F']
list(itertools.dropwhile(lambda x: x < 5, [1,4,6,3,8]))  # [6, 3, 8]
list(itertools.takewhile(lambda x: x < 5, [1,4,6,3,8]))  # [1, 4]

# Combinatorics
list(itertools.product('AB', repeat=2))   # [('A','A'), ('A','B'), ('B','A'), ('B','B')]
list(itertools.permutations('ABC', 2))    # [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]
list(itertools.combinations('ABC', 2))    # [('A','B'), ('A','C'), ('B','C')]
list(itertools.combinations_with_replacement('ABC', 2))  # [('A','A'), ('A','B'), ('A','C'), ('B','B'), ('B','C'), ('C','C')]
```

---

## Decorators

### Basic Decorators
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before function
# Hello!
# After function
```

### Decorators with Arguments
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints 3 times
```

### Class-based Decorators
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()  # Call 1, Hi!
say_hi()  # Call 2, Hi!
```

### Useful Built-in Decorators
```python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@functools.singledispatch
def process(arg):
    print(f"Default: {arg}")

@process.register(int)
def _(arg):
    print(f"Integer: {arg}")

@process.register(str)
def _(arg):
    print(f"String: {arg}")

# property, classmethod, staticmethod
class Example:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, v):
        if v < 0:
            raise ValueError("Must be positive")
        self._value = v
    
    @classmethod
    def from_string(cls, s):
        return cls(int(s))
    
    @staticmethod
    def validate(v):
        return v > 0
```

---

## Context Managers

### Class-based
```python
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.host}")
        self.connection = "connected"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        self.connection = None
        return False  # Don't suppress exceptions

with DatabaseConnection("localhost") as db:
    print("Using database")
```

### Contextlib
```python
from contextlib import contextmanager, closing, suppress, redirect_stdout
import io

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        print(f"Elapsed: {time.time() - start:.4f}s")

with timer():
    sum(range(1000000))

# Suppress exceptions
with suppress(FileNotFoundError):
    open('nonexistent.txt')

# Redirect stdout
buf = io.StringIO()
with redirect_stdout(buf):
    print("Hello")
print(buf.getvalue())  # "Hello\n"
```

---

## Metaclasses

### Basic Metaclass
```python
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Creating class {name}")
        return super().__new__(mcs, name, bases, namespace)
    
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.created = True

class MyClass(metaclass=Meta):
    pass

# MyClass.created == True
```

### Singleton Pattern
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connected = False

db1 = Database()
db2 = Database()
db1 is db2  # True
```

### Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return f"Area: {self.area()}, Perimeter: {self.perimeter()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Circle()  # TypeError: Can't instantiate abstract class
c = Circle(5)
c.describe()  # "Area: 78.53975, Perimeter: 31.4159"
```

---

## Concurrency and Parallelism

### Threading
```python
import threading
import time

def worker(name, delay):
    print(f"{name} starting")
    time.sleep(delay)
    print(f"{name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}", 1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All done")

# Thread-safe counter
import threading
class Counter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    @property
    def value(self):
        with self._lock:
            return self._value
```

### Multiprocessing
```python
from multiprocessing import Process, Pool, Queue, Value, Array
import os

def worker(num):
    return num * num

if __name__ == '__main__':
    with Pool(4) as pool:
        results = pool.map(worker, range(10))
    print(results)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Shared memory
counter = Value('i', 0)
def increment(counter):
    for _ in range(1000):
        with counter.get_lock():
            counter.value += 1
```

### Asyncio (Python 3.4+)
```python
import asyncio

async def fetch_data(name, delay):
    print(f"{name} starting")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return f"Data from {name}"

async def main():
    # Sequential
    result1 = await fetch_data("Task 1", 1)
    result2 = await fetch_data("Task 2", 1)
    
    # Concurrent
    task1 = asyncio.create_task(fetch_data("Task 1", 1))
    task2 = asyncio.create_task(fetch_data("Task 2", 1))
    result1 = await task1
    result2 = await task2
    
    # gather
    results = await asyncio.gather(
        fetch_data("Task 1", 1),
        fetch_data("Task 2", 1),
        fetch_data("Task 3", 1)
    )
    
    return results

asyncio.run(main())
```

### Async Context Managers
```python
class AsyncDB:
    async def __aenter__(self):
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

async with AsyncDB() as db:
    await db.query("SELECT * FROM users")
```

---

## Advanced Function Concepts

### Partial Functions
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

square(5)  # 25
cube(3)    # 27
```

### Function Composition
```python
from functools import reduce

def compose(*funcs):
    return lambda x: reduce(lambda v, f: f(v), funcs, x)

add_one = lambda x: x + 1
double = lambda x: x * 2
add_one_then_double = compose(double, add_one)
add_one_then_double(5)  # 12
```

### Currying
```python
def curry(func):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *a, **kw: curried(*(args + a), **{**kwargs, **kw})
    return curried

@curry
def add(a, b, c):
    return a + b + c

add(1)(2)(3)      # 6
add(1, 2)(3)      # 6
add(1)(2, 3)      # 6
```

---

## Type System Advanced

### Generics
```python
from typing import Generic, TypeVar, List, Dict

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def peek(self) -> T:
        return self._items[-1]

int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
```

### Protocols (Structural Typing)
```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "Drawing circle"

class Square:
    def draw(self) -> str:
        return "Drawing square"

def render(obj: Drawable) -> None:
    print(obj.draw())

render(Circle())  # OK
render(Square())  # OK
```

### TypedDict
```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str

user: User = {"name": "Alice", "age": 30, "email": "alice@example.com"}
```

### Literal Types
```python
from typing import Literal

Direction = Literal["north", "south", "east", "west"]

def move(direction: Direction) -> None:
    print(f"Moving {direction}")

move("north")  # OK
# move("up")   # Type error
```

---

## Memory Management

### Garbage Collection
```python
import gc

# Reference counting (primary)
import sys
sys.getrefcount([])  # Includes temporary reference

# Manual GC control
gc.collect()           # Force collection
gc.disable()           # Disable automatic
gc.enable()            # Enable automatic
gc.get_threshold()     # Collection thresholds
gc.set_threshold(700, 10, 10)  # Set thresholds
```

### Weak References
```python
import weakref

class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    
    def get(self, key):
        return self._cache.get(key)
    
    def set(self, key, value):
        self._cache[key] = value

cache = Cache()
class Data:
    def __init__(self, value):
        self.value = value

data = Data(42)
cache.set("key", data)
cache.get("key")  # Data object
del data
cache.get("key")  # None (garbage collected)
```

### __slots__
```python
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
sys.getsizeof(WithoutSlots(1, 2))  # Larger (has __dict__)
sys.getsizeof(WithSlots(1, 2))     # Smaller (no __dict__)
```

---

## Testing

### unittest
```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5
    
    def tearDown(self):
        pass
    
    def test_add(self):
        self.assertEqual(self.a + self.b, 15)
    
    def test_subtract(self):
        self.assertEqual(self.a - self.b, 5)
    
    @unittest.skip("Not implemented")
    def test_multiply(self):
        pass

if __name__ == '__main__':
    unittest.main()
```

### pytest
```python
# test_example.py
import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

# Run: pytest test_example.py -v
```

### Mocking
```python
from unittest.mock import Mock, patch, MagicMock

# Simple mock
mock = Mock(return_value=42)
mock()  # 42

# Patch
with patch('module.ClassName') as mock_class:
    mock_class.return_value.method.return_value = "mocked"
    # Test code using module.ClassName

# Mock side effects
mock = Mock(side_effect=[1, 2, 3])
mock()  # 1
mock()  # 2
mock()  # 3
```

---

## Performance Optimization

### Profiling
```python
import cProfile
import pstats

def slow_function():
    return sum(i**2 for i in range(100000))

# Profile
profiler = cProfile.Profile()
profiler.enable()
slow_function()
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)

# Or use: python -m cProfile -o profile.stats script.py
# Then: python -m pstats profile.stats
```

### Timeit
```python
import timeit

# Time a snippet
timeit.timeit("sum(range(100))", number=10000)

# Time a function
def func():
    return sum(range(100))

timeit.timeit(func, number=10000)

# Compare
timeit.timeit("[x**2 for x in range(100)]", number=10000)
timeit.timeit("list(map(lambda x: x**2, range(100)))", number=10000)
```

### Optimization Tips
```python
# Use local variables
def slow():
    result = []
    for i in range(10000):
        result.append(i * 2)
    return result

def fast():
    result = []
    append = result.append  # Local reference
    for i in range(10000):
        append(i * 2)
    return result

# Use built-ins
sum(range(n))           # Faster than loop
max(items)              # Faster than manual
any(x > 0 for x in items)  # Short-circuits
all(x > 0 for x in items)  # Short-circuits

# Use sets for membership
# Slow: item in large_list
# Fast: item in large_set

# String joining
# Slow: s += "a" in loop
# Fast: "".join(list_of_strings)
```

---

## Packaging and Distribution

### Project Structure
```
my_package/
├── pyproject.toml
├── setup.py (legacy)
├── README.md
├── LICENSE
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── module1.py
│       └── subpackage/
│           ├── __init__.py
│           └── module2.py
└── tests/
    ├── test_module1.py
    └── test_module2.py
```

### pyproject.toml (Modern)
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
version = "0.1.0"
description = "A sample package"
readme = "README.md"
license = {text = "MIT"}
authors = [{name = "Your Name", email = "you@example.com"}]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dependencies = [
    "requests>=2.28.0",
]

[project.optional-dependencies]
dev = ["pytest", "black", "mypy"]

[tool.setuptools.packages.find]
where = ["src"]
```

### Building and Publishing
```bash
# Build
pip install build
python -m build

# Check
twine check dist/*

# Publish to TestPyPI
twine upload --repository testpypi dist/*

# Publish to PyPI
twine upload dist/*
```

---

## Advanced Patterns

### Dependency Injection
```python
from abc import ABC, abstractmethod
from typing import Protocol

class Database(Protocol):
    def query(self, sql: str) -> list: ...

class PostgresDB:
    def query(self, sql: str) -> list:
        return []

class MySQLDB:
    def query(self, sql: str) -> list:
        return []

class UserService:
    def __init__(self, db: Database):
        self.db = db
    
    def get_users(self):
        return self.db.query("SELECT * FROM users")

# Usage
service = UserService(PostgresDB())
# or
service = UserService(MySQLDB())
```

### Observer Pattern
```python
from typing import Callable, List

class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, List[Callable]] = {}
    
    def on(self, event: str, callback: Callable):
        self._listeners.setdefault(event, []).append(callback)
    
    def emit(self, event: str, *args, **kwargs):
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)
    
    def off(self, event: str, callback: Callable):
        if event in self._listeners:
            self._listeners[event].remove(callback)

emitter = EventEmitter()
emitter.on("user_created", lambda user: print(f"Welcome {user}"))
emitter.emit("user_created", "Alice")
```

### Strategy Pattern
```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

class QuickSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data)

class BubbleSort(SortStrategy):
    def sort(self, data: list) -> list:
        # Implementation
        return sorted(data)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy
    
    def sort(self, data: list) -> list:
        return self._strategy.sort(data)
```

---

## Security Best Practices

### Input Validation
```python
import re
from typing import Optional

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def sanitize_input(text: str, max_length: int = 1000) -> str:
    # Remove null bytes
    text = text.replace('\x00', '')
    # Truncate
    return text[:max_length]
```

### Secure Secrets
```python
import os
from pathlib import Path

# Environment variables
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not set")

# .env file (use python-dotenv)
from dotenv import load_dotenv
load_dotenv()  # Loads .env file
```

### SQL Injection Prevention
```python
import sqlite3

# BAD
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")

# GOOD - Parameterized queries
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

---

## Debugging and Logging

### Logging
```python
import logging

# Configure
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.debug("Debug info")
logger.info("General info")
logger.warning("Warning")
logger.error("Error occurred")
logger.exception("Exception with traceback")

# Structured logging
logger.info("User logged in", extra={"user_id": 123, "ip": "192.168.1.1"})
```

### Debugging with pdb
```python
import pdb

def buggy_function(x, y):
    pdb.set_trace()  # Breakpoint
    result = x / y
    return result

# Or run: python -m pdb script.py
# Commands: n(next), s(step), c(continue), p(print), q(quit)
```

### Breakpoint (Python 3.7+)
```python
def func():
    breakpoint()  # Built-in, uses PYTHONBREAKPOINT env var
    return 42
```

---

## Useful Third-Party Libraries

| Category | Libraries |
|----------|-----------|
| Web Frameworks | FastAPI, Flask, Django, Starlette |
| Data Science | NumPy, Pandas, Polars, SciPy |
| Visualization | Matplotlib, Seaborn, Plotly, Altair |
| Database | SQLAlchemy, Tortoise ORM, Prisma |
| Testing | pytest, hypothesis, factory-boy |
| Type Checking | mypy, pyright, pydantic |
| Code Quality | black, ruff, isort, pre-commit |
| Async | aiohttp, httpx, asyncpg |
| Config | pydantic-settings, dynaconf |
| CLI | typer, click, rich |
| Serialization | msgspec, orjson, pydantic |

---

## Python Internals (CPython)

### Bytecode
```python
import dis

def hello():
    x = 1
    y = 2
    return x + y

dis.dis(hello)
# Shows bytecode instructions
```

### Memory Layout
```python
import sys

# Object headers
# PyObject_HEAD: refcount + type pointer
# Variable-sized objects have PyVarObject_HEAD

sys.getsizeof(0)        # 24 bytes (int)
sys.getsizeof("")       # 49 bytes (str)
sys.getsizeof([])       # 56 bytes (list)
sys.getsizeof({})       # 64 bytes (dict)
```

### GIL (Global Interpreter Lock)
```python
# GIL allows only one thread to execute Python bytecode
# CPU-bound tasks: use multiprocessing
# I/O-bound tasks: threading works fine (GIL released during I/O)

# Check GIL status
import sys
sys.getswitchinterval()  # Thread switch interval
```

---

## Modern Python Features (3.10+)

### Pattern Matching (3.10+)
```python
def handle_command(command: str):
    match command.split():
        case ["quit"]:
            print("Goodbye!")
        case ["load", filename]:
            print(f"Loading {filename}")
        case ["save", filename, *rest]:
            print(f"Saving {filename} with options {rest}")
        case ["reset", "--hard"] | ["reset", "-f"]:
            print("Hard reset")
        case _:
            print(f"Unknown command: {command}")

handle_command("load file.txt")
handle_command("save file.txt --force")
handle_command("reset --hard")
```

### Union Types (3.10+)
```python
# Old
from typing import Union
def func(x: Union[int, str]) -> Union[int, str]: ...

# New
def func(x: int | str) -> int | str: ...

# Type aliases
type UserID = int | str
type JSON = dict | list | str | int | float | bool | None
```

### Exception Groups (3.11+)
```python
try:
    raise ExceptionGroup("Multiple errors", [
        ValueError("Bad value"),
        TypeError("Wrong type"),
        KeyError("Missing key")
    ])
except* ValueError as eg:
    print(f"Value errors: {eg.exceptions}")
except* TypeError as eg:
    print(f"Type errors: {eg.exceptions}")
```

### Self Type (3.11+)
```python
from typing import Self

class Builder:
    def __init__(self):
        self.value = 0
    
    def set_value(self, v: int) -> Self:
        self.value = v
        return self
    
    def build(self) -> Self:
        return self

Builder().set_value(5).build()
```

### Dataclass Transforms (3.11+)
```python
from typing import dataclass_transform

@dataclass_transform()
def create_model(cls):
    return dataclass(cls)

@create_model
class User:
    name: str
    age: int
```

---

## Quick Reference: Advanced Cheatsheet

| Concept | Syntax/Module |
|---------|---------------|
| Generator | `yield` / `(x for x in ...)` |
| Decorator | `@decorator` / `functools.wraps` |
| Context Manager | `with` / `contextlib` |
| Metaclass | `class Foo(metaclass=Meta)` |
| Abstract Base Class | `abc.ABC`, `@abstractmethod` |
| Type Variables | `TypeVar('T')`, `Generic[T]` |
| Protocol | `class Proto(Protocol)` |
| Async/Await | `async def`, `await`, `asyncio` |
| Pattern Matching | `match x: case ...` |
| Union Types | `int \| str` |
| Exception Groups | `except* Type` |
| Self Type | `Self` |
| Dataclass | `@dataclass` |
| Slots | `__slots__ = [...]` |
| Weak Ref | `weakref.ref(obj)` |

---

## Resources for Further Learning

### Official Documentation
- [Python Docs](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Library Reference](https://docs.python.org/3/library/)

### Books
- "Fluent Python" by Luciano Ramalho
- "Effective Python" by Brett Slatkin
- "Python Cookbook" by David Beazley & Brian Jones
- "High Performance Python" by Micha Gorelick & Ian Ozsvald

### Tools
- **Type Checkers**: mypy, pyright, pytype
- **Formatters**: black, ruff
- **Linters**: ruff, flake8, pylint
- **Testing**: pytest, hypothesis
- **Profiling**: cProfile, py-spy, snakeviz

### Practice
- LeetCode / HackerRank / Codewars
- Advent of Code
- Real Python tutorials
- Python Weekly newsletter



---

## 👩‍💻 Author

**Zeeshan kanuga** — Technical Architect |DevOps Engineer | Platform Engineering | AI-Augmented DevOps

Built by [Zeeshan Kanuga](https://github.com/zeeshankanuga)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zeeshankanuga/)

---

**Happy Learning!**