"""
=============================================================================
FILE: 09_oop_basics.py
TOPIC: Object-Oriented Programming - Classes, Objects, Inheritance, Polymorphism
LEVEL: Intermediate
PREREQUISITES: 01-08 (basic Python concepts)
=============================================================================

This file covers Object-Oriented Programming in Python:
- Classes and objects
- Attributes and methods
- Constructors (__init__)
- Inheritance
- Polymorphism
- Encapsulation
- Special methods (dunder methods)
- Class methods and static methods
- Properties
- Abstract base classes

Run this file: python 09_oop_basics.py
"""

# =============================================================================
# SECTION 1: CLASSES AND OBJECTS
# =============================================================================

print("=" * 60)
print("SECTION 1: CLASSES AND OBJECTS")
print("=" * 60)

# Defining a simple class
class Dog:
    """A simple dog class."""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Constructor - called when creating new instance."""
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute
    
    def bark(self):
        """Instance method."""
        return f"{self.name} says Woof!"
    
    def __str__(self):
        """String representation."""
        return f"Dog(name={self.name}, age={self.age})"
    
    def __repr__(self):
        """Official string representation."""
        return f"Dog('{self.name}', {self.age})"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"dog1: {dog1}")
print(f"dog2: {dog2}")
print(f"dog1.name: {dog1.name}")
print(f"dog1.age: {dog1.age}")
print(f"dog1.species: {dog1.species}")
print(f"dog1.bark(): {dog1.bark()}")

# Each instance has its own attributes
dog1.name = "Buddy Jr."
print(f"\nAfter modification:")
print(f"dog1.name: {dog1.name}")
print(f"dog2.name: {dog2.name}")

# Class attribute is shared
print(f"dog1.species: {dog1.species}")
print(f"dog2.species: {dog2.species}")
Dog.species = "Canis lupus familiaris"
print(f"After class change: dog1.species: {dog1.species}, dog2.species: {dog2.species}")


# =============================================================================
# SECTION 2: CONSTRUCTORS AND INITIALIZATION
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: CONSTRUCTORS AND INITIALIZATION")
print("=" * 60)

class Person:
    def __init__(self, name, age=0, email=None):
        """Constructor with default parameters."""
        self.name = name
        self.age = age
        self.email = email
        self._id = None  # "Private" by convention
    
    def __init_subclass__(cls, **kwargs):
        """Called when class is subclassed."""
        super().__init_subclass__(**kwargs)
        print(f"Subclass created: {cls.__name__}")

# Multiple constructors using class methods
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @classmethod
    def square(cls, side):
        """Alternative constructor for square."""
        return cls(side, side)
    
    @classmethod
    def from_dict(cls, data):
        """Alternative constructor from dictionary."""
        return cls(data['width'], data['height'])
    
    def area(self):
        return self.width * self.height

# Using alternative constructors
rect1 = Rectangle(10, 5)
rect2 = Rectangle.square(7)
rect3 = Rectangle.from_dict({"width": 8, "height": 6})

print(f"Rectangle(10, 5).area(): {rect1.area()}")
print(f"Rectangle.square(7).area(): {rect2.area()}")
print(f"Rectangle.from_dict(...).area(): {rect3.area()}")


# =============================================================================
# SECTION 3: INSTANCE METHODS, CLASS METHODS, STATIC METHODS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: METHOD TYPES")
print("=" * 60)

class Calculator:
    """Demonstrates different method types."""
    
    # Class attribute
    history = []
    
    def __init__(self):
        self.last_result = None
    
    # Instance method - operates on instance
    def add(self, a, b):
        result = a + b
        self.last_result = result
        Calculator.history.append(f"{a} + {b} = {result}")
        return result
    
    # Class method - operates on class
    @classmethod
    def get_history(cls):
        return cls.history
    
    @classmethod
    def clear_history(cls):
        cls.history.clear()
    
    # Static method - no access to class or instance
    @staticmethod
    def is_even(n):
        return n % 2 == 0
    
    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Negative not allowed")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

calc = Calculator()
print(f"calc.add(5, 3): {calc.add(5, 3)}")
print(f"calc.last_result: {calc.last_result}")
print(f"Calculator.get_history(): {Calculator.get_history()}")
print(f"Calculator.is_even(4): {Calculator.is_even(4)}")
print(f"Calculator.factorial(5): {Calculator.factorial(5)}")


# =============================================================================
# SECTION 4: INHERITANCE
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: INHERITANCE")
print("=" * 60)

# Base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def __str__(self):
        return f"{self.name} ({self.species})"

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} fetches the ball!"

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Cat")
        self.indoor = indoor
    
    def make_sound(self):
        return "Meow!"
    
    def purr(self):
        return f"{self.name} purrs..."

# Using inheritance
dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", indoor=False)

print(f"dog: {dog}")
print(f"dog.make_sound(): {dog.make_sound()}")
print(f"dog.fetch(): {dog.fetch()}")
print(f"dog.breed: {dog.breed}")

print(f"\ncat: {cat}")
print(f"cat.make_sound(): {cat.make_sound()}")
print(f"cat.purr(): {cat.purr()}")
print(f"cat.indoor: {cat.indoor}")

# isinstance and issubclass
print(f"\nisinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")


# =============================================================================
# SECTION 5: POLYMORPHISM
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: POLYMORPHISM")
print("=" * 60)

# Polymorphism: same interface, different behavior
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        import math
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

# Polymorphic function
def print_shape_info(shape):
    print(f"  {shape.__class__.__name__}: area={shape.area():.2f}, perimeter={shape.perimeter():.2f}")

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
print("Polymorphic behavior:")
for shape in shapes:
    print_shape_info(shape)


# =============================================================================
# SECTION 6: ENCAPSULATION
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: ENCAPSULATION")
print("=" * 60)

class BankAccount:
    """Demonstrates encapsulation with private attributes."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder      # Public
        self._balance = initial_balance           # "Protected" (convention)
        self.__pin = "0000"                       # "Private" (name mangling)
    
    # Public methods to access private data
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return "Insufficient funds"
    
    def get_balance(self, pin):
        if pin == self.__pin:
            return self._balance
        return "Invalid PIN"
    
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return True
        return False

