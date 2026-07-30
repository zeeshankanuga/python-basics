"""
=============================================================================
FILE: 08_error_handling.py
TOPIC: Error Handling - Try/Except, Custom Exceptions, Best Practices
LEVEL: Intermediate
PREREQUISITES: 01-07 (basic Python concepts)
=============================================================================

This file covers error handling in Python:
- Understanding exceptions
- try/except/else/finally blocks
- Common built-in exceptions
- Raising exceptions
- Custom exception classes
- Exception chaining
- Best practices

Run this file: python 08_error_handling.py
"""

# =============================================================================
# SECTION 1: UNDERSTANDING EXCEPTIONS
# =============================================================================

print("=" * 60)
print("SECTION 1: UNDERSTANDING EXCEPTIONS")
print("=" * 60)

print("""
Exceptions are events that disrupt normal program flow:
- Syntax errors (caught at compile time)
- Runtime errors (exceptions) - occur during execution

When an exception occurs:
1. Python creates an exception object
2. Normal flow stops
3. Python searches for handler (try/except)
4. If found, handler runs; if not, program crashes with traceback

Common Exception Types:
- Exception (base class for most exceptions)
- ValueError - wrong value type
- TypeError - wrong type for operation
- IndexError - sequence index out of range
- KeyError - dictionary key not found
- FileNotFoundError - file doesn't exist
- ZeroDivisionError - division by zero
- ImportError - import fails
- AttributeError - attribute doesn't exist
""")


# =============================================================================
# SECTION 2: BASIC TRY/EXCEPT
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: BASIC TRY/EXCEPT")
print("=" * 60)

# Catching a specific exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught: Division by zero!")

# Catching multiple exceptions
try:
    value = int("hello")
except ValueError:
    print("Caught: Invalid integer conversion")
except TypeError:
    print("Caught: Type error")

# Catching multiple exceptions in one block
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except (IndexError, KeyError) as e:
    print(f"Caught: {type(e).__name__}: {e}")

# Accessing exception object
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")


# =============================================================================
# SECTION 3: TRY/EXCEPT/ELSE/FINALLY
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: TRY/EXCEPT/ELSE/FINALLY")
print("=" * 60)

print("""
Complete try block structure:
-----------------------------
try:
    # Code that might raise exception
    risky_operation()
except SomeException:
    # Handle specific exception
    handle_error()
except AnotherException:
    # Handle another exception
    handle_other_error()
except Exception:
    # Catch all other exceptions (broad)
    handle_generic()
else:
    # Runs ONLY if NO exception occurred
    success_cleanup()
finally:
    # ALWAYS runs (cleanup)
    always_cleanup()
""")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    else:
        print(f"Success: {a} / {b} = {result}")
        return result
    finally:
        print("  (finally block always executes)")

print("divide(10, 2):")
divide(10, 2)

print("\ndivide(10, 0):")
divide(10, 0)


# =============================================================================
# SECTION 4: RAISING EXCEPTIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: RAISING EXCEPTIONS")
print("=" * 60)

# raise with exception class
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age set to {age}"

print("set_age(25):", set_age(25))
try:
    set_age(-5)
except ValueError as e:
    print(f"Caught: {e}")

# raise with custom message
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError(f"Insufficient funds: ${balance} available, ${amount} requested")
    return balance - amount

try:
    withdraw(100, 150)
except ValueError as e:
    print(f"Caught: {e}")

# Re-raising exception (preserves traceback)
def process_data(data):
    try:
        # Some processing
        result = data / 0
    except ZeroDivisionError:
        print("Logging error...")
        raise  # Re-raise the same exception

try:
    process_data(10)
except ZeroDivisionError:
    print("Caught re-raised exception")


# =============================================================================
# SECTION 5: CUSTOM EXCEPTIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: CUSTOM EXCEPTIONS")
print("=" * 60)

# Basic custom exception
class CustomError(Exception):
    """Base custom exception."""
    pass

class ValidationError(CustomError):
    """Raised when validation fails."""
    def __init__(self, message, field=None):
        self.field = field
        super().__init__(message)

