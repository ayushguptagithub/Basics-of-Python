Here’s a comprehensive guide on **Functions in Python**, with explanations, code examples, and detailed explanations for students.

---

# **Python Functions: A Complete Guide**

---

## **What is a Function?**
A **function** in Python is a block of reusable code that performs a specific task. Functions make code modular, reusable, and easier to maintain.

---

## **Types of Functions**
1. **Built-in Functions**: Predefined functions like `print()`, `len()`, etc.
2. **User-defined Functions**: Functions created by the user using the `def` keyword.
3. **Anonymous Functions**: Functions without a name, defined using the `lambda` keyword.

---

## **Creating a Function**

To create a function, use the `def` keyword, followed by the function name, parentheses `( )`, and a colon `:`.

### **Syntax**
```python
def function_name(parameters):
    """Docstring: Optional description of the function."""
    # Function body
    return value  # Optional
```

### **Example**
```python
def greet(name):
    """This function greets the user by name."""
    return f"Hello, {name}!"

print(greet("John"))  # Output: Hello, John!
```

---

## **Calling a Function**
A function is called by its name followed by parentheses.

```python
def add(a, b):
    return a + b

result = add(5, 10)  # Function call
print(result)        # Output: 15
```

---

## **Function Arguments**

1. **Positional Arguments**  
   Arguments are passed in the same order as the function parameters.

   ```python
   def subtract(a, b):
       return a - b

   print(subtract(10, 5))  # Output: 5
   ```

2. **Keyword Arguments**  
   Arguments are passed with parameter names, irrespective of their position.

   ```python
   def introduce(name, age):
       return f"My name is {name} and I am {age} years old."

   print(introduce(age=25, name="Alice"))
   # Output: My name is Alice and I am 25 years old.
   ```

3. **Default Arguments**  
   Parameters with default values are optional when calling the function.

   ```python
   def greet(name="Guest"):
       return f"Hello, {name}!"

   print(greet())          # Output: Hello, Guest!
   print(greet("John"))    # Output: Hello, John!
   ```

4. **Variable-Length Arguments**  
   - **`*args` (Non-keyword Arguments)**: Used to pass a variable number of positional arguments.

     ```python
     def add(*numbers):
         return sum(numbers)

     print(add(1, 2, 3, 4))  # Output: 10
     ```

   - **`**kwargs` (Keyword Arguments)**: Used to pass a variable number of keyword arguments.

     ```python
     def details(**info):
         for key, value in info.items():
             print(f"{key}: {value}")

     details(name="John", age=25, city="New York")
     # Output:
     # name: John
     # age: 25
     # city: New York
     ```

---

## **Return Statement**

The `return` statement sends a result back to the caller. If no `return` is specified, the function returns `None`.

```python
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)  # Output: 12
```

---

## **Docstrings**
A **docstring** is an optional description of a function, enclosed in triple quotes.

```python
def greet(name):
    """This function greets the user by name."""
    return f"Hello, {name}!"

print(greet.__doc__)  # Output: This function greets the user by name.
```

---

## **Anonymous (Lambda) Functions**

Lambda functions are single-line, anonymous functions defined using the `lambda` keyword.

### **Syntax**
```python
lambda arguments: expression
```

### **Example**
```python
square = lambda x: x**2
print(square(5))  # Output: 25

add = lambda a, b: a + b
print(add(3, 7))  # Output: 10
```

---

## **Scope and Lifetime of Variables**

1. **Local Scope**: Variables declared inside a function are local to that function.
2. **Global Scope**: Variables declared outside any function are global.

### **Example**
```python
x = 10  # Global variable

def modify():
    x = 5  # Local variable
    print("Inside function:", x)

modify()
print("Outside function:", x)
# Output:
# Inside function: 5
# Outside function: 10
```

### **Using `global` Keyword**
```python
x = 10

def modify():
    global x
    x = 5

modify()
print(x)  # Output: 5
```

---

## **Recursive Functions**

A function that calls itself is called a recursive function.

