"""
=============================================================================
FILE: 07_file_io.py
TOPIC: File I/O - Reading, Writing, Context Managers
LEVEL: Intermediate
PREREQUISITES: 01-06 (basic Python concepts)
=============================================================================

This file covers file input/output operations in Python:
- Opening and closing files
- Reading files (read, readline, readlines)
- Writing files (write, writelines)
- Context managers (with statement)
- File modes
- Path handling with pathlib
- Binary files
- CSV, JSON file handling
- Best practices

Run this file: python 07_file_io.py
"""

# =============================================================================
# SECTION 1: BASIC FILE OPERATIONS
# =============================================================================

print("=" * 60)
print("SECTION 1: BASIC FILE OPERATIONS")
print("=" * 60)

import tempfile
import os

# Create a temporary file for demonstration
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python File I/O\n")
    f.write("Line 3: Learning is fun!\n")
    temp_filename = f.name

print(f"Created temp file: {temp_filename}")

# 1. Opening a file (traditional way - NOT recommended)
file_obj = open(temp_filename, 'r')
content = file_obj.read()
file_obj.close()
print(f"\n1. Traditional open/close:")
print(f"   Content:\n{content}")

# 2. Reading line by line
file_obj = open(temp_filename, 'r')
print(f"\n2. Reading line by line:")
line1 = file_obj.readline()
print(f"   First line: {line1.strip()}")
line2 = file_obj.readline()
print(f"   Second line: {line2.strip()}")
file_obj.close()

# 3. Reading all lines into a list
file_obj = open(temp_filename, 'r')
lines = file_obj.readlines()
file_obj.close()
print(f"\n3. readlines(): {lines}")

# Clean up
os.unlink(temp_filename)


# =============================================================================
# SECTION 2: CONTEXT MANAGERS (WITH STATEMENT) - RECOMMENDED
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: CONTEXT MANAGERS (WITH STATEMENT)")
print("=" * 60)

print("""
The 'with' statement automatically handles:
- Opening the file
- Closing the file (even if exception occurs)
- This is the RECOMMENDED way to work with files
""")

# Create temp file again
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.write("Context managers are great!\n")
    f.write("They handle cleanup automatically.\n")
    temp_filename = f.name

# Reading with context manager
with open(temp_filename, 'r') as f:
    content = f.read()
    print(f"Read with 'with':\n{content}")

# Writing with context manager
with open(temp_filename, 'w') as f:
    f.write("New content written!\n")
    f.write("Old content is gone (w mode truncates).\n")

# Appending with context manager
with open(temp_filename, 'a') as f:
    f.write("Appended line.\n")

# Reading back
with open(temp_filename, 'r') as f:
    print(f"After write + append:\n{f.read()}")

os.unlink(temp_filename)


# =============================================================================
# SECTION 3: FILE MODES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: FILE MODES")
print("=" * 60)

print("""
Common File Modes:
------------------
'r'   Read (default) - file must exist
'w'   Write - creates new or truncates existing
'a'   Append - creates new or adds to end
'x'   Exclusive create - fails if exists
'b'   Binary mode (e.g., 'rb', 'wb')
't'   Text mode (default) (e.g., 'rt', 'wt')
'+'   Read and write (e.g., 'r+', 'w+')

Combined modes:
----------------
'r+'  Read and write (file must exist)
'w+'  Write and read (truncates or creates)
'a+'  Append and read (creates if not exists)
'rb'  Read binary
'wb'  Write binary
""")

# Demonstrate modes
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.write("Original content\n")
    temp_filename = f.name

# 'r' - read
with open(temp_filename, 'r') as f:
    print(f"'r' mode: {f.read().strip()}")

# 'w' - write (truncates!)
with open(temp_filename, 'w') as f:
    f.write("Written with 'w' mode\n")
with open(temp_filename, 'r') as f:
    print(f"After 'w': {f.read().strip()}")

# 'a' - append
with open(temp_filename, 'a') as f:
    f.write("Appended with 'a' mode\n")
with open(temp_filename, 'r') as f:
    print(f"After 'a': {f.read().strip()}")

# 'x' - exclusive create
try:
    with open(temp_filename, 'x') as f:
        f.write("This won't write")
except FileExistsError:
    print(f"'x' mode: FileExistsError (as expected)")

os.unlink(temp_filename)


# =============================================================================
# SECTION 4: READING TECHNIQUES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: READING TECHNIQUES")
print("=" * 60)

# Create sample file
sample_content = """First line
Second line
Third line
Fourth line
Fifth line"""

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.write(sample_content)
    temp_filename = f.name