class InsufficientFundsError(CustomError):
    """Raised when account has insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: ${balance} available, ${amount} requested")

# Using custom exceptions
class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValidationError("Initial balance cannot be negative", "initial_balance")
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValidationError("Deposit amount must be positive", "amount")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive", "amount")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Testing custom exceptions
account = BankAccount(100)
print(f"Initial balance: {account.balance}")

account.deposit(50)
print(f"After deposit: {account.balance}")

try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(f"Withdrawal failed: {e}")
    print(f"  Balance: ${e.balance}, Requested: ${e.amount}")

try:
    account.deposit(-10)
except ValidationError as e:
    print(f"Deposit failed: {e}")
    print(f"  Field: {e.field}")


# =============================================================================
# SECTION 6: EXCEPTION CHAINING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: EXCEPTION CHAINING")
print("=" * 60)

print("""
Exception chaining preserves original cause:
-------------------------------------------
1. Implicit chaining (automatic):
   try:
       risky()
   except SomeError:
       raise OtherError()  # __cause__ set automatically

2. Explicit chaining (raise ... from ...):
   raise NewError() from original_error

3. Suppressing chaining:
   raise NewError() from None
""")

# Implicit chaining
def parse_config(config_str):
    try:
        return int(config_str)
    except ValueError:
        raise RuntimeError("Config parsing failed")

try:
    parse_config("not_a_number")
except RuntimeError as e:
    print(f"Implicit chaining:")
    print(f"  Exception: {e}")
    print(f"  Cause: {e.__cause__}")

# Explicit chaining
def read_config_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Cannot read config: {filename}") from e

try:
    read_config_file("nonexistent.txt")
except RuntimeError as e:
    print(f"\nExplicit chaining:")
    print(f"  Exception: {e}")
    print(f"  Cause: {e.__cause__}")

# Suppress chaining
try:
    try:
        int("abc")
    except ValueError:
        raise RuntimeError("Conversion failed") from None
except RuntimeError as e:
    print(f"\nSuppressed chaining:")
    print(f"  Exception: {e}")
    print(f"  Cause: {e.__cause__}")


# =============================================================================
# SECTION 7: COMMON EXCEPTION PATTERNS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: COMMON EXCEPTION PATTERNS")
print("=" * 60)

# 1. EAFP (Easier to Ask Forgiveness than Permission) - Pythonic
print("1. EAFP vs LBYL:")
# LBYL (Look Before You Leap) - not Pythonic
my_dict = {"a": 1}
if "a" in my_dict:
    print(f"  LBYL: {my_dict['a']}")

# EAFP - Pythonic
try:
    print(f"  EAFP: {my_dict['a']}")
except KeyError:
    print("  Key not found")

# 2. Try/except in loops
print("\n2. Exception handling in loops:")
data = ["1", "2", "three", "4", "five"]
results = []
for item in data:
    try:
        results.append(int(item))
    except ValueError:
        results.append(None)
        print(f"  Skipped invalid: {item}")
print(f"  Results: {results}")

# 3. Context manager for cleanup
print("\n3. Resource cleanup with try/finally:")
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"  Acquired: {name}")
    
    def release(self):
        print(f"  Released: {self.name}")
    
    def use(self):
        if self.name == "bad":
            raise RuntimeError("Resource error")

res = Resource("good")
try:
    res.use()
finally:
    res.release()

# 4. Assertion (for debugging, not production error handling)
print("\n4. Assertions:")
def calculate_discount(price, discount_percent):
    assert 0 <= discount_percent <= 100, "Discount must be 0-100"
    return price * (1 - discount_percent / 100)

print(f"  100 with 20% off: {calculate_discount(100, 20)}")
# calculate_discount(100, 150)  # AssertionError


# =============================================================================
# SECTION 8: EXCEPTION BEST PRACTICES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: EXCEPTION BEST PRACTICES")
print("=" * 60)

print("""
DO:
✓ Catch specific exceptions (not bare except:)
✓ Use custom exceptions for domain errors
✓ Include useful information in exception messages
✓ Use finally for cleanup (or context managers)
✓ Chain exceptions with 'from' for debugging
✓ Log exceptions before handling/re-raising
✓ Use else clause for success-only code

