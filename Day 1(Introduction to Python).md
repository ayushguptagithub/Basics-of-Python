**Introduction to Python**

Python is a versatile, high-level, and interpreted programming language known for its simplicity and readability. It is widely used in various fields, including web development, data science, artificial intelligence, machine learning, automation, and more. Python's clean and straightforward syntax allows beginners to learn programming easily while being powerful enough for advanced developers to create complex applications.

### Key Features of Python:
1. **Easy to Learn and Use:** Python's syntax is straightforward and resembles plain English, making it an excellent choice for beginners.
2. **Interpreted Language:** Python executes code line-by-line, enabling easier debugging and dynamic execution.
3. **Versatile and Cross-Platform:** It runs on various platforms like Windows, macOS, Linux, etc.
4. **Extensive Libraries and Frameworks:** Python has a rich ecosystem of libraries such as NumPy, Pandas, Matplotlib, TensorFlow, and frameworks like Django and Flask.
5. **Community Support:** A vast and active community ensures quick solutions to problems and frequent updates.

### Python Applications:
- **Web Development:** Frameworks like Django and Flask enable efficient web application development.
- **Data Science:** Libraries like Pandas and NumPy simplify data manipulation and analysis.
- **Artificial Intelligence:** TensorFlow and PyTorch are used to build AI and machine learning models.
- **Automation:** Scripts written in Python can automate repetitive tasks.
- **Game Development:** Libraries like Pygame are available for game creation.

### Example Python Code:
```python
# A simple program to print "Hello, World!"
print("Hello, World!")
```


---

### 1. **Basic Print**
```python
print("Hello, World!")
```

---

### 2. **Printing Variables**
```python
name = "Ayush"
print(name)
```

---

### 3. **Printing Multiple Items**
- **Using commas (adds spaces by default):**
```python
name = "Ayush"
age = 25
print("Name:", name, "Age:", age)
```

---

### 4. **String Concatenation**
```python
name = "Ayush"
print("Hello, " + name)
```

---

### 5. **String Formatting**
- **Using `%` (Old-style formatting):**
```python
name = "Ayush"
age = 25
print("My name is %s and I am %d years old." % (name, age))
```

- **Using `.format()` (Modern-style formatting):**
```python
name = "Ayush"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```

- **Using f-strings (Python 3.6+):**
```python
name = "Ayush"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

---

### 6. **Using Escape Characters**
```python
print("Hello\nWorld")  # New line
print("Hello\tWorld")  # Tab
print("He said, \"Python is awesome!\"")  # Double quotes inside a string
```

---

### 7. **Specifying a Separator**
- **Default separator is a space, but it can be changed using `sep`:**
```python
print("Python", "is", "fun", sep="-")
```

---

### 8. **Custom End Character**
- **Default `end` is a newline, but it can be changed:**
```python
print("Hello", end=" ")
print("World")
```

---

### 9. **Printing to a File**
```python
with open("output.txt", "w") as file:
    print("Hello, File!", file=file)