# 1. read() - entire file as string
with open(temp_filename, 'r') as f:
    content = f.read()
    print(f"1. read(): {repr(content[:50])}...")

# 2. read(size) - read specific number of characters
with open(temp_filename, 'r') as f:
    chunk = f.read(10)
    print(f"2. read(10): {repr(chunk)}")

# 3. readline() - one line at a time
with open(temp_filename, 'r') as f:
    line = f.readline()
    print(f"3. readline(): {repr(line)}")

# 4. readlines() - all lines as list
with open(temp_filename, 'r') as f:
    lines = f.readlines()
    print(f"4. readlines(): {lines}")

# 5. Iterate over file object (memory efficient!)
print(f"5. Iterating:")
with open(temp_filename, 'r') as f:
    for i, line in enumerate(f, 1):
        print(f"   Line {i}: {line.strip()}")

# 6. seek() and tell() - random access
with open(temp_filename, 'r') as f:
    print(f"6. seek/tell:")
    print(f"   Position: {f.tell()}")
    first = f.read(5)
    print(f"   Read 5 chars: {repr(first)}, Position: {f.tell()}")
    f.seek(0)
    print(f"   After seek(0): {f.tell()}")

os.unlink(temp_filename)


# =============================================================================
# SECTION 5: WRITING TECHNIQUES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: WRITING TECHNIQUES")
print("=" * 60)

# 1. write() - single string
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    chars_written = f.write("Hello, ")
    chars_written += f.write("World!\n")
    print(f"1. write() returns chars written: {chars_written}")
    temp_filename = f.name

with open(temp_filename, 'r') as f:
    print(f"   Content: {f.read()}")

# 2. writelines() - list of strings (no newlines added!)
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.writelines(lines)
    temp_filename = f.name

with open(temp_filename, 'r') as f:
    print(f"2. writelines(): {f.read()}")

# 3. print() to file
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    print("Printed to file", file=f)
    print("With print()", file=f)
    temp_filename = f.name

with open(temp_filename, 'r') as f:
    print(f"3. print(..., file=f): {f.read()}")

os.unlink(temp_filename)


# =============================================================================
# SECTION 6: PATHLIB - MODERN PATH HANDLING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: PATHLIB - MODERN PATH HANDLING")
print("=" * 60)

from pathlib import Path

# Creating paths
home = Path.home()
print(f"Home directory: {home}")

# Path operations
file_path = home / "Documents" / "example.txt"
print(f"Constructed path: {file_path}")

# Path properties
print(f"Name: {file_path.name}")
print(f"Suffix: {file_path.suffix}")
print(f"Stem: {file_path.stem}")
print(f"Parent: {file_path.parent}")
print(f"Parts: {file_path.parts}")

# Path methods
print(f"Exists: {file_path.exists()}")
print(f"Is file: {file_path.is_file()}")
print(f"Is dir: {file_path.is_dir()}")

# Create and use temp file with pathlib
with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir_path = Path(tmpdir)
    test_file = tmpdir_path / "test.txt"
    
    # Write
    test_file.write_text("Hello from pathlib!\nLine 2\nLine 3")
    print(f"\nWritten with pathlib")
    
    # Read
    content = test_file.read_text()
    print(f"Read with pathlib: {content}")
    
    # Read lines
    lines = test_file.read_text().splitlines()
    print(f"Lines: {lines}")
    
    # Write lines
    test_file.write_text("\n".join(["New line 1", "New line 2"]))
    print(f"After rewrite: {test_file.read_text()}")
    
    # Binary
    test_file.write_bytes(b"Binary data")
    print(f"Bytes: {test_file.read_bytes()}")


# =============================================================================
# SECTION 7: WORKING WITH CSV FILES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: WORKING WITH CSV FILES")
print("=" * 60)

import csv

# Sample data
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"],
    ["Charlie", 35, "Chicago"],
]

# Writing CSV
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    temp_filename = f.name

print("Written CSV:")
with open(temp_filename, 'r') as f:
    print(f.read())

# Reading CSV
with open(temp_filename, 'r', newline='') as f:
    reader = csv.reader(f)
    print("Reading CSV:")
    for row in reader:
        print(f"  {row}")

# Using DictReader/DictWriter
with open(temp_filename, 'r', newline='') as f:
    reader = csv.DictReader(f)
    print("\nAs dictionaries:")
    for row in reader:
        print(f"  {row}")