DON'T:
✗ Use bare 'except:' (catches everything including SystemExit)
✗ Catch Exception too broadly without reason
✗ Use exceptions for control flow (normal flow)
✗ Swallow exceptions silently (pass in except)
✗ Raise generic Exception (use specific types)
✗ Forget to clean up resources

Anti-patterns to avoid:
-----------------------
# BAD - bare except
try:
    do_something()
except:
    pass  # Swallows ALL exceptions including KeyboardInterrupt!

# BAD - catching Exception too broadly
try:
    do_something()
except Exception:
    pass  # Hides bugs!

# GOOD - specific exceptions
try:
    do_something()
except (ValueError, TypeError) as e:
    logger.error(f"Invalid input: {e}")
    raise ValidationError(str(e))

# GOOD - re-raise after logging
try:
    risky_operation()
except SpecificError as e:
    logger.exception("Operation failed")
    raise
""")


# =============================================================================
# SECTION 9: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Robust input validation
def get_valid_input(prompt, validator, error_msg="Invalid input"):
    """Keep asking until valid input."""
    while True:
        try:
            value = input(prompt)
            return validator(value)
        except (ValueError, TypeError) as e:
            print(f"  {error_msg}: {e}")

# Simulate input for demo
def demo_get_valid_input():
    print("1. Input validation (simulated):")
    test_inputs = iter(["abc", "-5", "25"])
    def mock_input(prompt):
        val = next(test_inputs)
        print(f"  {prompt}{val}")
        return val
    
    # Monkey patch for demo
    import builtins
    original_input = builtins.input
    builtins.input = mock_input
    
    try:
        age = get_valid_input("Enter age: ", int, "Must be a positive integer")
        print(f"  Got age: {age}")
    finally:
        builtins.input = original_input

demo_get_valid_input()

# Example 2: Retry decorator
import time
from functools import wraps

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """Decorator to retry function on exception."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"  Attempt {attempt + 1} failed: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1, exceptions=(ConnectionError,))
def unreliable_connection():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network unavailable")
    return "Connected!"

print("\n2. Retry decorator:")
try:
    result = unreliable_connection()
    print(f"  Success: {result}")
except ConnectionError:
    print("  All retries failed")

# Example 3: Context manager for error handling
from contextlib import contextmanager

@contextmanager
def error_handler(operation_name, default=None):
    """Context manager that catches and logs errors."""
    try:
        yield
    except Exception as e:
        print(f"  [{operation_name}] Error: {type(e).__name__}: {e}")
        if default is not None:
            return default
        raise

print("\n3. Error handler context manager:")
with error_handler("file_read", default="default content"):
    raise FileNotFoundError("test.txt missing")

# Example 4: Validation with multiple errors
class ValidationCollector:
    """Collect multiple validation errors before raising."""
    def __init__(self):
        self.errors = []
    
    def check(self, condition, message):
        if not condition:
            self.errors.append(message)
    
    def raise_if_errors(self):
        if self.errors:
            raise ValidationError("Validation failed: " + "; ".join(self.errors))

def validate_user(data):
    collector = ValidationCollector()
    collector.check("name" in data and data["name"], "Name is required")
    collector.check("email" in data and "@" in data["email"], "Valid email required")
    collector.check("age" in data and isinstance(data["age"], int) and data["age"] >= 0, "Age must be positive integer")
    collector.check("age" not in data or data["age"] <= 150, "Age must be <= 150")
    collector.raise_if_errors()
    return True

print("\n4. Validation collector:")
test_users = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "", "email": "bob@example.com", "age": 30},
    {"name": "Charlie", "email": "charlie", "age": -5},
]

for user in test_users:
    try:
        validate_user(user)
        print(f"  Valid: {user}")
    except ValidationError as e:
        print(f"  Invalid: {user} -> {e}")


# =============================================================================
# SECTION 10: DEBUGGING WITH TRACEBACK
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: DEBUGGING WITH TRACEBACK")
print("=" * 60)

import traceback

def level3():
    raise ValueError("Error at level 3")

def level2():
    level3()

def level1():
    level2()

print("Full traceback:")
try:
    level1()
except Exception:
    traceback.print_exc()

print("\nFormatted traceback:")
try:
    level1()
except Exception as e:
    tb_str = traceback.format_exc()
    print(f"Captured:\n{tb_str}")

