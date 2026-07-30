"""
=============================================================================
FILE: 10_stdlib_overview.py
TOPIC: Standard Library Overview - Commonly Used Modules
LEVEL: Intermediate
PREREQUISITES: 01-09 (all previous concepts)
=============================================================================

This file provides an overview of commonly used Python standard library modules:
- os, sys, pathlib - System and file operations
- datetime, time - Date and time handling
- json, csv, xml - Data serialization
- random, secrets - Random number generation
- collections, itertools, functools - Advanced data structures
- re - Regular expressions
- math, statistics, decimal - Mathematical operations
- typing - Type hints
- logging - Application logging
- argparse - Command-line argument parsing
- subprocess - Running external commands
- threading, multiprocessing - Concurrency
- unittest - Testing

Run this file: python 10_stdlib_overview.py
"""

# =============================================================================
# SECTION 1: SYSTEM AND FILE OPERATIONS
# =============================================================================

print("=" * 60)
print("SECTION 1: SYSTEM AND FILE OPERATIONS")
print("=" * 60)

import os
import sys
from pathlib import Path

# os - Operating system interface
print("1.1 os module:")
print(f"  Current dir: {os.getcwd()}")
print(f"  User home: {os.path.expanduser('~')}")
print(f"  Env var PATH: {os.environ.get('PATH', '')[:50]}...")

# pathlib - Object-oriented paths
print("\n1.2 pathlib module:")
home = Path.home()
config_dir = home / ".config" / "myapp"
print(f"  Home: {home}")
print(f"  Config dir: {config_dir}")
print(f"  Name: {config_dir.name}")
print(f"  Parent: {config_dir.parent}")

# sys - System-specific parameters
print("\n1.3 sys module:")
print(f"  Python version: {sys.version.split()[0]}")
print(f"  Platform: {sys.platform}")
print(f"  Args: {sys.argv}")
print(f"  Path entries: {len(sys.path)}")


# =============================================================================
# SECTION 2: DATE AND TIME
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: DATE AND TIME")
print("=" * 60)

from datetime import datetime, date, time, timedelta, timezone

print("2.1 datetime module:")
now = datetime.now()
print(f"  Now: {now}")
print(f"  Today: {date.today()}")
print(f"  Time: {now.time()}")

# Formatting
print(f"  ISO format: {now.isoformat()}")
print(f"  Custom: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Parsing
parsed = datetime.strptime("2024-01-15 10:30:00", "%Y-%m-%d %H:%M:%S")
print(f"  Parsed: {parsed}")

# Arithmetic
print(f"\n2.2 Time arithmetic:")
print(f"  Tomorrow: {date.today() + timedelta(days=1)}")
print(f"  In 2 hours: {now + timedelta(hours=2)}")
print(f"  Difference: {datetime(2024, 12, 31) - datetime(2024, 1, 1)}")

# Timezones
print(f"\n2.3 Timezones:")
utc_now = datetime.now(timezone.utc)
print(f"  UTC: {utc_now}")
est = timezone(timedelta(hours=-5))
est_now = datetime.now(est)
print(f"  EST: {est_now}")

# time module
import time
print(f"\n2.4 time module:")
print(f"  Time since epoch: {time.time()}")
print(f"  Sleep demo (0.1s): ", end="", flush=True)
time.sleep(0.1)
print("done")


# =============================================================================
# SECTION 3: DATA SERIALIZATION
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: DATA SERIALIZATION")
print("=" * 60)

import json
import csv
import xml.etree.ElementTree as ET

# JSON
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL", "AWS"],
    "active": True,
    "metadata": {"created": "2024-01-01"}
}

print("3.1 JSON:")
json_str = json.dumps(data, indent=2)
print(f"  Serialized:\n{json_str}")
loaded = json.loads(json_str)
print(f"  Deserialized: {loaded['name']}")

# CSV
print("\n3.2 CSV:")
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"],
]

import tempfile
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
    temp_csv = f.name

with open(temp_csv, 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row}")

import os
os.unlink(temp_csv)

# XML
print("\n3.3 XML:")
root = ET.Element("users")
for user_data in [("Alice", 25), ("Bob", 30)]:
    user = ET.SubElement(root, "user")
    ET.SubElement(user, "name").text = user_data[0]
    ET.SubElement(user, "age").text = str(user_data[1])

xml_str = ET.tostring(root, encoding='unicode')
print(f"  XML: {xml_str}")

# Parse XML
parsed_root = ET.fromstring(xml_str)
for user in parsed_root.findall("user"):
    print(f"  User: {user.find('name').text}, {user.find('age').text}")