account = BankAccount("Alice", 1000)
print(f"Account holder: {account.account_holder}")
print(f"Public attr: {account.account_holder}")
print(f"Protected attr: {account._balance}")

# Private attribute (name mangled)
# print(account.__pin)  # AttributeError!
print(f"Private attr (mangled): {account._BankAccount__pin}")

print(f"Deposit 500: {account.deposit(500)}")
print(f"Balance: {account.get_balance('0000')}")
print(f"Withdraw 200: {account.withdraw(200, '0000')}")
print(f"Balance: {account.get_balance('0000')}")


# =============================================================================
# SECTION 7: PROPERTIES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: PROPERTIES")
print("=" * 60)

class Temperature:
    """Temperature with Celsius/Fahrenheit conversion using properties."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        return self._celsius + 273.15

temp = Temperature(25)
print(f"25°C = {temp.fahrenheit:.1f}°F = {temp.kelvin:.2f}K")

temp.fahrenheit = 100
print(f"100°F = {temp.celsius:.1f}°C")

try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

# Read-only property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(f"\nCircle radius=5:")
print(f"  radius: {c.radius}")
print(f"  diameter: {c.diameter}")
print(f"  area: {c.area:.2f}")
# c.radius = 10  # AttributeError: can't set attribute


# =============================================================================
# SECTION 8: SPECIAL METHODS (DUNDER METHODS)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: SPECIAL METHODS (DUNDER METHODS)")
print("=" * 60)

class Vector:
    """2D Vector with operator overloading."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Subtraction
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Multiplication (scalar)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self * scalar
    
    # Equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Length
    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))
    
    # Boolean value
    def __bool__(self):
        return self.x != 0 or self.y != 0
    
    # Indexing
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")
    
    # Iteration
    def __iter__(self):
        yield self.x
        yield self.y
    
    # Call
    def __call__(self, scale=1):
        return Vector(self.x * scale, self.y * scale)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"3 * v1: {3 * v1}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