```

---

### 10. **Printing Non-String Data**
```python
numbers = [1, 2, 3]
print(numbers)
```

---

### 11. **Printing Unicode Characters**
```python
print("\u2764")  # Prints a heart emoji (❤)
```

---

### 12. **Using Print with Debugging Tools**
```python
print(f"Debugging: Variable value is {variable}")
```
Python provides a wide range of data types to handle different kinds of data. These data types can be broadly categorized into built-in data types and derived data types. Here's a comprehensive list:

---

### **1. Numeric Types**
Used to represent numbers.

- **int**: Integer values (e.g., -5, 0, 100).
  ```python
  x = 10  # int
  ```

- **float**: Decimal or floating-point numbers (e.g., 3.14, -2.7).
  ```python
  y = 3.14  # float
  ```

- **complex**: Complex numbers with real and imaginary parts (e.g., 3+5j).
  ```python
  z = 3 + 5j  # complex
  ```

---

### **2. Sequence Types**
Used to store collections of items in a specific order.

- **str**: Strings (immutable sequences of characters).
  ```python
  name = "Python"  # str
  ```

- **list**: Ordered, mutable collection of elements (e.g., [1, 2, 3]).
  ```python
  my_list = [1, 2, 3]  # list
  ```

- **tuple**: Ordered, immutable collection of elements (e.g., (1, 2, 3)).
  ```python
  my_tuple = (1, 2, 3)  # tuple
  ```

---

### **3. Mapping Type**
Used to store key-value pairs.

- **dict**: Dictionary, an unordered collection of key-value pairs.
  ```python
  my_dict = {"name": "Ayush", "age": 25}  # dict
  ```

---

### **4. Set Types**
Used to store unordered collections of unique items.

- **set**: Mutable, unordered collection of unique elements.
  ```python
  my_set = {1, 2, 3}  # set
  ```

- **frozenset**: Immutable version of a set.
  ```python
  my_frozenset = frozenset({1, 2, 3})  # frozenset
  ```

---

### **5. Boolean Type**
Represents truth values.

- **bool**: True or False.
  ```python
  is_active = True  # bool
  ```




### **Type Checking**
You can check the type of a variable using the `type()` function:
```python
x = 10
print(type(x))  # Output: <class 'int'>
```

### **Introduction to Conditional Statements in Python**

Conditional statements allow your program to execute a specific block of code based on a condition. These statements use boolean expressions (`True` or `False`) to determine which path the program should take.

---

### **Types of Conditional Statements**

#### 1. **if Statement**
The `if` statement is used to execute a block of code if a specified condition is `True`.

**Syntax:**
```python
if condition:
    # Code to execute if the condition is True
```

**Example:**
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

---

#### 2. **if-else Statement**
The `if-else` statement provides an alternative block of code to execute if the condition is `False`.

**Syntax:**
```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

**Example:**
```python
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

---

#### 3. **if-elif-else Statement**
The `if-elif-else` structure is used to check multiple conditions in sequence. Only the first condition that evaluates to `True` will be executed.

**Syntax:**
```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if all conditions are False
```

**Example:**
```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")
```

---

#### 4. **Nested if Statements**
An `if` statement can be nested inside another `if` statement for more complex conditions.

**Syntax:**
```python
if condition1:
    if condition2:
        # Code to execute if both conditions are True
```

**Example:**
```python
num = 10

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")
```

---

#### 5. **Short-Hand if**
For simple conditions, you can write the `if` statement in a single line.

**Syntax:**
```python
if condition: action
```

**Example:**
```python
x = 5
if x > 0: print("x is positive")
```

---

#### 6. **Short-Hand if-else (Ternary Operator)**
A concise way to write `if-else` statements.

**Syntax:**
```python
action_if_true if condition else action_if_false
```

**Example:**
```python
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
```

---

### **Logical Operators in Conditional Statements**
Logical operators can be used to combine multiple conditions:
- **and**: Both conditions must be true.
- **or**: At least one condition must be true.
- **not**: Negates the condition.

**Example:**
```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")
```

---

### **Key Points to Remember**
1. Indentation is crucial in Python. Blocks of code inside conditions must be indented.
2. You can nest multiple `if` statements for complex logic.
3. Use logical operators for combining multiple conditions.

### **Introduction to Loops in Python**

Loops in Python are used to execute a block of code repeatedly as long as a specified condition is true. They are essential for tasks that require repetitive actions, such as iterating through items in a list or performing calculations multiple times.

---

### **Types of Loops in Python**

#### 1. **`for` Loop**
The `for` loop is used to iterate over a sequence (e.g., list, tuple, dictionary, string, or range) and execute a block of code for each item in the sequence.

**Syntax:**
```python
for item in sequence:
    # Code to execute for each item
```

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

#### 2. **`while` Loop**
The `while` loop executes a block of code as long as the specified condition evaluates to `True`.

**Syntax:**
```python
while condition:
    # Code to execute while the condition is True
```

**Example:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

### **Control Statements in Loops**

Python provides control statements to alter the flow of a loop:

#### **1. `break` Statement**
The `break` statement is used to exit the loop prematurely when a specific condition is met.

**Example:**
```python
for num in range(1, 10):
    if num == 5:
        break
    print(num)
```

---

#### **2. `continue` Statement**
The `continue` statement skips the current iteration and moves to the next iteration of the loop.

**Example:**
```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
```

---

#### **3. `pass` Statement**
The `pass` statement is a placeholder that does nothing. It’s useful for creating loops that are meant to be completed later.

**Example:**
```python
for num in range(1, 4):
    pass  # Placeholder for future code