# =============================================================================
# SECTION 4: RANDOM AND SECRETS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: RANDOM AND SECRETS")
print("=" * 60)

import random
import secrets

print("4.1 random module (pseudo-random):")
random.seed(42)  # Reproducible
print(f"  random(): {random.random()}")
print(f"  randint(1, 100): {random.randint(1, 100)}")
print(f"  choice: {random.choice(['red', 'green', 'blue'])}")
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"  shuffle: {items}")
print(f"  sample: {random.sample(range(100), 5)}")

print("\n4.2 secrets module (cryptographically secure):")
print(f"  token_hex(16): {secrets.token_hex(16)}")
print(f"  token_urlsafe(16): {secrets.token_urlsafe(16)}")
print(f"  randbelow(100): {secrets.randbelow(100)}")
print(f"  choice: {secrets.choice(['a', 'b', 'c'])}")

# UUID
import uuid
print(f"\n4.3 uuid module:")
print(f"  uuid4(): {uuid.uuid4()}")
print(f"  uuid1(): {uuid.uuid1()}")


# =============================================================================
# SECTION 5: COLLECTIONS, ITERTOOLS, FUNCTOOLS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: ADVANCED DATA STRUCTURES")
print("=" * 60)

from collections import Counter, defaultdict, OrderedDict, deque, namedtuple
from itertools import count, cycle, islice, combinations, permutations, product
from functools import lru_cache, reduce, partial, wraps

# Counter
print("5.1 Counter:")
text = "abracadabra"
cnt = Counter(text)
print(f"  Most common: {cnt.most_common(3)}")

# defaultdict
print("\n5.2 defaultdict:")
dd = defaultdict(list)
for key, value in [("a", 1), ("b", 2), ("a", 3)]:
    dd[key].append(value)
print(f"  {dict(dd)}")

# deque
print("\n5.3 deque:")
dq = deque([1, 2, 3], maxlen=5)
dq.appendleft(0)
dq.append(4)
dq.append(5)  # maxlen reached, removes leftmost
print(f"  {list(dq)}")

# namedtuple
print("\n5.4 namedtuple:")
Point = namedtuple("Point", "x y z")
p = Point(1, 2, 3)
print(f"  {p}, x={p.x}, y={p.y}")

# itertools
print("\n5.5 itertools:")
print(f"  count: {list(islice(count(10, 2), 5))}")
print(f"  cycle: {list(islice(cycle('AB'), 6))}")
print(f"  combinations: {list(combinations('ABCD', 2))}")
print(f"  permutations: {list(permutations('AB', 2))}")

# functools
print("\n5.6 functools:")

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(f"  fib(10) cached: {fib(10)}")

# partial
def power(base, exp):
    return base ** 2
square = partial(pow, exp=2)
cube = partial(pow, exp=3)
print(f"  partial square(5): {square(5)}")
print(f"  partial cube(3): {cube(3)}")

# reduce
print(f"  reduce sum: {reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])}")


# =============================================================================
# SECTION 6: REGULAR EXPRESSIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: REGULAR EXPRESSIONS")
print("=" * 60)

import re

text = "Contact: alice@example.com, bob@test.org, Phone: 555-123-4567"

print("6.1 Basic patterns:")
emails = re.findall(r'\b[\w.]+@[\w.]+\.\w+\b', text)
print(f"  Emails: {emails}")

phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(f"  Phones: {phones}")

# Substitution
cleaned = re.sub(r'\d', 'X', text)
print(f"  Masked: {cleaned}")

# Split
parts = re.split(r',\s*', text)
print(f"  Split: {parts}")

# Groups
match = re.search(r'(\w+)@(\w+\.\w+)', text)
if match:
    print(f"  Groups: {match.groups()}")
    print(f"  Full: {match.group(0)}")

# Compile for reuse
email_pattern = re.compile(r'\b[\w.]+@[\w.]+\.\w+\b')
print(f"  Compiled: {email_pattern.findall(text)}")


# =============================================================================
# SECTION 7: MATHEMATICAL OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: MATHEMATICAL OPERATIONS")
print("=" * 60)

import math
import statistics
from decimal import Decimal, getcontext
from fractions import Fraction

# math
print("7.1 math module:")
print(f"  pi: {math.pi}")
print(f"  sqrt(16): {math.sqrt(16)}")
print(f"  sin(pi/2): {math.sin(math.pi/2)}")
print(f"  log(100, 10): {math.log(100, 10)}")
print(f"  degrees(pi): {math.degrees(math.pi)}")