print(f"len(v1): {len(v1)}")
print(f"bool(v1): {bool(v1)}")
print(f"bool(Vector(0, 0)): {bool(Vector(0, 0))}")
print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")
print(f"list(v1): {list(v1)}")
print(f"v1(2): {v1(2)}")


# =============================================================================
# SECTION 9: ABSTRACT BASE CLASSES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: ABSTRACT BASE CLASSES")
print("=" * 60)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for vehicles."""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def start(self):
        return f"{self.info()}: Engine started"
    
    def stop(self):
        return f"{self.info()}: Engine stopped"

class Motorcycle(Vehicle):
    def start(self):
        return f"{self.info()}: Motorcycle started"
    
    def stop(self):
        return f"{self.info()}: Motorcycle stopped"

# Cannot instantiate abstract class
# vehicle = Vehicle("Generic", "Vehicle")  # TypeError!

car = Car("Toyota", "Camry")
bike = Motorcycle("Harley", "Davidson")

print(f"car.start(): {car.start()}")
print(f"car.stop(): {car.stop()}")
print(f"bike.start(): {bike.start()}")

# Abstract class with concrete methods
class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        pass
    
    def describe(self):
        return f"A {self.color} shape with area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle("red", 5, 3)
print(f"\nrect.describe(): {rect.describe()}")


# =============================================================================
# SECTION 10: MULTIPLE INHERITANCE AND MIXINS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: MULTIPLE INHERITANCE AND MIXINS")
print("=" * 60)

# Mixin classes (small, focused functionality)
class SerializableMixin:
    def to_json(self):
        import json
        from datetime import datetime
        
        def default(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')
        
        return json.dumps(self.__dict__, default=default)
    
    def to_dict(self):
        return self.__dict__

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def touch(self):
        from datetime import datetime
        self.updated_at = datetime.now()

# Using mixins
class User(SerializableMixin, TimestampMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print(f"user.to_dict(): {user.to_dict()}")
print(f"user.to_json(): {user.to_json()}")

# MRO (Method Resolution Order)
print(f"\nUser MRO: {[c.__name__ for c in User.__mro__]}")


# =============================================================================
# SECTION 11: CLASS VARIABLES VS INSTANCE VARIABLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 11: CLASS VS INSTANCE VARIABLES")
print("=" * 60)

class Counter:
    # Class variable (shared)
    count = 0
    
    def __init__(self, name):
        # Instance variable (unique per instance)
        self.name = name
        Counter.count += 1
        self.instance_id = Counter.count
    
    def __del__(self):
        Counter.count -= 1

c1 = Counter("First")
c2 = Counter("Second")
c3 = Counter("Third")

print(f"c1.instance_id: {c1.instance_id}, Counter.count: {Counter.count}")
print(f"c2.instance_id: {c2.instance_id}, Counter.count: {Counter.count}")
print(f"c3.instance_id: {c3.instance_id}, Counter.count: {Counter.count}")

del c2
print(f"After del c2: Counter.count: {Counter.count}")

# Mutable class variable trap!
class BadExample:
    items = []  # Shared by all instances!
    
    def add(self, item):
        self.items.append(item)

class GoodExample:
    def __init__(self):
        self.items = []  # Each instance gets own list
    
    def add(self, item):
        self.items.append(item)

print("\nMutable class variable trap:")
bad1 = BadExample()
bad1.add("a")
bad2 = BadExample()
bad2.add("b")
print(f"bad1.items: {bad1.items}")  # ['a', 'b'] - shared!
print(f"bad2.items: {bad2.items}")  # ['a', 'b'] - shared!

good1 = GoodExample()
good1.add("a")
good2 = GoodExample()
good2.add("b")
print(f"good1.items: {good1.items}")  # ['a'] - separate!
print(f"good2.items: {good2.items}")  # ['b'] - separate!


# =============================================================================
# SECTION 12: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 12: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Plugin system
class Plugin(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class UppercasePlugin(Plugin):
    def execute(self, data):
        return data.upper()

class ReversePlugin(Plugin):
    def execute(self, data):
        return data[::-1]

class PluginManager:
    def __init__(self):
        self.plugins = []
    
    def register(self, plugin):
        self.plugins.append(plugin)
    
    def process(self, data):
        for plugin in self.plugins:
            data = plugin.execute(data)
        return data

manager = PluginManager()
manager.register(UppercasePlugin())
manager.register(ReversePlugin())
print(f"Plugin pipeline: {manager.process('hello')}")

# Example 2: Data class (Python 3.7+)
from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

product = Product("Laptop", 999.99, ["electronics", "computer"])
print(f"\nDataclass: {product}")
print(f"product.price: {product.price}")

# Example 3: Enum
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()

print(f"\nStatus.COMPLETED: {Status.COMPLETED}")
print(f"Status.COMPLETED.value: {Status.COMPLETED.value}")

# Example 4: Protocol (Structural subtyping - Python 3.8+)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self):
        return "Drawing circle"

class Square:
    def draw(self):
        return "Drawing square"

def render(shape: Drawable):
    return shape.draw()

print(f"\nProtocol: {render(Circle())}")
print(f"Protocol: {render(Square())}")


# =============================================================================
# SECTION 13: PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 13: PRACTICE EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Employee Hierarchy
------------------------------
Create classes:
- Employee (base): name, id, salary, department
- Manager: inherits Employee, adds team_size, bonus
- Developer: inherits Employee, adds languages, projects
- Intern: inherits Employee, adds university, graduation_date

EXERCISE 2: Shape Calculator
----------------------------
Create abstract Shape class with:
- area() and perimeter() abstract methods
- Concrete subclasses: Circle, Rectangle, Triangle
- Function to calculate total area of list of shapes

EXERCISE 3: Bank System
-----------------------
Create:
- Account (base): account_number, balance, owner
- SavingsAccount: interest_rate, calculate_interest()
- CheckingAccount: overdraft_limit, withdraw()
- Transaction history with timestamps

EXERCISE 4: Game Characters
---------------------------
Create:
- Character (base): name, health, attack_power
- Warrior: special_ability = "shield_block"
- Mage: special_ability = "fireball"
- Archer: special_ability = "multi_shot"
- Battle system with polymorphism

EXERCISE 5: Configuration Classes
---------------------------------
Create:
- Config (base): load from file
- DevConfig, ProdConfig, TestConfig (inheritance)
- Factory function to get config by environment
""")