# Writing with DictWriter
new_data = [
    {"Name": "Diana", "Age": 28, "City": "Seattle"},
    {"Name": "Eve", "Age": 32, "City": "Boston"},
]

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age", "City"])
    writer.writeheader()
    writer.writerows(new_data)
    temp_filename2 = f.name

print("\nDictWriter output:")
with open(temp_filename2, 'r') as f:
    print(f.read())

os.unlink(temp_filename)
os.unlink(temp_filename2)


# =============================================================================
# SECTION 8: WORKING WITH JSON FILES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: WORKING WITH JSON FILES")
print("=" * 60)

import json

# Data to serialize
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "city": "NYC",
        "zip": "10001"
    },
    "active": True
}

# Writing JSON
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
    json.dump(data, f, indent=2)
    temp_filename = f.name

print("Written JSON:")
with open(temp_filename, 'r') as f:
    print(f.read())

# Reading JSON
with open(temp_filename, 'r') as f:
    loaded = json.load(f)
    print(f"Loaded: {loaded}")
    print(f"Name: {loaded['name']}")
    print(f"Skills: {loaded['skills']}")

# JSON with pathlib
from pathlib import Path
json_path = Path(temp_filename)
print(f"\nPathlib JSON read: {json.loads(json_path.read_text())['name']}")

os.unlink(temp_filename)


# =============================================================================
# SECTION 9: BINARY FILES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: BINARY FILES")
print("=" * 60)

# Writing binary data
binary_data = bytes(range(256))  # 0-255

with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.bin') as f:
    f.write(binary_data)
    temp_filename = f.name

print(f"Written {len(binary_data)} bytes")

# Reading binary
with open(temp_filename, 'rb') as f:
    data = f.read()
    print(f"Read {len(data)} bytes")
    print(f"First 10: {list(data[:10])}")
    print(f"Last 10: {list(data[-10:])}")

# Struct - packing/unpacking binary data
import struct

# Pack: integer, float, string
packed = struct.pack('if10s', 42, 3.14, b'Hello')
print(f"\nPacked binary: {packed}")
print(f"Length: {len(packed)}")

# Unpack
unpacked = struct.unpack('if10s', packed)
print(f"Unpacked: {unpacked}")

# Writing struct to file
with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.dat') as f:
    for i in range(5):
        f.write(struct.pack('if', i, i * 1.5))
    temp_filename = f.name

# Reading struct from file
with open(temp_filename, 'rb') as f:
    print("\nReading struct records:")
    while True:
        chunk = f.read(8)  # 4 bytes int + 4 bytes float
        if not chunk or len(chunk) < 8:
            break
        i, val = struct.unpack('if', chunk)
        print(f"  Record: int={i}, float={val}")

os.unlink(temp_filename)


# =============================================================================
# SECTION 10: FILE ENCODING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: FILE ENCODING")
print("=" * 60)

print("""
Text files need encoding specification:
- UTF-8 (default in Python 3) - supports all Unicode
- ASCII - only basic English
- Latin-1 - Western European
- UTF-16 - Unicode with 2 bytes per char

Always specify encoding for portability!
""")

# Writing with explicit encoding
text = "Hello, 世界! 🐍\nCafé, naïve, résumé"

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
    f.write(text)
    temp_filename = f.name

# Reading with explicit encoding
with open(temp_filename, 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"UTF-8: {content}")

# Different encodings
with open(temp_filename, 'w', encoding='utf-16') as f:
    f.write(text)

with open(temp_filename, 'r', encoding='utf-16') as f:
    content = f.read()
    print(f"UTF-16: {content}")

os.unlink(temp_filename)


# =============================================================================
# SECTION 11: COMMON FILE OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 11: COMMON FILE OPERATIONS")
print("=" * 60)

import shutil
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir_path = Path(tmpdir)
    
    # Create test files
    file1 = tmpdir_path / "file1.txt"
    file2 = tmpdir_path / "file2.txt"
    file1.write_text("Content of file 1")
    file2.write_text("Content of file 2")
    
    # Copy
    file3 = tmpdir_path / "file3_copy.txt"
    shutil.copy(file1, file3)
    print(f"Copy: {file3.read_text()}")
    
    # Copy with metadata
    file4 = tmpdir_path / "file4_copy2.txt"
    shutil.copy2(file1, file4)
    print(f"Copy2: {file4.read_text()}")
    
    # Move/rename
    file5 = tmpdir_path / "renamed.txt"
    shutil.move(file3, file5)
    print(f"Move: {file5.exists()}, {file3.exists()}")
    
    # Delete
    file5.unlink()
    print(f"Delete: {file5.exists()}")
    
    # Directory operations
    subdir = tmpdir_path / "subdir"
    subdir.mkdir()
    (subdir / "inner.txt").write_text("Inside subdir")
    print(f"List dir: {list(tmpdir_path.iterdir())}")
    print(f"List recursive: {list(tmpdir_path.rglob('*'))}")
    
    # File info
    stat = file1.stat()
    print(f"\nFile stats:")
    print(f"  Size: {stat.st_size} bytes")
    print(f"  Modified: {stat.st_mtime}")


