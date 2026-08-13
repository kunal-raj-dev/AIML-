## Classes and objects

**Concepts**

- **CLASS :** A class is a blueprint that defines attributes (data) and methods (behavior)
- **OBJECT :** An object (instance) is a concrete realization of that class with its own state.
    
**Basic syntax example**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age

    def bark(self):
        print(f"{self.name} barks!")

dog1 = Dog("Bruno", 3) # instance
dog1.bark()  # Bruno barks!
```

Q) Explain what `Dog` is, what `dog1` is, and what `self` does?
A) `Dog` is a class `dog1` is address pointer toward created object for particular instance.

---

## The `self` parameter

**Key points**
- `self` refers to the current instance and 
- Is the first parameter in instance methods by convention.
- Python passes the object automatically; you access instance attributes with `self.attr`.


```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
```
Q) Explain why `self.count` is different for different objects?
A) for every new instance new object created and different memory address

---
## Instance, class, and static variables

**Instance variables**
- Defined inside `__init__` or instance methods (`self.x`)
- and belongs to each object. (no cross data transfer between two objects)

**Class variables**
- Defined directly in the class body 
- shared across all instances.

```python
class User:
    user_count = 0  # class variable

    def __init__(self, name):
        self.name = name     # instance variable
        User.user_count += 1
```

Q) How `user_count` tracks total users across instances?
A) instance methods can access and manipulate variables of their class 

---
## Instance vs class vs static methods

**Instance methods**
- First parameter is `self`; operates on a specific object’s state.    

**Class methods**
- Declared with `@classmethod`, first parameter `cls`; operates on class‑level state (e.g., factories, tracking counts).

**Static methods**
- Declared with `@staticmethod`; no implicit `self` or `cls`; utility functions logically tied to the class.    

```python
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):                 # instance method
        return Circle.pi * self.radius ** 2

    @classmethod
    def unit_circle(cls):           # class method
        return cls(1)

    @staticmethod
    def is_valid_radius(r):         # static method
        return r >= 0


# Create a normal circle
c1 = Circle(5)
print(c1.radius)          # 5
print(c1.area())          # 78.53975

# Create a unit circle using the class method
c2 = Circle.unit_circle()
print(c2.radius)          # 1
print(c2.area())          # 3.14159

# Use the static method
print(Circle.is_valid_radius(10))   # True
print(Circle.is_valid_radius(-5))   # False
```

Be ready to explain when you’d choose each method type.

---

## Constructors and destructors

**Constructors (`__init__`)**

- Special method called automatically when creating an object; used to initialize instance state.
    
```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
```

You should note that Python doesn’t have multiple constructors but you can simulate them with class methods or default/optional parameters.[scribd](https://www.scribd.com/document/892061416/OOPS-Interview-Questions)

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __init__(self, name, age):
        self.name = name
        self.age = age
```


**Destructors (`__del__`)**

