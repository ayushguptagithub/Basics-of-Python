
---

# **Python Exception Handling: A Complete Guide**

---

## **What is an Exception?**
An **exception** is an error that occurs during the execution of a program, disrupting the normal flow of the program. Python provides a robust way to handle exceptions, ensuring the program can recover or gracefully terminate.

---

## **Why Use Exception Handling?**
1. **Avoid Program Crashes**: Prevent abrupt termination due to errors.
2. **Graceful Error Management**: Handle errors in a controlled manner.
3. **Debugging**: Provides meaningful error messages.

---

## **Syntax of Exception Handling**

Python uses the `try...except` block to catch and handle exceptions.

### **Basic Syntax**
```python
try:
    # Code that may raise an exception
    pass
except ExceptionType:
    # Code to handle the exception
    pass
```

---

## **Common Built-in Exceptions**

| Exception             | Description                                |
|-----------------------|--------------------------------------------|
| `ZeroDivisionError`   | Raised when dividing by zero              |
| `ValueError`          | Raised when a function gets an invalid value |
| `TypeError`           | Raised when an operation is performed on incompatible types |
| `FileNotFoundError`   | Raised when a file is not found           |
| `IndexError`          | Raised when an index is out of range      |
| `KeyError`            | Raised when a dictionary key is not found |

---

## **Example: Basic Exception Handling**

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
```

---

## **Multiple Exceptions**

You can handle multiple exceptions using separate `except` blocks.

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
```

---

## **Using `else` with `try...except`**

The `else` block executes if no exceptions occur.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"Result: {result}")
```

---

## **The `finally` Block**

The `finally` block always executes, whether an exception occurs or not.

```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
```

---

## **Raising Exceptions**

You can raise exceptions explicitly using the `raise` keyword.

```python
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(e)
```

---

## **Custom Exceptions**

Create user-defined exceptions by subclassing the `Exception` class.

```python
class NegativeValueError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeValueError("Negative value entered!")
except NegativeValueError as e:
    print(e)
```

---

## **Chained Exceptions**

Python allows chaining exceptions using the `raise ... from` syntax.

```python
try:
    try:
        num = int("invalid")
    except ValueError as e:
        raise RuntimeError("Conversion failed") from e
except RuntimeError as e:
    print(f"Runtime error: {e}")
```

---

## **Using `assert` for Error Checking**

The `assert` statement is used to debug by testing conditions.

```python
def divide(a, b):
    assert b != 0, "Divider cannot be zero!"
    return a / b

try:
    print(divide(10, 0))
except AssertionError as e:
    print(e)
```

---

## **Best Practices for Exception Handling**

1. **Handle Specific Exceptions**: Avoid catching generic exceptions unless necessary.
2. **Log Errors**: Log exception details for debugging.
3. **Use `finally` for Cleanup**: Ensure resources like files or database connections are closed.
4. **Avoid Silent Failures**: Always provide meaningful error messages.

---

## **Examples of Common Use Cases**

### **File Handling with Exception Handling**
```python
try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
```

---

### **Division by Zero**
```python
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

### **Dictionary Key Access**
```python
try:
    data = {"name": "Alice"}
    print(data["age"])
except KeyError:
    print("Key not found in dictionary.")
```

---

### **Iterating Safely Over a List**
```python
try:
    items = [1, 2, 3]
    print(items[5])
except IndexError:
    print("Index out of range.")
```

---

## **Comparison: Checked vs. Unchecked Exceptions**

| **Feature**           | **Checked Exception**              | **Unchecked Exception**             |
|------------------------|------------------------------------|-------------------------------------|
| **Definition**         | Must be explicitly handled         | Occurs at runtime, handling optional |
| **Examples**           | FileNotFoundError, KeyError       | ZeroDivisionError, ValueError       |

---