print("\nTraceback details:")
try:
    level1()
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Traceback object: {e.__traceback__}")
    tb = e.__traceback__
    while tb:
        print(f"  File: {tb.tb_frame.f_code.co_filename}, Line: {tb.tb_lineno}, Function: {tb.tb_frame.f_code.co_name}")
        tb = tb.tb_next


# =============================================================================
# SECTION 11: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 11: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Exception Hierarchy
-------------------------------
Create custom exceptions for a library system:
- LibraryError (base)
- BookNotFoundError
- BookAlreadyBorrowedError
- MemberNotFoundError
- MaxBooksExceededError

EXERCISE 2: Safe Calculator
---------------------------
Create a calculator that:
- Handles division by zero
- Handles invalid operators
- Handles non-numeric input
- Returns Result object (success/error)

EXERCISE 3: File Processor with Retry
-------------------------------------
Write a function that processes a file with:
- Retry on temporary errors (PermissionError)
- Skip permanently failed files
- Log all errors
- Return summary

EXERCISE 4: API Client Error Handling
-------------------------------------
Create an API client that:
- Defines custom exceptions for HTTP errors
- Retries on 5xx errors
- Raises specific exceptions for 4xx errors
- Includes request/response info in exceptions

EXERCISE 5: Context Manager for Transactions
--------------------------------------------
Create a DatabaseTransaction context manager:
- Commits on success
- Rolls back on exception
- Logs transaction status
""")

# Exercise Solutions
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
print("\nExercise 1 - Library Exception Hierarchy:")

class LibraryError(Exception):
    """Base exception for library system."""
    pass

class BookNotFoundError(LibraryError):
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"Book not found: {book_id}")

class BookAlreadyBorrowedError(LibraryError):
    def __init__(self, book_id, borrower):
        self.book_id = book_id
        self.borrower = borrower
        super().__init__(f"Book {book_id} already borrowed by {borrower}")

class MemberNotFoundError(LibraryError):
    def __init__(self, member_id):
        self.member_id = member_id
        super().__init__(f"Member not found: {member_id}")

class MaxBooksExceededError(LibraryError):
    def __init__(self, member_id, limit):
        self.member_id = member_id
        self.limit = limit
        super().__init__(f"Member {member_id} has reached max limit of {limit} books")

# Test
try:
    raise BookNotFoundError("ISBN-12345")
except LibraryError as e:
    print(f"  Caught: {e}")

# Exercise 2
print("\nExercise 2 - Safe Calculator:")

class CalcResult:
    def __init__(self, success, value=None, error=None):
        self.success = success
        self.value = value
        self.error = error
    
    def __repr__(self):
        if self.success:
            return f"CalcResult(success=True, value={self.value})"
        return f"CalcResult(success=False, error={self.error})"

def safe_calculate(a, operator, b):
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return CalcResult(False, error="Invalid numbers")
    
    try:
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                return CalcResult(False, error="Division by zero")
            result = a / b
        else:
            return CalcResult(False, error=f"Unknown operator: {operator}")
        return CalcResult(True, value=result)
    except Exception as e:
        return CalcResult(False, error=str(e))

tests = [(10, '+', 5), (10, '/', 0), ("abc", '*', 2), (10, '%', 3)]
for a, op, b in tests:
    result = safe_calculate(a, op, b)
    print(f"  {a} {op} {b} = {result}")

# Exercise 3
print("\nExercise 3 - File Processor with Retry:")

def process_file_with_retry(filepath, max_retries=3):
    """Process file with retry on transient errors."""
    import errno
    
    for attempt in range(max_retries):
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            return {"success": True, "content": content, "attempts": attempt + 1}
        except PermissionError as e:
            if attempt == max_retries - 1:
                return {"success": False, "error": f"Permission denied after {max_retries} attempts", "attempts": attempt + 1}
            print(f"  Retry {attempt + 1}/{max_retries} for {filepath}")
            time.sleep(0.1)
        except FileNotFoundError:
            return {"success": False, "error": "File not found", "attempts": attempt + 1}
        except OSError as e:
            return {"success": False, "error": f"OS error: {e}", "attempts": attempt + 1}

# Test with existing file
import tempfile
import os
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.write("Test content")
    temp_filename = f.name

result = process_file_with_retry(temp_filename)
print(f"  Existing file: {result}")

result = process_file_with_retry("nonexistent.txt")
print(f"  Missing file: {result}")

os.unlink(temp_filename)

# Exercise 4
print("\nExercise 4 - API Client Error Handling:")

class APIError(Exception):
    def __init__(self, message, status_code=None, response=None):
        self.status_code = status_code
        self.response = response
        super().__init__(message)

class ClientError(APIError):
    """4xx errors"""
    pass

class ServerError(APIError):
    """5xx errors"""
    pass

class NotFoundError(ClientError):
    pass

class UnauthorizedError(ClientError):
    pass

class RateLimitError(ClientError):
    def __init__(self, retry_after=None):
        self.retry_after = retry_after
        super().__init__("Rate limited", status_code=429)

def make_request(url, max_retries=3):
    """Simulated API request with error handling."""
    import random
    
    # Simulate different responses
    responses = [
        {"status": 200, "data": {"result": "success"}},
        {"status": 404, "error": "Not found"},
        {"status": 500, "error": "Server error"},
        {"status": 429, "error": "Rate limited", "retry_after": 1},
    ]
    
    for attempt in range(max_retries):
        response = random.choice(responses)
        
        if response["status"] == 200:
            return response["data"]
        elif response["status"] == 404:
            raise NotFoundError(response["error"], status_code=404)
        elif response["status"] == 401:
            raise UnauthorizedError("Unauthorized", status_code=401)
        elif response["status"] == 429:
            raise RateLimitError(response.get("retry_after"))
        elif response["status"] >= 500:
            if attempt == max_retries - 1:
                raise ServerError(response["error"], status_code=response["status"])
            print(f"  Server error, retry {attempt + 1}/{max_retries}")
            time.sleep(0.1)
    
    raise ServerError("Max retries exceeded")

print("  Simulated API calls:")
for i in range(5):
    try:
        result = make_request("/api/test")
        print(f"    Call {i+1}: Success - {result}")
    except NotFoundError as e:
        print(f"    Call {i+1}: NotFound - {e}")
    except RateLimitError as e:
        print(f"    Call {i+1}: RateLimited - {e}")
    except ServerError as e:
        print(f"    Call {i+1}: ServerError - {e}")

# Exercise 5
print("\nExercise 5 - Database Transaction Context Manager:")

class DatabaseTransaction:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.committed = False
        self.rolled_back = False
    
    def __enter__(self):
        print(f"  [TXN] Begin transaction on {self.connection_string}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
            print(f"  [TXN] Rolled back due to: {exc_type.__name__}: {exc_val}")
        return False  # Don't suppress exception
    
    def commit(self):
        self.committed = True
        print(f"  [TXN] Committed")
    
    def rollback(self):
        self.rolled_back = True
        print(f"  [TXN] Rolled back")
    
    def execute(self, query):
        print(f"  [TXN] Execute: {query}")

print("  Successful transaction:")
with DatabaseTransaction("postgresql://localhost/db") as txn:
    txn.execute("INSERT INTO users (name) VALUES ('Alice')")
    txn.execute("UPDATE accounts SET balance = 100 WHERE user_id = 1")

print("\n  Failed transaction:")
try:
    with DatabaseTransaction("postgresql://localhost/db") as txn:
        txn.execute("INSERT INTO users (name) VALUES ('Bob')")
        raise ValueError("Constraint violation!")
except ValueError:
    print("  Caught exception after rollback")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Use try/except to handle exceptions gracefully
2. Catch specific exceptions, not bare 'except:'
3. Use else for success-only code, finally for cleanup
4. Raise exceptions with 'raise' for error conditions
5. Create custom exceptions for domain-specific errors
6. Chain exceptions with 'raise ... from ...' for debugging
7. Use context managers ('with') for resource management
8. EAFP (try/except) is more Pythonic than LBYL (if checks)
9. Log exceptions before handling or re-raising
10. Don't use exceptions for normal control flow
11. Include useful context in exception messages
12. Consider retry logic for transient failures
""")

print("\n✅ File 08 complete! Run 'python 09_oop_basics.py' next.")