```

---

### **Looping Techniques**

#### **1. Using `range()` in Loops**
The `range()` function generates a sequence of numbers.

**Example:**
```python
for i in range(1, 6):  # Numbers from 1 to 5
    print(i)
```

#### **2. Nested Loops**
A loop inside another loop is called a nested loop.

**Example:**
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
```

---

### **Loop with `else`**
The `else` block is executed when the loop finishes without a `break`.

**Example:**
```python
for num in range(1, 4):
    print(num)
else:
    print("Loop finished!")
```

---

### **Iterating Over Different Data Types**

#### **1. List**
```python
my_list = [1, 2, 3]
for item in my_list:
    print(item)
```

#### **2. String**
```python
my_string = "Python"
for char in my_string:
    print(char)
```

#### **3. Dictionary**
```python
my_dict = {"name": "Ayush", "age": 25}
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

---

### **Key Points to Remember**
1. Use `for` loops for sequences and `while` loops for conditions.
2. Use `break` to exit the loop and `continue` to skip to the next iteration.
3. Nested loops can be used for multi-dimensional data.
4. The `else` clause in loops adds more control after loop completion.

### **Here are the 10 questions on if-elif-else:**

---

### **1. Odd or Even**
Check whether a given number is odd or even.

**Solution:**
```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### **2. Find the Largest Number**
Find the largest among three numbers.

**Solution:**
```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print(f"{a} is the largest number.")
elif b > c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")
```

---

### **3. Grade Calculator**
Assign a grade based on marks.

**Solution:**
```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")
```

---

### **4. Leap Year Checker**
Determine whether a year is a leap year.

**Solution:**
```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

### **5. Number Classification**
Check if a number is positive, negative, or zero.

**Solution:**
```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

### **6. Calculator**
Perform basic arithmetic operations.

**Solution:**
```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/" and num2 != 0:
    print(f"Result: {num1 / num2}")
else:
    print("Invalid operator or division by zero!")
```

---

### **7. Age Eligibility**
Determine eligibility for driving, voting, and retirement.

**Solution:**
```python
age = int(input("Enter your age: "))

if age >= 60:
    print("You can drive, vote, and retire.")
elif age >= 18:
    print("You can drive and vote but not retire.")
else:
    print("You cannot drive, vote, or retire.")
```

---

### **8. Evenly Divisible Check**
Check if a number is divisible by both 5 and 7.

**Solution:**
```python
number = int(input("Enter a number: "))

if number % 5 == 0 and number % 7 == 0:
    print("Divisible by both 5 and 7")
else:
    print("Not divisible by both 5 and 7")
```

---

### **9. Triangle Type**
Determine the type of triangle based on side lengths.

**Solution:**
```python
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
```

---

### **10. BMI Calculator**
Calculate BMI and classify it.

**Solution:**
```python
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
```


### **For-loop Questions (without lists or data types):**

#### 1. **Print Numbers from 1 to 10**
Write a program using a `for` loop to print the numbers from 1 to 10.

**Solution:**
```python
for i in range(1, 11):
    print(i)
```

---

#### 2. **Sum of First N Natural Numbers**
Write a program to calculate the sum of the first `n` natural numbers, where `n` is a user input.

**Solution:**
```python
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum:", sum)
```

---

#### 3. **Print a Pattern of Stars**
Write a program to print the following pattern of stars using a `for` loop:
```
*
**
***
****
*****
```

**Solution:**
```python
for i in range(1, 6):
    print('*' * i)
```

---

#### 4. **Print Even Numbers from 2 to 20**
Write a program using a `for` loop to print all even numbers from 2 to 20.

**Solution:**
```python
for i in range(2, 21, 2):
    print(i)
```

---

#### 5. **Print Numbers in Reverse Order**
Write a program using a `for` loop to print numbers from 10 to 1.

**Solution:**
```python
for i in range(10, 0, -1):
    print(i)
```

---

### **While-loop Questions (without lists or data types):**

#### 6. **Print Numbers from 1 to 10**
Write a program using a `while` loop to print the numbers from 1 to 10.