### **Example: Factorial**
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```



## **Advantages of Functions**
1. **Code Reusability**: Avoids repetition of code.
2. **Modularity**: Breaks the program into smaller, manageable pieces.
3. **Improves Readability**: Easier to understand and maintain.
4. **Debugging**: Errors are easier to identify and fix.

---

## **Comparison: Function vs. Lambda**

| Feature              | Function                      | Lambda                       |
|-----------------------|------------------------------|------------------------------|
| **Definition**        | `def` keyword                | `lambda` keyword             |
| **Name**              | Has a name                   | Anonymous (no name)          |
| **Complexity**        | Can include multiple lines   | Single-line expression only  |
| **Use Case**          | For reusable, complex logic  | For short, simple operations |

---

# **Python Classes: A Complete Guide**

---

## **What is a Class?**
A **class** is a blueprint for creating objects. It defines the structure and behavior (data and methods) that the objects of the class will have.

---

## **Key Concepts**
1. **Class**: The blueprint or template.
2. **Object**: An instance of the class.
3. **Attributes**: Data or properties associated with an object.
4. **Methods**: Functions defined within a class that operate on its attributes.
5. **`self`**: Refers to the instance of the class. It is used to access attributes and methods within the class.

---

## **Creating a Class**

### **Syntax**
```python
class ClassName:
    """Class docstring: Description of the class."""
    # Attributes and methods go here
```

---

## **Creating Objects**
An **object** is created by calling the class as if it were a function.

```python
class Dog:
    """A simple Dog class."""
    pass

# Create an object of the Dog class
my_dog = Dog()
print(type(my_dog))  # Output: <class '__main__.Dog'>
```

---

## **Class with Attributes**

### **Instance Attributes**
Attributes specific to each object are defined inside the `__init__` method.

```python
class Dog:
    """A class representing a dog."""
    
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Charlie", "Poodle")

print(dog1.name, dog1.breed)  # Output: Buddy Golden Retriever
print(dog2.name, dog2.breed)  # Output: Charlie Poodle
```

---

### **Class Attributes**
Attributes shared across all instances of the class.

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
```

---

## **Methods in Classes**

### **Instance Methods**
Operate on an instance's attributes and require `self` as the first parameter.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Buddy")
print(dog.bark())  # Output: Buddy says woof!
```

---

### **Class Methods**
Operate on class attributes and require `@classmethod` decorator. The first parameter is `cls`.

```python
class Dog:
    species = "Canis familiaris"

    @classmethod
    def get_species(cls):
        return cls.species

print(Dog.get_species())  # Output: Canis familiaris
```

---

### **Static Methods**
Do not operate on class or instance attributes. Defined using `@staticmethod`.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 10))  # Output: 15
```

---

## **Special (Magic/Dunder) Methods**
Special methods provide built-in behavior for objects. They are surrounded by double underscores (`__`).

### **`__init__`**
Called automatically when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.name, person.age)  # Output: Alice 30
```

---

### **`__str__`**
Defines the string representation of an object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old
```

---

### **`__repr__`**
Provides an unambiguous string representation of the object (useful for debugging).

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(repr(person))  # Output: Person(name='Alice', age=30)
```

---

## **Inheritance**
Inheritance allows a class (child) to derive attributes and methods from another class (parent).

### **Example**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Buddy")
print(dog.eat())  # Output: Buddy is eating.
print(dog.bark())  # Output: Buddy says woof!
```

---

## **Polymorphism**
Polymorphism allows methods to have different implementations depending on the class.

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
# Output:
# Woof!
# Meow!
```

---

## **Encapsulation**
Encapsulation restricts access to certain components of an object.

### **Access Modifiers**
1. **Public**: Accessible from anywhere.
2. **Protected (`_attribute`)**: Indicated by a single underscore; treated as "protected."
3. **Private (`__attribute`)**: Indicated by double underscores; name-mangled to restrict access.

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Public
        self._age = age   # Protected
        self.__salary = 50000  # Private

    def get_salary(self):
        return self.__salary

person = Person("Alice", 30)
print(person.name)  # Output: Alice
print(person._age)  # Output: 30
print(person.get_salary())  # Output: 50000
```

---

## **Abstract Classes**
Abstract classes cannot be instantiated and must be subclassed. They use the `abc` module.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!
```

---

## **Class vs. Instance Variables**

| **Feature**            | **Class Variable**               | **Instance Variable**            |
|-------------------------|----------------------------------|-----------------------------------|
| **Shared?**             | Shared among all instances       | Unique to each instance          |
| **Defined in**          | Class level                     | Instance (inside `__init__`)     |

---

## **Key Benefits of Classes**
1. **Code Reusability**: Methods and attributes can be reused.
2. **Organization**: Encapsulates logic into objects.
3. **Modularity**: Easier to manage and debug.
4. **Abstraction**: Hides complex implementation details.