# =============================================================================
# SECTION 12: TEMPORARY FILES AND DIRECTORIES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 12: TEMPORARY FILES AND DIRECTORIES")
print("=" * 60)

import tempfile

# Temporary file (auto-deletes on close)
with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt') as f:
    f.write("Temporary data")
    f.seek(0)
    print(f"Temp file: {f.name}")
    print(f"Content: {f.read()}")

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"\nTemp dir: {tmpdir}")
    test_file = Path(tmpdir) / "test.txt"
    test_file.write_text("In temp dir")
    print(f"Created: {test_file.read_text()}")

# Manual temp file (persists until manually deleted)
temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log')
temp_file.write("Log entry 1\n")
temp_file.write("Log entry 2\n")
temp_file.close()
print(f"\nPersistent temp file: {temp_file.name}")
print(f"Content: {Path(temp_file.name).read_text()}")
Path(temp_file.name).unlink()  # Clean up


# =============================================================================
# SECTION 13: BEST PRACTICES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 13: BEST PRACTICES")
print("=" * 60)

print("""
File I/O Best Practices:
------------------------
✓ Always use 'with' statement (context managers)
✓ Specify encoding explicitly (encoding='utf-8')
✓ Use pathlib for path manipulation
✓ Handle exceptions (FileNotFoundError, PermissionError)
✓ Use appropriate modes ('r', 'w', 'a', 'rb', 'wb')
✓ For large files, read line by line (iterate)
✓ Close files explicitly if not using 'with'
✓ Use newline='' for CSV files
✓ Validate paths before operations
✓ Use temporary files for intermediate data

Common Patterns:
----------------
# Read all
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Read lines
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process line by line (memory efficient)
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        process(line)

# Write
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Append
with open(path, 'a', encoding='utf-8') as f:
    f.write(new_content)

# Binary
with open(path, 'rb') as f:
    data = f.read()

Error Handling:
---------------
try:
    with open(path, 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission")
except IOError as e:
    print(f"I/O error: {e}")
""")


# =============================================================================
# SECTION 14: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 14: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Log File Analyzer
-----------------------------
Create a log file with entries like:
  [2024-01-15 10:30:00] INFO: User login
  [2024-01-15 10:31:00] ERROR: Connection failed
  [2024-01-15 10:32:00] WARNING: High memory
Write a script to count ERROR, WARNING, INFO entries

EXERCISE 2: CSV Data Processor
------------------------------
Create a CSV with: Name, Age, Salary, Department
Write a script to:
- Calculate average salary by department
- Find highest paid employee
- Export filtered data (e.g., salary > 50000)

EXERCISE 3: Configuration Manager
---------------------------------
Create a JSON config file with app settings
Write a class ConfigManager that:
- Loads config from file
- Provides get/set methods
- Saves changes back to file

EXERCISE 4: File Backup Utility
-------------------------------
Write a script that:
- Takes a directory path
- Creates a backup with timestamp
- Copies all files preserving structure
- Logs what was backed up