# Exercise Solutions
print("\n--- EXERCISE SOLUTIONS ---")

# Exercise 1
print("\nExercise 1 - Employee Hierarchy:")

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department
    
    def get_info(self):
        return f"{self.name} (ID: {self.emp_id}), {self.department}, ${self.salary:,}"

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department, team_size, bonus=0):
        super().__init__(name, emp_id, salary, department)
        self.team_size = team_size
        self.bonus = bonus
    
    def get_info(self):
        base = super().get_info()
        return f"{base}, Team: {self.team_size}, Bonus: ${self.bonus:,}"

class Developer(Employee):
    def __init__(self, name, emp_id, salary, department, languages, projects):
        super().__init__(name, emp_id, salary, department)
        self.languages = languages
        self.projects = projects
    
    def get_info(self):
        base = super().get_info()
        return f"{base}, Languages: {', '.join(self.languages)}"

class Intern(Employee):
    def __init__(self, name, emp_id, salary, department, university, graduation_date):
        super().__init__(name, emp_id, salary, department)
        self.university = university
        self.graduation_date = graduation_date
    
    def get_info(self):
        base = super().get_info()
        return f"{base}, University: {self.university}, Graduates: {self.graduation_date}"

employees = [
    Manager("Alice", "M001", 120000, "Engineering", 8, 15000),
    Developer("Bob", "D001", 90000, "Engineering", ["Python", "Java"], ["Project A", "Project B"]),
    Intern("Charlie", "I001", 30000, "Marketing", "Stanford", "2025-06"),
]

for emp in employees:
    print(f"  {emp.get_info()}")

# Exercise 2
print("\nExercise 2 - Shape Calculator:")

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

def total_area(shapes):
    return sum(shape.area() for shape in shapes)

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
print(f"  Shapes: {[type(s).__name__ for s in shapes]}")
print(f"  Total area: {total_area(shapes):.2f}")