**Solution:**
```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

---

#### 7. **Print Multiples of 3 Less than 30**
Write a program to print all multiples of 3 less than 30 using a `while` loop.

**Solution:**
```python
i = 3
while i < 30:
    print(i)
    i += 3
```

---

#### 8. **Sum of Numbers Until User Input (Stopping at 0)**
Write a program that keeps asking the user for a number and adds it to the sum. The program stops when the user enters `0`.

**Solution:**
```python
sum = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    sum += num
print("Total sum:", sum)
```

---

#### 9. **Countdown from 10 to 1**
Write a program using a `while` loop to countdown from 10 to 1.

**Solution:**
```python
i = 10
while i > 0:
    print(i)
    i -= 1
```



### **1. Reverse a Number**
Write a program using a `while` loop to reverse a given number.

**Solution:**
```python
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)
```

**Example:**
- Input: 1234
- Output: 4321

---

### **2. Check if a Number is an Armstrong Number (3-digit)**
Write a program to check if a 3-digit number is an Armstrong number. An Armstrong number is a number that is equal to the sum of the cubes of its digits.

**Solution:**
```python
num = int(input("Enter a 3-digit number: "))
original_num = num
sum_of_cubes = 0

while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** 3
    num = num // 10

if sum_of_cubes == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
```

**Example:**
- Input: 153
- Output: 153 is an Armstrong number.

---

### **3. Reverse a Number (Using for-loop)**
Write a program to reverse a given number using a `for` loop.

**Solution:**
```python
num = int(input("Enter a number: "))
reverse = 0
for digit in str(num):
    reverse = reverse * 10 + int(digit)

print("Reversed number:", reverse)
```

**Example:**
- Input: 6789
- Output: 9876

---

### **4. Check if a Number is an Armstrong Number (N-digit)**
Write a program to check if a number is an Armstrong number for any number of digits. An Armstrong number is a number equal to the sum of its digits raised to the power of the number of digits.

**Solution:**
```python
num = int(input("Enter a number: "))
num_of_digits = len(str(num))
original_num = num
sum_of_powers = 0

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** num_of_digits
    num = num // 10

if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
```

**Example:**
- Input: 9474
- Output: 9474 is an Armstrong number.

---

### **5. Check if a Number is an Armstrong Number (4-digit)**
Write a program to check if a 4-digit number is an Armstrong number. The number is an Armstrong number if the sum of its digits raised to the fourth power equals the number.

**Solution:**
```python
num = int(input("Enter a 4-digit number: "))
original_num = num
sum_of_powers = 0

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** 4
    num = num // 10

if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
```

**Example:**
- Input: 1634
- Output: 1634 is an Armstrong number.

---


---

### **1. Factorial of a Number (Using `while` loop)**
Write a program to calculate the factorial of a number using a `while` loop.

**Solution:**
```python
num = int(input("Enter a number: "))
factorial = 1

while num > 1:
    factorial *= num
    num -= 1

print("Factorial:", factorial)
```

**Example:**
- Input: 5
- Output: 120

---

### **2. Factorial of a Number (Using `for` loop)**
Write a program to calculate the factorial of a number using a `for` loop.

**Solution:**
```python
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)
```

**Example:**
- Input: 4
- Output: 24

---

### **3. Fibonacci Series (Up to Nth Term)**
Write a program to print the Fibonacci series up to the `n`-th term using a `for` loop.

**Solution:**
```python
n = int(input("Enter the number of terms: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

**Example:**
- Input: 7
- Output: 0 1 1 2 3 5 8

---

### **4. Fibonacci Series (Up to Nth Term Using `while` loop)**
Write a program to print the Fibonacci series up to the `n`-th term using a `while` loop.

**Solution:**
```python
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
```

**Example:**
- Input: 6
- Output: 0 1 1 2 3 5

---

### **5. Fibonacci Series (Nth Term)**
Write a program to find the `n`-th term of the Fibonacci series using a `while` loop.

**Solution:**
```python
n = int(input("Enter the position (n) of the Fibonacci series: "))
a, b = 0, 1
count = 1

while count < n:
    a, b = b, a + b
    count += 1

print(f"The {n}th term of the Fibonacci series is: {a}")
```

**Example:**
- Input: 6
- Output: The 6th term of the Fibonacci series is: 5