- Called when an object is about to be destroyed; rarely used today.[pynative](https://pynative.com/python/object-oriented-programming/)
    
```python
class FileHandler:
    def __init__(self, path):
        self.file = open(path)

    def __del__(self):
        self.file.close()
```

Explain why context managers (`with`) are usually preferred over `__del__`.[tutorialsteacher](https://www.tutorialsteacher.com/python/magic-methods-in-python)

---
## Encapsulation and access control

**Concepts**

- Encapsulation bundles data and methods in a class and hides internals to protect invariants.[geeksforgeeks](https://www.geeksforgeeks.org/python/python-oops-concepts/)
    
- Python uses naming conventions for access:
    - Public: `var`
    - “Protected”: `_var` (by convention).
    - “Private”: `__var` (name mangling).[programiz](https://www.programiz.com/python-programming/object-oriented-programming)
        
**Example**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         # public
        self._balance = balance    # protected by convention
        self.__password = "1234"   # name-mangled

    def deposit(self, amount):
        self._balance += amount
```

You should be able to talk about why Python prefers “we are all consenting adults” over strict private enforcement.[programiz](https://www.programiz.com/python-programming/object-oriented-programming)]

---
## Properties, getters, and setters

### Why properties

- Properties allow you to expose attributes with controlled access, validation, read-only access, and computed values while keeping **attribute-like syntax**.
- Properties are one of the most useful features in Python because they let you **treat a method like an attribute**.
- They let you change the internal implementation of a class without changing how external code uses it.

### Without properties

```python
class Product:
    def __init__(self, price):
        self.price = price
```

Usage:
```python
p = Product(100)

print(p.price)
p.price = 200
```

Here, `price` is just a normal public instance variable.

Problem:
```python
p.price = -100
```

There is no validation, so invalid values can be assigned.

---
### Using traditional getters and setters

```python
class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Invalid price")
        self._price = value
```

Usage:
```python
print(p.get_price())
p.set_price(200)
```

This works, but it isn't considered Pythonic because users must remember to call methods instead of using attributes.

---
### Using properties

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price
```

Usage:
```python
p = Product(100)

print(p.price)

p.price = 200
```

Although it looks like a normal attribute, Python is actually calling methods behind the scenes.

Reading:
```python
p.price
```

calls
```python
price(self)
```

Writing:
```python
p.price = 200
```

calls
```python
price(self, 200)
```

(the setter).

---
### Why use `_price` instead of `price`?

`_price` stores the actual data.

`price` is the public interface exposed through the property.

If the getter returned `self.price` instead of `self._price`, it would call itself forever (infinite recursion).

---
### Why not just create a `set_price()` method?

You can.

The advantage of properties is that users can continue writing

```python
p.price = 200
```

instead of

```python
p.set_price(200)
```

while still getting validation.

Properties combine the simplicity of attributes with the power of methods.

---

### Read-only properties

If only a getter is defined:

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
```

Then:
```python
print(p.price)
```
works.

But:
```python
p.price = 200
```

raises
```text
AttributeError: property 'price' has no setter
```

The property becomes read-only.

---
### Can someone still change `_price`?

Yes.
```python
p._price = -100
```

works because `_price` is only protected by convention.

Properties don't make data truly private.

Python follows the philosophy:

> "We are all consenting adults."

meaning programmers are expected to respect the public interface (`price`) instead of modifying internal variables (`_price`) directly.

---
### When should you use properties?

Use properties when you need:

- Validation before assigning a value.
- Read-only attributes.
- Computed attributes (for example, `area`).
- To change the internal implementation without changing external code.

---
## Inheritance (is‑a relationship)

**Basics**
- Inheritance is an Object-Oriented Programming (OOP) feature where one class (child/subclass) acquires the properties and methods of another class (parent/superclass).
- Types often asked: single, multiple, multilevel, hierarchical, hybrid inheritance.[geeksforgeeks](https://www.geeksforgeeks.org/python/python-oops-concepts/)
    

**Single inheritance example**
```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):  # Dog is-an Animal
    def speak(self):
        print("Woof!")
```

You should discuss how overriding works (`Dog.speak` replaces `Animal.speak` for dogs).[w3resource](https://www.w3resource.com/python-interview/object-oriented-programming.php)

**Multiple inheritance and MRO**

- Python allows a class to inherit from multiple parents; method resolution is determined by MRO (Method Resolution Order), visible via `ClassName.__mro__`.[geeksforgeeks](https://www.geeksforgeeks.org/python/dunder-magic-methods-python/)]
    

python

`class Flyer:     def move(self):        print("Flying") class Walker:     def move(self):        print("Walking") class Bird(Flyer, Walker):     pass print(Bird.__mro__)`

Be able to explain why MRO matters when parents define the same method and why you must design carefully with multiple inheritance.[blog.finxter](https://blog.finxter.com/python-dunder-methods-cheat-sheet/)]

**Using `super()`**

- `super()` is used to call parent methods (especially constructors) in inheritance hierarchies.[scribd](https://www.scribd.com/document/892061416/OOPS-Interview-Questions)]
    

python

`class Employee:     def __init__(self, name):        self.name = name class Manager(Employee):     def __init__(self, name, team_size):        super().__init__(name)        self.team_size = team_size`

Explain super in both single and multiple inheritance contexts.[scribd](https://www.scribd.com/document/892061416/OOPS-Interview-Questions)]

---

## Composition and aggregation (has‑a relationship)

**Concepts**

- **Composition** is “has‑a”: building complex objects by embedding other objects as attributes instead of inheriting from them (Car has‑a Engine).[scribd](https://www.scribd.com/document/892061416/OOPS-Interview-Questions)]
    

python

`class Engine:     def start(self):        print("Engine started") class Car:     def __init__(self):        self.engine = Engine()  # composition     def drive(self):        self.engine.start()        print("Car is moving")`

You should compare composition vs inheritance and explain when you prefer composition to keep designs flexible.[realpython](https://realpython.com/python3-object-oriented-programming/)]

---

## Polymorphism

**Concepts**

- “Same interface, different implementations”: methods with the same name behave differently for different types.[realpython](https://realpython.com/python3-object-oriented-programming/)]
    
- Interview focus areas in Python:
    
    - Method overriding.[w3resource](https://www.w3resource.com/python-interview/object-oriented-programming.php)]
        
    - Duck typing (no explicit interface, just behavior).[programiz](https://www.programiz.com/python-programming/object-oriented-programming)]
        
    - “Overloading” with defaults and `*args` (since Python doesn’t support traditional overloading).[w3resource](https://www.w3resource.com/python-interview/object-oriented-programming.php)]
        
    - Operator overloading via dunder methods like `__add__`, `__eq__`.[tutorialsteacher](https://www.tutorialsteacher.com/python/magic-methods-in-python)]
        

**Overriding example**

python

`class Shape:     def area(self):        raise NotImplementedError class Rectangle(Shape):     def __init__(self, w, h):        self.w = w        self.h = h     def area(self):        return self.w * self.h class Circle(Shape):     def __init__(self, r):        self.r = r     def area(self):        return 3.14159 * self.r ** 2 shapes = [Rectangle(2, 3), Circle(1)] for s in shapes:     print(s.area())`

Be ready to show polymorphism via a common interface (`area`) used on different concrete classes.[programiz](https://www.programiz.com/python-programming/object-oriented-programming)]

**Duck typing example**

python

`def make_it_speak(animal):     animal.speak()  # works for any object that has speak() class Dog:     def speak(self):        print("Woof") class Human:     def speak(self):        print("Hello") make_it_speak(Dog()) make_it_speak(Human())`

Explain how Python focuses on what an object can do rather than its type.[programiz](https://www.programiz.com/python-programming/object-oriented-programming)]

---

## Magic / dunder methods and operator overloading

**Concepts**

- Dunder (double‑underscore) methods define how objects behave in built‑in operations: creation, printing, indexing, arithmetic, comparison, context managers, etc.[geeksforgeeks](https://www.geeksforgeeks.org/python/dunder-magic-methods-python/)]
    
- Common ones you should know:
    
    - `__init__`, `__del__` (construction & destruction).[pynative](https://pynative.com/python/object-oriented-programming/)]
        
    - `__str__`, `__repr__` (string representations).[dilshanrgs31.medium](https://dilshanrgs31.medium.com/15-essential-dunder-magic-methods-in-python-a-beginners-guide-02bd7ecc905e)]
        
    - `__len__`, `__getitem__`, `__setitem__`, `__iter__` (sequence behavior).[blog.finxter](https://blog.finxter.com/python-dunder-methods-cheat-sheet/)]
        
    - `__eq__`, `__lt__`, `__hash__` (comparisons & hashing).[tutorialsteacher](https://www.tutorialsteacher.com/python/magic-methods-in-python)]
        
    - `__enter__`, `__exit__` (context manager).[blog.finxter](https://blog.finxter.com/python-dunder-methods-cheat-sheet/)]
        
    - `__call__` (callable objects).[tutorialsteacher](https://www.tutorialsteacher.com/python/magic-methods-in-python)]
        

**Example: `__str__` and `__repr__`**

python

`class Point:     def __init__(self, x, y):        self.x = x        self.y = y     def __repr__(self):        return f"Point({self.x}, {self.y})"     def __str__(self):        return f"({self.x}, {self.y})"`

You should explain use cases: `__repr__` for debugging, `__str__` for user‑friendly output.[dilshanrgs31.medium](https://dilshanrgs31.medium.com/15-essential-dunder-magic-methods-in-python-a-beginners-guide-02bd7ecc905e)]

**Example: operator overloading**

python

`class Vector:     def __init__(self, x, y):        self.x, self.y = x, y     def __add__(self, other):        return Vector(self.x + other.x, self.y + other.y)     def __repr__(self):        return f"Vector({self.x}, {self.y})" v1 = Vector(1, 2) v2 = Vector(3, 4) print(v1 + v2)  # Vector(4, 6)`

Explain how this allows natural arithmetic syntax for custom types.[blog.finxter](https://blog.finxter.com/python-dunder-methods-cheat-sheet/)]

---

## Abstraction and abstract base classes

**Concepts**

- Abstraction hides implementation details and exposes only what’s necessary (focus on “what” not “how”).[realpython](https://realpython.com/python3-object-oriented-programming/)]
    
- In Python, you typically use the `abc` module to define abstract base classes with abstract methods.[w3resource](https://www.w3resource.com/python-interview/object-oriented-programming.php)]
    

**Example with `abc`**

python

`from abc import ABC, abstractmethod class PaymentProcessor(ABC):     @abstractmethod    def pay(self, amount):        pass class CreditCardProcessor(PaymentProcessor):     def pay(self, amount):        print(f"Paid {amount} with credit card") class UPIProcessor(PaymentProcessor):     def pay(self, amount):        print(f"Paid {amount} via UPI")`

You should explain how ABCs enforce contracts across different implementations in a system.[programiz](https://www.programiz.com/python-programming/object-oriented-programming)]

---

## Dataclasses

**Concepts**

- `dataclasses` module (Python 3.7+) reduces boilerplate for classes that primarily store data.[realpython](https://realpython.com/ref/stdlib/dataclasses/)]
    
- `@dataclass` auto‑generates `__init__`, `__repr__`, `__eq__`, and optionally ordering, immutability, etc.[realpython](https://realpython.com/python-data-classes/)]
    

**Example**

python

`from dataclasses import dataclass @dataclass class UserProfile:     username: str    email: str    is_active: bool = True u = UserProfile("kunal", "k@example.com") print(u)          # nice __repr__ print(u.username) # attribute access`

You should understand:

- Type hints are required for fields.[docs.python](https://docs.python.org/3/library/dataclasses.html)]
    
- `frozen=True` makes instances immutable.[realpython](https://realpython.com/ref/stdlib/dataclasses/)]
    
- `field(default_factory=...)` for mutable defaults.[realpython](https://realpython.com/python-data-classes/)]
    

Big MNCs often ask “when would you use a dataclass vs a regular class or namedtuple?”.[w3schools](https://www.w3schools.com/python/ref_module_dataclasses.asp)]

---

## Copy semantics: shallow vs deep copy

**Concepts**

- **Shallow copy**: copies the outer object, but nested mutable members are shared.[scribd](https://www.scribd.com/document/892061416/OOPS-Interview-Questions)]
    
- **Deep copy**: recursively copies nested objects.[scribd](https://www.scribd.com/document/892061416/OOPS-Interview-Questions)]
    

**Example**

python

`import copy class Team:     def __init__(self, members):        self.members = members team1 = Team(["A", "B"]) team2 = copy.copy(team1)     # shallow team3 = copy.deepcopy(team1) # deep`

Explain how this matters for object graphs in OOP and potential bugs if you mutate shared state unintentionally.[scribd](https://www.scribd.com/document/892061416/OOPS-Interview-Questions)]

---

## Memory management and object lifecycle

**Key points**

- Python uses automatic memory management with **reference counting** plus a cyclic garbage collector.[pynative](https://pynative.com/python/object-oriented-programming/)]
    
- When reference count drops to zero, the object is eligible for collection; `gc` module can manage cycles.[pynative](https://pynative.com/python/object-oriented-programming/)]
    
- Destructors (`__del__`) can be unpredictable in some cases; prefer context managers or explicit cleanup.[tutorialsteacher](https://www.tutorialsteacher.com/python/magic-methods-in-python)]
    

You should be able to reason about when objects are created, referenced, and cleaned up in a typical backend application.[pynative](https://pynative.com/python/object-oriented-programming/)]

---

## Common OOP design patterns in Python

You don’t need full textbook depth, but you should know at least:

**Singleton**

- Ensures only one instance of a class exists; interviewers often ask about pros/cons and thread safety.[youtube](https://www.youtube.com/watch?v=pMesBcZjpvA)]
    

python

`class Singleton:     _instance = None     def __new__(cls, *args, **kwargs):        if not cls._instance:            cls._instance = super().__new__(cls)        return cls._instance`

Explain why globals or dependency injection are often preferred over singletons in large systems.[youtube](https://www.youtube.com/watch?v=pMesBcZjpvA)][realpython](https://realpython.com/python3-object-oriented-programming/)]

**Factory**

- Encapsulates object creation logic to return different subclasses behind a common interface.[realpython](https://realpython.com/python3-object-oriented-programming/)]
    

python

`def get_payment_processor(method: str):     if method == "card":        return CreditCardProcessor()    elif method == "upi":        return UPIProcessor()    else:        raise ValueError("Unknown method")`

**Strategy**

- Encapsulates interchangeable behaviors; you already saw a bit of this with `PaymentProcessor`.[realpython](https://realpython.com/python3-object-oriented-programming/)]
    

Be ready to sketch how you’d use these patterns in a microservice or web backend context.[realpython](https://realpython.com/python3-object-oriented-programming/)]

---

## OOP vs procedural style in Python

**Talking points**

- Procedural: functions and data structures, top‑down flow; good for small scripts.[w3schools](https://www.w3schools.com/python/python_oop.asp)]
    
- OOP: models entities and relationships; better for complex systems with evolving requirements and multiple behaviors.[programiz](https://www.programiz.com/python-programming/object-oriented-programming)]
    

Interviewers may ask you to refactor a procedural script into an OO design and discuss trade‑offs.[programiz](https://www.programiz.com/python-programming/object-oriented-programming)]

---

## Additional advanced topics worth knowing briefly

You don’t need full mastery, but mentions can impress:

- **Metaclasses** (`type`, custom metaclasses) — how classes themselves can be created/modified.[docs.python](https://docs.python.org/3/library/dataclasses.html)]
    
- **Descriptors** (objects implementing `__get__`, `__set__`, `__delete__`), basis of properties.[blog.finxter](https://blog.finxter.com/python-dunder-methods-cheat-sheet/)]
    
- **Slots** (`__slots__`) to optimize memory by preventing dynamic attribute creation.[docs.python](https://docs.python.org/3/library/dataclasses.html)]
    
- **Protocols and structural typing** (inspired by duck typing; useful with type hints).[typing.python](https://typing.python.org/en/latest/spec/dataclasses.html)]
    

Even a high‑level explanation of their purpose and where they’re used is valuable in senior interviews.[typing.python](https://typing.python.org/en/latest/spec/dataclasses.html)]

---

## How to practice like you’re in the interview

Given your level (competitive programming + full‑stack), you should prepare by:

- For each topic above, write **at least one small, clean class hierarchy** (2–4 classes) and be ready to:
    
    - Explain design choices (why inheritance or composition, why properties, etc.).[realpython](https://realpython.com/python3-object-oriented-programming/)]
        
    - Modify the design live (add new feature, refactor to pattern).[realpython](https://realpython.com/python3-object-oriented-programming/)]
        
- Be able to discuss **real projects** (e.g., your blood bank portal) in OOP terms: entities, relationships, patterns used, and how Python’s OOP helped structure the code.[programiz](https://www.programiz.com/python-programming/object-oriented-programming)]
    
- Practice answering classic conceptual questions from guides like PYnative / w3resource / GeeksforGeeks on Python OOP.[pynative](https://pynative.com/python-oop-interview-questions/)]
    

If you like, next step I can act as your interviewer and run you through a mock OOP round, asking questions from these topics and giving feedback on your answers and code.