# statistics
print("\n7.2 statistics module:")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"  mean: {statistics.mean(data)}")
print(f"  median: {statistics.median(data)}")
print(f"  stdev: {statistics.stdev(data)}")
print(f"  variance: {statistics.variance(data)}")

# decimal - precise decimal arithmetic
print("\n7.3 decimal module:")
getcontext().prec = 28
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(f"  0.1 + 0.2 = {d1 + d2}")  # Exact!
print(f"  float: {0.1 + 0.2}")  # Inexact

# fractions
print("\n7.4 fractions module:")
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print(f"  1/3 + 1/6 = {f1 + f2}")
print(f"  as float: {float(f1 + f2)}")


# =============================================================================
# SECTION 8: TYPE HINTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: TYPE HINTS")
print("=" * 60)

from typing import List, Dict, Set, Tuple, Optional, Union, Callable, Any, TypeVar, Generic

print("8.1 Basic types:")
def process(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

result = process(["a", "bb", "ccc"])
print(f"  {result}")

print("\n8.2 Optional and Union:")
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(f"  find_user(1): {find_user(1)}")
print(f"  find_user(3): {find_user(3)}")

# Generic types
T = TypeVar('T')
def first_item(items: List[T]) -> Optional[T]:
    return items[0] if items else None

print(f"\n8.3 Generics:")
print(f"  first_item([1,2,3]): {first_item([1, 2, 3])}")
print(f"  first_item(['a','b']): {first_item(['a', 'b'])}")

# Callable
print("\n8.4 Callable:")
def apply_twice(func: Callable[[int], int], x: int) -> int:
    return func(func(x))

print(f"  apply_twice(lambda x: x*2, 3): {apply_twice(lambda x: x*2, 3)}")


# =============================================================================
# SECTION 9: LOGGING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: LOGGING")
print("=" * 60)

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

print("9.1 Basic logging:")
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

# Logging with exception
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Division by zero occurred")


# =============================================================================
# SECTION 10: COMMAND-LINE ARGUMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: COMMAND-LINE ARGUMENTS (argparse)")
print("=" * 60)

import argparse

print("10.1 argparse example:")
parser = argparse.ArgumentParser(description="Demo script")
parser.add_argument("input", help="Input file")
parser.add_argument("-o", "--output", help="Output file")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
parser.add_argument("--count", type=int, default=1, help="Count")

# Simulate parsing
args = parser.parse_args(["input.txt", "-o", "output.txt", "-v", "--count", "5"])
print(f"  input: {args.input}")
print(f"  output: {args.output}")
print(f"  verbose: {args.verbose}")
print(f"  count: {args.count}")


# =============================================================================
# SECTION 11: SUBPROCESS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 11: SUBPROCESS")
print("=" * 60)

import subprocess

print("11.1 Running commands:")
# Run command and capture output
result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)
print(f"  stdout: {result.stdout.strip()}")
print(f"  returncode: {result.returncode}")

# Run with input
result = subprocess.run(["cat"], input="test input", capture_output=True, text=True)
print(f"  cat echo: {result.stdout.strip()}")

# Run shell command
result = subprocess.run("echo $HOME", shell=True, capture_output=True, text=True)
print(f"  shell: {result.stdout.strip()}")


# =============================================================================
# SECTION 12: CONCURRENCY
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 12: CONCURRENCY")
print("=" * 60)

import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Threading
print("12.1 threading:")
results = []

def worker(n):
    time.sleep(0.1)
    results.append(n * 2)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"  Thread results: {results}")

# ThreadPoolExecutor
print("\n12.2 ThreadPoolExecutor:")
def square(n):
    time.sleep(0.05)
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(square, i) for i in range(5)]
    results = [f.result() for f in futures]
print(f"  Pool results: {results}")

# ProcessPoolExecutor (for CPU-bound tasks)
print("\n12.3 ProcessPoolExecutor:")
def cpu_task(n):
    return sum(i * i for i in range(n))

# Note: ProcessPoolExecutor requires if __name__ == '__main__' guard
# This is a limitation when running as a script directly
print("  (ProcessPoolExecutor demo skipped - requires __main__ guard)")
print("  In real usage, wrap in: if __name__ == '__main__':")
print("      with ProcessPoolExecutor(max_workers=2) as executor:")
print("          results = list(executor.map(cpu_task, [1000, 2000, 3000]))")


# =============================================================================
# SECTION 13: TESTING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 13: TESTING (unittest)")
print("=" * 60)

import unittest