EXERCISE 5: Text File Statistics
--------------------------------
Write a function that analyzes a text file:
- Line count, word count, character count
- Most common words (top 10)
- Average line length
""")

# Exercise Solutions
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
print("\nExercise 1 - Log File Analyzer:")
log_entries = """[2024-01-15 10:30:00] INFO: User login
[2024-01-15 10:31:00] ERROR: Connection failed
[2024-01-15 10:32:00] WARNING: High memory usage
[2024-01-15 10:33:00] INFO: Data processed
[2024-01-15 10:34:00] ERROR: Timeout
[2024-01-15 10:35:00] INFO: Retry successful
[2024-01-15 10:36:00] WARNING: Disk space low"""

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
    f.write(log_entries)
    temp_filename = f.name

counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
with open(temp_filename, 'r') as f:
    for line in f:
        for level in counts:
            if level in line:
                counts[level] += 1

print(f"  Log counts: {counts}")
os.unlink(temp_filename)

# Exercise 2
print("\nExercise 2 - CSV Data Processor:")
csv_data = """Name,Age,Salary,Department
Alice,25,50000,Engineering
Bob,30,60000,Engineering
Charlie,35,55000,Sales
Diana,28,70000,Engineering
Eve,32,45000,Sales
Frank,29,80000,Marketing"""

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
    f.write(csv_data)
    temp_filename = f.name

import csv
from collections import defaultdict

dept_salaries = defaultdict(list)
all_employees = []

with open(temp_filename, 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        salary = int(row['Salary'])
        dept_salaries[row['Department']].append(salary)
        all_employees.append((row['Name'], salary, row['Department']))

print("  Average salary by department:")
for dept, salaries in dept_salaries.items():
    print(f"    {dept}: ${sum(salaries)/len(salaries):.0f}")

highest = max(all_employees, key=lambda x: x[1])
print(f"  Highest paid: {highest[0]} (${highest[1]})")

high_earners = [e for e in all_employees if e[1] > 50000]
print(f"  Salary > 50000: {len(high_earners)} employees")

os.unlink(temp_filename)

# Exercise 3
print("\nExercise 3 - Configuration Manager:")
import json

class ConfigManager:
    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.config = {}
        self.load()
    
    def load(self):
        if self.config_path.exists():
            self.config = json.loads(self.config_path.read_text())
        else:
            self.config = {}
    
    def save(self):
        self.config_path.write_text(json.dumps(self.config, indent=2))
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save()
    
    def __getitem__(self, key):
        return self.config[key]
    
    def __setitem__(self, key, value):
        self.set(key, value)

with tempfile.TemporaryDirectory() as tmpdir:
    config_file = Path(tmpdir) / "config.json"
    cfg = ConfigManager(config_file)
    
    cfg.set("app_name", "MyApp")
    cfg.set("version", "1.0.0")
    cfg.set("debug", True)
    cfg.set("max_connections", 100)
    
    print(f"  Config: {cfg.config}")
    print(f"  app_name: {cfg.get('app_name')}")
    print(f"  debug: {cfg.get('debug')}")
    
    cfg["new_setting"] = "value"
    print(f"  After [] set: {cfg.get('new_setting')}")

# Exercise 4
print("\nExercise 4 - File Backup Utility (simplified):")
with tempfile.TemporaryDirectory() as src_dir:
    src = Path(src_dir)
    (src / "file1.txt").write_text("Content 1")
    (src / "subdir").mkdir()
    (src / "subdir" / "file2.txt").write_text("Content 2")
    
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(tmpdir) / f"backup_{timestamp}"
    
    # Copy entire directory
    shutil.copytree(src, backup_dir)
    print(f"  Backed up to: {backup_dir}")
    print(f"  Files: {list(backup_dir.rglob('*'))}")

# Exercise 5
print("\nExercise 5 - Text File Statistics:")
sample_text = """Python is a powerful programming language.
It is easy to learn and use.
Python has many libraries for data science.
Machine learning with Python is popular.
Web development with Django and Flask.
Python runs on all major platforms."""

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.write(sample_text)
    temp_filename = f.name

with open(temp_filename, 'r') as f:
    lines = f.readlines()
    chars = sum(len(line) for line in lines)
    words = sum(len(line.split()) for line in lines)
    
    # Word frequency
    all_words = []
    for line in lines:
        all_words.extend(line.lower().strip().split())
    
    from collections import Counter
    word_freq = Counter(all_words)
    
    print(f"  Lines: {len(lines)}")
    print(f"  Words: {words}")
    print(f"  Characters: {chars}")
    print(f"  Avg line length: {chars/len(lines):.1f}")
    print(f"  Top 5 words: {word_freq.most_common(5)}")

os.unlink(temp_filename)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. ALWAYS use 'with' statement for file operations
2. Specify encoding='utf-8' for text files
3. Use pathlib.Path for modern path handling
4. File modes: r/w/a/x + b/t/+
5. Read methods: read(), readline(), readlines(), iterate
6. Write methods: write(), writelines(), print(..., file=f)
7. CSV: csv.reader/writer, DictReader/DictWriter
8. JSON: json.dump/load, json.dumps/loads
9. Binary: open with 'b', use struct for structured data
10. Handle exceptions: FileNotFoundError, PermissionError
11. tempfile for temporary files/directories
12. shutil for high-level file operations (copy, move, etc.)
""")

print("\n✅ File 07 complete! Run 'python 08_error_handling.py' next.")