
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