# Test case
class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def test_division(self):
        self.assertAlmostEqual(10 / 3, 3.333, places=2)
    
    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
    
    @unittest.skip("Skipped for demo")
    def test_skipped(self):
        self.fail("Should not run")

# Run tests programmatically
suite = unittest.TestLoader().loadTestsFromTestCase(TestMath)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f"  Tests run: {result.testsRun}")
print(f"  Failures: {len(result.failures)}")
print(f"  Errors: {len(result.errors)}")
print(f"  Skipped: {len(result.skipped)}")


# =============================================================================
# SECTION 14: OTHER USEFUL MODULES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 14: OTHER USEFUL MODULES")
print("=" * 60)

# hashlib - Cryptographic hashes
import hashlib
print("14.1 hashlib:")
data = b"Hello, World!"
print(f"  SHA256: {hashlib.sha256(data).hexdigest()}")
print(f"  MD5: {hashlib.md5(data).hexdigest()}")

# base64 - Encoding
import base64
print("\n14.2 base64:")
encoded = base64.b64encode(b"Secret data")
print(f"  Encoded: {encoded}")
print(f"  Decoded: {base64.b64decode(encoded)}")

# urllib - URL handling
from urllib.parse import urlparse, urlencode, parse_qs
print("\n14.3 urllib.parse:")
url = "https://example.com/path?key=value&name=test"
parsed = urlparse(url)
print(f"  scheme: {parsed.scheme}")
print(f"  netloc: {parsed.netloc}")
print(f"  path: {parsed.path}")
print(f"  query: {parsed.query}")
print(f"  params: {parse_qs(parsed.query)}")

# textwrap - Text formatting
import textwrap
print("\n14.4 textwrap:")
long_text = "This is a very long text that needs to be wrapped to fit within a certain width for display purposes."
wrapped = textwrap.fill(long_text, width=40)
print(f"  Wrapped:\n{wrapped}")

# pprint - Pretty printing
import pprint
print("\n14.5 pprint:")
complex_data = {"a": [1, 2, {"nested": "value"}], "b": {"c": [3, 4]}}
pprint.pprint(complex_data, width=40)

# dataclasses (revisited)
from dataclasses import dataclass, asdict, astuple
print("\n14.6 dataclasses:")
@dataclass
class Config:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False

cfg = Config(host="0.0.0.0", port=3000)
print(f"  asdict: {asdict(cfg)}")
print(f"  astuple: {astuple(cfg)}")


# =============================================================================
# SECTION 15: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 15: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Log Parser
----------------------
Write a script that parses a log file using regex:
- Extract timestamps, log levels, messages
- Count occurrences of each level
- Filter by date range

EXERCISE 2: Configuration Loader
--------------------------------
Create a config loader that:
- Reads from JSON/YAML/TOML (use json, yaml, tomllib)
- Supports environment variable overrides
- Validates required fields

EXERCISE 3: File Organizer
--------------------------
Write a script that:
- Scans a directory recursively
- Groups files by extension
- Moves files to subdirectories by type
- Logs all operations

EXERCISE 4: Web Scraper with Rate Limiting
------------------------------------------
Create a scraper that:
- Uses urllib/requests to fetch pages
- Implements rate limiting with time.sleep
- Handles retries with exponential backoff
- Saves results to JSON

