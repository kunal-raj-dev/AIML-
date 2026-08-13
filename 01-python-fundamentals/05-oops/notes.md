# OOP Concepts Notes

## Important Concepts

- Classes & Objects: Blueprints vs instantiated entities.
- `__init__` constructor method: Sets initial state attributes on instantiation.
- `self` parameter: References the specific current instance of the class.
- Class vs Instance Attributes: Class variables are shared, instance variables are unique.
- **Abstraction**
  - methods defined in abstract class are minimum must required blueprints hta must exist in other class which inherit this abstract class
  - we ca add new method apart from blueprint

- **Inheritance**
  - when same method/attribute in parent class and subclasses then priority give to to subclass method/attribute
  - we can change pointer to oject by t2=t1. and reuse t1 as new instance for object.
  - when we replace old pointer to oject with new old one if not store is removed by python garbage dumper

## Common Mistakes

- Forgetting to pass `self` as the first argument in class method definitions.
- Accidentally sharing instance state by initializing lists directly as class attributes instead of inside the `__init__` constructor.
- Incorrect naming: typing `__init__` with single underscores instead of double underscores.

## Interview Notes

- **What is the role of self in Python classes?** `self` acts as a placeholder representing the specific object instance being created or manipulated. It allows access to instance properties and other class methods.
- **What is the difference between a Class Method and a Static Method?** Class Methods (`@classmethod`) accept `cls` as a parameter and can access class properties. Static Methods (`@staticmethod`) do not receive instance (`self`) or class (`cls`) parameters, behaving like regular functions housed within the namespace.

## Practice Ideas

- Design a BankAccount class holding balance, deposit methods, and withdrawal methods.
- Build a Library system modeling Book classes containing title, author, and checkout states.
