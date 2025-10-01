
---

# 🔹 Q1

```python
class Demo:
    @staticmethod
    def specialAdd(num1):
        if num1 != 0:
            return (num1 + 2) + Demo.specialAdd(num1 - 1)
        else:
            return 3

    @staticmethod
    def extraordinaryAdd(num2):
        if num2 != 0:
            return Demo.specialAdd(num2) + Demo.extraordinaryAdd(num2 - 1)
        else:
            return 0

print(Demo.extraordinaryAdd(5))
```

a. 80

b. 52

c. 70

d. 25

---

# 🔹 Q2

```python
def mystery(n):
    if n <= 0:
        return
    mystery(n - 1)
    print(n, end=" ")
    mystery(n - 2)

mystery(3)
```

a. 1 2 3 1

b. 1 2 3 2 1

c. 3 2 1 2 1

d. 1 2 1 3 2 1

---

# 🔹 Q3

```python
def fun(n):
    if n == 0:
        return
    fun(n // 2)
    print(n % 2, end="")

fun(13)
```

a. 1011

b. 1101

c. 1110

d. 0110

---

# 🔹 Q4

```python
def reverse(n, rev):
    if n == 0:
        return rev
    return reverse(n // 10, rev * 10 + n % 10)

print(reverse(1234, 0))
```

a. 1234

b. 0

c. 4321

d. Compilation Error

---

# 🔹 Q5

```python
def zigzag(n):
    if n <= 0:
        return
    print(n, end=" ")
    zigzag(n - 1)
    print(n, end=" ")
    zigzag(n - 2)
    print(n, end=" ")

zigzag(2)
```

a. 2 1 1 2 1 2

b. 1 1 2 2 1 1

c. Infinity

d. 2 1 1 1 2 2

---

# 🔹 Q6

```python
def mystery(n):
    if n == 0:
        return 1
    return n * mystery(n - 1) + mystery(n - 1)

print(mystery(3))
```

a. 24

b. 26

c. 32

d. 22

---

# 🔹 Q7

```python
def recurse(n):
    if n == 0:
        return
    print(n, end=" ")
    if n % 2 == 0:
        recurse(n - 2)
    else:
        recurse(n - 1)
    print(n, end=" ")

recurse(4)
```

a. 4 4 2 2

b. 4 2 2 4

c. 2 4 2 4

d. 4 2 4 4

---

# 🔹 Q8

```python
def weird(a, b):
    if b == 0:
        return 0
    return weird(a + a, b // 2) if b % 2 == 0 else weird(a + a, b // 2) + a

print(weird(3, 5))
```

a. 15

b. 8

c. 0

d. Compilation Error

---

# 🔹 Q9

```python
def oddEvenRec(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return oddEvenRec(n - 1) - 1
    else:
        return oddEvenRec(n - 1) + 1

print(oddEvenRec(5))
```

a. 0

b. 1

c. 11

d. Compilation Error

---

# 🔹 Q10

```python
def trickyPrint(n):
    if n == 0:
        return
    trickyPrint(n - 1)
    print(n, end=" ")
    trickyPrint(n - 1)

trickyPrint(3)
```

a. 2 1 1 2 3 1 2

b. 3 3 3 2 2 2 1

c. 1 2 1 1 2 2 3

d. 1 2 1 3 1 2 1

---