# Exercise 3
print("\nExercise 3 - Bank System:")

from datetime import datetime

class Account:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []
        self._record("account_opened", initial_balance)
    
    def _record(self, type_, amount):
        self.transactions.append({
            "type": type_,
            "amount": amount,
            "balance": self.balance,
            "timestamp": datetime.now()
        })
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._record("deposit", amount)
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self._record("withdraw", amount)
            return True
        return False
    
    def get_statement(self):
        return self.transactions

class SavingsAccount(Account):
    def __init__(self, account_number, owner, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return interest

class CheckingAccount(Account):
    def __init__(self, account_number, owner, initial_balance=0, overdraft_limit=100):
        super().__init__(account_number, owner, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self._record("withdraw", amount)
            return True
        return False

savings = SavingsAccount("SA001", "Alice", 1000, 0.05)
checking = CheckingAccount("CA001", "Bob", 500, 200)

savings.deposit(500)
interest = savings.calculate_interest()
print(f"  Savings: balance={savings.balance}, interest={interest:.2f}")

checking.withdraw(600)  # Uses overdraft
print(f"  Checking: balance={checking.balance}, overdraft used={500-checking.balance}")

# Exercise 4
print("\nExercise 4 - Game Characters:")

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.alive = True
    
    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        return f"{self.name} attacks {target.name} for {damage} damage"
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            return f"{self.name} has been defeated!"
        return f"{self.name} takes {damage} damage, health: {self.health}"
    
    def special(self, target):
        return f"{self.name} uses basic attack"

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
    
    def special(self, target):
        self.health += 20  # Shield block heals
        return f"{self.name} uses Shield Block! Health: {self.health}"

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=35)
    
    def special(self, target):
        damage = self.attack_power * 2
        target.take_damage(damage)
        return f"{self.name} casts Fireball! Deals {damage} damage"

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25)
    
    def special(self, targets):
        results = []
        for target in targets:
            damage = self.attack_power
            target.take_damage(damage)
            results.append(f"{target.name} takes {damage}")
        return f"{self.name} uses Multi-Shot! " + ", ".join(results)

warrior = Warrior("Conan")
mage = Mage("Gandalf")
archer = Archer("Legolas")
enemies = [Character("Orc1", 50, 10), Character("Orc2", 50, 10)]

print(f"  {warrior.special(enemies[0])}")
print(f"  {mage.special(enemies[1])}")
print(f"  {archer.special(enemies)}")

# Exercise 5
print("\nExercise 5 - Configuration Classes:")

class Config:
    DEBUG = False
    DATABASE_URL = "sqlite:///app.db"
    SECRET_KEY = "default-secret"
    
    @classmethod
    def get_config(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}

class DevConfig(Config):
    DEBUG = True
    DATABASE_URL = "sqlite:///dev.db"

class ProdConfig(Config):
    DEBUG = False
    DATABASE_URL = "postgresql://prod.db"
    SECRET_KEY = "super-secret-production-key"

class TestConfig(Config):
    DEBUG = True
    DATABASE_URL = "sqlite:///:memory:"

def get_config(env):
    configs = {
        "development": DevConfig,
        "production": ProdConfig,
        "testing": TestConfig,
    }
    return configs.get(env, Config)

print(f"  Dev: {get_config('development').get_config()}")
print(f"  Prod: {get_config('production').get_config()}")
print(f"  Test: {get_config('testing').get_config()}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Classes define blueprints; objects are instances
2. __init__ is constructor; self refers to instance
3. Inheritance: class Child(Parent) - use super()
4. Polymorphism: same method name, different behavior
5. Encapsulation: _protected, __private (name mangling)
6. Properties: @property for controlled attribute access
7. Class methods (@classmethod) - work with class
8. Static methods (@staticmethod) - utility functions
9. Special methods (__add__, __eq__, etc.) for operators
10. Abstract base classes (ABC) define interfaces
11. Mixins for reusable functionality
12. Dataclasses reduce boilerplate for data containers
13. MRO determines method resolution in multiple inheritance
""")

print("\n✅ File 09 complete! Run 'python 10_stdlib_overview.py' next.")