EXERCISE 5: Parallel Data Processor
-----------------------------------
Write a program that:
- Processes a large CSV file in chunks
- Uses ProcessPoolExecutor for CPU-bound work
- Aggregates results
- Shows progress with threading
""")

# Exercise Solutions
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
print("\nExercise 1 - Log Parser:")
log_data = """2024-01-15 10:30:00 INFO User logged in
2024-01-15 10:31:00 ERROR Database connection failed
2024-01-15 10:32:00 WARNING High memory usage
2024-01-15 10:33:00 INFO Data processed
2024-01-15 10:34:00 ERROR Timeout on request"""

import re
from collections import Counter

pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)')
levels = Counter()

for line in log_data.strip().split('\n'):
    match = pattern.match(line)
    if match:
        timestamp, level, message = match.groups()
        levels[level] += 1

print(f"  Log levels: {dict(levels)}")

# Exercise 2
print("\nExercise 2 - Config Loader:")
import json
import os

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}
    
    def load(self):
        with open(self.config_path) as f:
            self.config = json.load(f)
        
        # Override with env vars
        for key, value in self.config.items():
            env_key = f"APP_{key.upper()}"
            if env_key in os.environ:
                self.config[key] = os.environ[env_key]
    
    def get(self, key, default=None):
        return self.config.get(key, default)

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
    json.dump({"host": "localhost", "port": 8080, "debug": False}, f)
    config_file = f.name

loader = ConfigLoader(config_file)
loader.load()
print(f"  Loaded: {loader.config}")
os.unlink(config_file)

# Exercise 3
print("\nExercise 3 - File Organizer (simulated):")
from pathlib import Path

def organize_files(directory: Path):
    """Organize files by extension."""
    for file_path in directory.rglob("*"):
        if file_path.is_file():
            ext = file_path.suffix.lower().lstrip('.')
            if not ext:
                ext = 'no_extension'
            target_dir = directory / ext
            target_dir.mkdir(exist_ok=True)
            # In real implementation: file_path.rename(target_dir / file_path.name)
            print(f"  Would move: {file_path.name} -> {ext}/")

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    (tmpdir / "document.pdf").write_text("pdf")
    (tmpdir / "image.png").write_text("png")
    (tmpdir / "script.py").write_text("py")
    (tmpdir / "README").write_text("readme")
    organize_files(tmpdir)

# Exercise 4
print("\nExercise 4 - Rate Limited Scraper:")
import time

class RateLimitedScraper:
    def __init__(self, requests_per_second=2):
        self.min_interval = 1.0 / requests_per_second
        self.last_request = 0
    
    def fetch(self, url):
        # Rate limiting
        elapsed = time.time() - self.last_request
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        
        self.last_request = time.time()
        # In real implementation: return requests.get(url).text
        return f"Content from {url}"

scraper = RateLimitedScraper(requests_per_second=5)
start = time.time()
for i in range(3):
    print(f"  {scraper.fetch(f'http://example.com/page{i}')}")
print(f"  Time for 3 requests: {time.time() - start:.2f}s")

# Exercise 5
print("\nExercise 5 - Parallel Processor:")
from concurrent.futures import ThreadPoolExecutor

def process_chunk(chunk):
    """Simulate CPU-bound processing."""
    return sum(x * x for x in chunk)

data_chunks = [list(range(i, i + 1000)) for i in range(0, 5000, 1000)]

# Using ThreadPoolExecutor for demo (ProcessPoolExecutor requires __main__ guard)
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(process_chunk, data_chunks))

total = sum(results)
print(f"  Processed {len(data_chunks)} chunks")
print(f"  Total sum of squares: {total}")
print(f"  Note: For true CPU-bound work, use ProcessPoolExecutor with if __name__ == '__main__':")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
Python Standard Library - Key Modules:

SYSTEM & FILES:
- os, sys, pathlib - Paths, environment, system info
- shutil - High-level file operations
- tempfile - Temporary files/directories

DATE & TIME:
- datetime - Dates, times, timedeltas, timezones
- time - Time functions, sleep, benchmarks

DATA SERIALIZATION:
- json - JSON encoding/decoding
- csv - CSV reading/writing
- xml.etree.ElementTree - XML parsing
- pickle - Python object serialization (not secure!)

RANDOM & SECURITY:
- random - Pseudo-random numbers
- secrets - Cryptographically secure random
- uuid - Unique identifiers
- hashlib - Cryptographic hashes

ADVANCED DATA STRUCTURES:
- collections - Counter, defaultdict, deque, namedtuple
- itertools - Iterator tools (count, cycle, combinations)
- functools - Higher-order functions (lru_cache, partial)

TEXT PROCESSING:
- re - Regular expressions
- string - String constants and templates
- textwrap - Text wrapping/formatting

MATH:
- math - Mathematical functions
- statistics - Statistical functions
- decimal - Precise decimal arithmetic
- fractions - Rational numbers

TYPING & DEBUGGING:
- typing - Type hints
- logging - Application logging
- pprint - Pretty printing
- traceback - Exception tracebacks

CONCURRENCY:
- threading - Thread-based parallelism
- multiprocessing - Process-based parallelism
- concurrent.futures - High-level executor interface
- asyncio - Asynchronous I/O (separate module)

TESTING & CLI:
- unittest - Unit testing framework
- argparse - Command-line argument parsing
- subprocess - Running external commands

NETWORKING:
- urllib - URL handling
- http.client - HTTP client
- socket - Low-level networking

Remember: "Batteries included" - check stdlib before adding dependencies!
""")

print("\n✅ File 10 complete! You've finished all 10 tutorial files!")
print("\n📚 NEXT STEPS:")
print("  - Review all files in order (01-10)")
print("  - Complete all practice exercises")
print("  - Build a small project using what you've learned")
print("  - Explore: asyncio, pytest, requests, numpy, pandas")