# Python Learning Repository

A structured, hands-on guide to learning Python from basics to advanced concepts. This repository contains day-by-day learning materials, comprehensive documentation, and practical examples.

---

## 📁 Repository Structure

```
python/
├── day-1/           # Day 1: Python fundamentals, syntax, variables
├── day-2/           # Day 2: Control flow, loops, conditionals
├── day-3/           # Day 3: Data structures (lists, tuples, sets, dicts)
├── day-4/           # Day 4: Functions, modules, packages
├── day-5/           # Day 5: File I/O, exceptions, OOP basics
├── day-6/           # Day 6: Advanced OOP, decorators, generators
├── day-7/           # Day 7: Concurrency, testing, packaging
├── python-basic.md  # Complete Python basics reference guide
├── python-advance.md # Complete Python advanced concepts guide
└── README.md        # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ installed ([Download Python](https://www.python.org/downloads/))
- Code editor (VS Code, PyCharm, or any preferred editor)
- Basic terminal/command line knowledge

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/zeeshankanuga/python-basics.git
cd python-basics

# Verify Python installation
python --version
# or
python3 --version

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Deactivate when done
deactivate
```

---

## 📚 Learning Path

### Week 1: Python Fundamentals (Days 1-3)

| Day | Topic | Key Concepts | Reference |
|-----|-------|--------------|-----------|
| **Day 1** | Python Basics | Variables, data types, strings, basic I/O | `python-basic.md` |
| **Day 2** | Control Flow | Conditionals, loops, break/continue | `python-basic.md` |
| **Day 3** | Data Structures | Lists, tuples, sets, dictionaries, comprehensions | `python-basic.md` |

**Practice**: Complete exercises in `day-1/`, `day-2/`, `day-3/` folders

### Week 2: Core Python Skills (Days 4-5)

| Day | Topic | Key Concepts | Reference |
|-----|-------|--------------|-----------|
| **Day 4** | Functions & Modules | Defining functions, *args/**kwargs, imports, virtual envs | `python-basic.md` |
| **Day 5** | File I/O & OOP | Reading/writing files, JSON, classes, inheritance | `python-basic.md` |

**Practice**: Complete exercises in `day-4/`, `day-5/` folders

### Week 3: Advanced Python (Days 6-7)

| Day | Topic | Key Concepts | Reference |
|-----|-------|--------------|-----------|
| **Day 6** | Advanced Concepts | Decorators, generators, context managers, itertools | `python-advance.md` |
| **Day 7** | Production Python | Concurrency (threading/asyncio), testing, packaging | `python-advance.md` |

**Practice**: Complete exercises in `day-6/`, `day-7/` folders

---

## 📖 How to Use This Repository

### 1. **Read the Reference Guides First**
Start with [`python-basic.md`](python-basic.md) for a complete overview of Python fundamentals, then progress to [`python-advance.md`](python-advance.md) for advanced topics.

### 2. **Follow the Day-by-Day Structure**
Each `day-N/` folder contains:
- **Concept explanations** with code examples
- **Hands-on exercises** with solutions
- **Mini-projects** to apply what you've learned

### 3. **Practice Actively**
```bash
# Run example scripts
python day-1/hello_world.py

# Experiment in interactive mode
python
>>> print("Hello, Python!")
```

### 4. **Track Your Progress**
- ✅ Complete all exercises in each day's folder
- ✅ Build the mini-project at the end of each day
- ✅ Modify examples to experiment with variations
- ✅ Write your own code from scratch

---

## 🛠️ Development Workflow

### Running Python Scripts
```bash
# Run a script
python script.py

# Run with arguments
python script.py arg1 arg2

# Run module
python -m package.module
```

### Using the Python REPL
```bash
# Start interactive session
python

# Exit
exit()  # or Ctrl+D (Linux/macOS) / Ctrl+Z (Windows)
```

### Installing Packages
```bash
# Install single package
pip install requests

# Install from requirements
pip install -r requirements.txt

# Save installed packages
pip freeze > requirements.txt
```

---

## 📋 Quick Reference

### Essential Commands
| Command | Description |
|---------|-------------|
| `python --version` | Check Python version |
| `python -m venv venv` | Create virtual environment |
| `pip install package` | Install package |
| `pip list` | List installed packages |
| `python -m pytest` | Run tests |
| `python -m black .` | Format code |
| `python -m mypy .` | Type check |

### Helpful Resources in This Repo
- **[python-basic.md](python-basic.md)** — Complete basics reference (variables, control flow, data structures, functions, OOP, file I/O)
- **[python-advance.md](python-advance.md)** — Advanced concepts (decorators, generators, async, metaclasses, testing, packaging)

---

## 🎯 Learning Tips

1. **Code Daily** — Even 30 minutes daily beats 5 hours once a week
2. **Type Everything** — Don't copy-paste; type code to build muscle memory
3. **Break Things** — Modify examples, cause errors, then fix them
4. **Build Projects** — Apply concepts to real problems (CLI tools, web scrapers, APIs)
5. **Read Code** — Explore open-source Python projects on GitHub
6. **Use Type Hints** — Start early with type annotations for better code quality

---

## 🔗 Useful External Resources

### Official Documentation
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Library Reference](https://docs.python.org/3/library/)
- [PEP 8 Style Guide](https://pep8.org/)

### Practice Platforms
- [LeetCode](https://leetcode.com/) — Algorithmic problems
- [HackerRank](https://www.hackerrank.com/) — Coding challenges
- [Codewars](https://www.codewars.com/) — Kata practice
- [Advent of Code](https://adventofcode.com/) — Annual puzzles

### Advanced Learning
- [Real Python](https://realpython.com/) — In-depth tutorials
- [Python Weekly](https://www.pythonweekly.com/) — Newsletter
- [Fluent Python](https://www.oreilly.com/library/view/fluent-python/9781491946237/) — Book by Luciano Ramalho

---

## 🤝 Contributing

Found an error? Want to add examples? Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Zeeshan Kanuga** — Technical Architect | DevOps Engineer | Platform Engineering | AI-Augmented DevOps

Built by [Zeeshan Kanuga](https://github.com/zeeshankanuga)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zeeshankanuga/)

---

**Happy Learning! 🐍**