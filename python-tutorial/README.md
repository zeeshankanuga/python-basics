# Complete Python Learning Tutorial

Based on the Python tutorial video (https://youtu.be/mM6X7wjEtag), this repository contains a comprehensive learning path from Python basics to intermediate concepts with practical examples.

## 📚 Learning Path Overview

This tutorial is structured in a progressive manner - each file builds upon concepts from previous files. Follow the numbered sequence for the best learning experience.

## 📁 File Structure & Reading Order

| File | Topic | Difficulty | Prerequisites |
|------|-------|------------|---------------|
| `01_basics_syntax.py` | Variables, Data Types, Basic Operations | Beginner | None |
| `02_control_flow.py` | If/Elif/Else, Comparison & Logical Operators | Beginner | 01 |
| `03_loops.py` | For Loops, While Loops, Loop Control | Beginner | 01, 02 |
| `04_functions.py` | Function Definitions, Parameters, Return Values | Beginner | 01-03 |
| `05_data_structures.py` | Lists, Tuples, Dictionaries, Sets | Beginner | 01-03 |
| `06_modules_packages.py` | Importing Modules, Creating Packages | Intermediate | 01-05 |
| `07_file_io.py` | File Reading/Writing, Context Managers | Intermediate | 01-05 |
| `08_error_handling.py` | Try/Except, Custom Exceptions | Intermediate | 01-05 |
| `09_oop_basics.py` | Classes, Objects, Inheritance, Polymorphism | Intermediate | 01-08 |
| `10_stdlib_overview.py` | Common Standard Library Modules | Intermediate | 01-08 |

## 🚀 How to Run the Examples

### Prerequisites
- Python 3.8+ installed on your system
- A code editor (VS Code recommended)
- Terminal/Command prompt access

### Running a Single File
```bash
# Navigate to the tutorial directory
cd /Users/zeeshankanuga/Zeeshan/DevOps/python/python-tutorial

# Run any Python file
python 01_basics_syntax.py
```

### Running All Files in Sequence
```bash
# Run all files in order
for file in *.py; do
    echo "=== Running $file ==="
    python "$file"
    echo ""
done
```

### Interactive Learning (Recommended)
```bash
# Start Python REPL
python

# Then import and test concepts interactively
>>> from 01_basics_syntax import *
>>> # Test variables, data types, etc.
```

## 📖 How to Read These Files

Each file follows this structure:
1. **Concept Explanation** - Clear explanation of the topic
2. **Code Examples** - Practical, runnable code with comments
3. **Expected Output** - Shows what the code produces
4. **Key Takeaways** - Summary of important concepts
5. **Practice Exercises** - Hands-on exercises to reinforce learning

### Reading Tips
- **Read top to bottom** - Concepts build progressively
- **Run the code** - Don't just read, execute and experiment
- **Modify examples** - Change values, add print statements to see what happens
- **Complete exercises** - Practice is essential for retention

## 🎯 Learning Objectives

By completing this tutorial, you will understand:
- ✅ Python syntax and basic programming concepts
- ✅ Variables, data types, and operators
- ✅ Control flow (conditionals and loops)
- ✅ Functions and code organization
- ✅ Core data structures (list, tuple, dict, set)
- ✅ Modules and packages
- ✅ File I/O operations
- ✅ Error handling and debugging
- ✅ Object-Oriented Programming basics
- ✅ Common standard library modules

## 📝 Study Recommendations

### For Complete Beginners
1. Spend 1-2 hours per file
2. Type out examples manually (don't copy-paste)
3. Complete all practice exercises
4. Review previous files before moving on

### For Experienced Programmers
1. Skim familiar concepts
2. Focus on Python-specific syntax
3. Pay attention to best practices shown
4. Use as reference for Python idioms

## 🔧 Development Environment Setup

### VS Code (Recommended)
1. Install VS Code
2. Install Python extension
3. Select Python interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter"
4. Open this folder in VS Code

### Running in VS Code
- Open any `.py` file
- Click the ▶️ Run button (top right)
- Or press `F5` to debug
- Use integrated terminal: `Ctrl+``

## 📚 Additional Resources

### Official Documentation
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [Python Language Reference](https://docs.python.org/3/reference/)

### Practice Platforms
- [LeetCode](https://leetcode.com/) - Algorithm practice
- [HackerRank](https://www.hackerrank.com/) - Coding challenges
- [Exercism](https://exercism.org/) - Mentored practice

### Style Guides
- [PEP 8](https://pep8.org/) - Style Guide for Python Code
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## 🤝 Contributing

Found an error or want to improve an example?
1. Fork this repository
2. Make your changes
3. Submit a pull request

## 📄 License

This tutorial is for educational purposes. Feel free to use, modify, and share.

---

**Happy Learning! 🐍**

*Start with `01_basics_syntax.py` and work your way through!*