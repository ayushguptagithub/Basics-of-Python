Here are some pattern printing questions along with their solutions in Python:

---

### **1. Right-Angled Triangle Pattern**
#### **Pattern:**
```
*
* *
* * *
* * * *
* * * * *
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    print("* " * i)
```

---

### **2. Inverted Right-Angled Triangle**
#### **Pattern:**
```
* * * * *
* * * *
* * *
* *
*
```
#### **Code:**
```python
rows = 5
for i in range(rows, 0, -1):
    print("* " * i)
```

---

### **3. Pyramid Pattern**
#### **Pattern:**
```
    *
   * *
  * * *
 * * * *
* * * * *
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
```

---

### **4. Inverted Pyramid Pattern**
#### **Pattern:**
```
* * * * *
 * * * *
  * * *
   * *
    *
```
#### **Code:**
```python
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)
```

---

### **5. Diamond Pattern**
#### **Pattern:**
```
    *    
   * *   
  * * *  
 * * * * 
* * * * *
 * * * * 
  * * *  
   * *   
    *    
```
#### **Code:**
```python
rows = 5

# Upper Part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower Part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
```

---

Here are more pattern printing questions with their Python solutions:

---

### **6. Hollow Square Pattern**
#### **Pattern:**
```
* * * * *
*       *
*       *
*       *
* * * * *
```
#### **Code:**
```python
rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("* " * rows)
    else:
        print("* " + "  " * (rows - 2) + "*")
```

---

### **7. Hollow Pyramid Pattern**
#### **Pattern:**
```
    *    
   * *   
  *   *  
 *     * 
*********
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    if i == 1 or i == rows:
        print(" " * (rows - i) + "* " * i)
    else:
        print(" " * (rows - i) + "* " + "  " * (i - 2) + "*")
```


---

### **8. Hourglass Pattern**
#### **Pattern:**
```
* * * * * * * 
  * * * * *   
    * * *     
      *       
    * * *     
  * * * * *   
* * * * * * * 
```
#### **Code:**
```python
rows = 4

# Upper part
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * (2 * i - 1))

# Lower part
for i in range(2, rows + 1):
    print(" " * (rows - i) + "* " * (2 * i - 1))
```

Here are some more pattern printing questions using simple `for` loops and basic logic:  

---

### **13. Square Pattern**
#### **Pattern:**  
```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```
#### **Code:**
```python
rows = 5
for i in range(rows):
    print("* " * rows)
```

---

### **14. Right-Angled Number Triangle**  
#### **Pattern:**  
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

### **15. Right-Angled Number Reverse Triangle**  
#### **Pattern:**  
```
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```
#### **Code:**
```python
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

### **16. Right-Angled Triangle with Same Number**  
#### **Pattern:**  
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()
```

---

### **17. Left-Aligned Right-Angled Triangle**  
#### **Pattern:**  
```
        *
      * *
    * * *
  * * * *
* * * * *
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    print("  " * (rows - i) + "* " * i)
```

---

### **18. Left-Aligned Inverted Triangle**  
#### **Pattern:**  
```
* * * * *
  * * * *
    * * *
      * *
        *
```
#### **Code:**
```python
rows = 5
for i in range(rows, 0, -1):
    print("  " * (rows - i) + "* " * i)
```

---

### **19. Number Pyramid**  
#### **Pattern:**  
```
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + (str(i) + " ") * i)
```

---

### **20. Number Mirror Pyramid**  
#### **Pattern:**  
```
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    print()
```

---

### **21. Simple Alternating 0-1 Triangle**  
#### **Pattern:**  
```
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()
```

---

### **22. Character Triangle**  
#### **Pattern:**  
```
A
A B
A B C
A B C D
A B C D E
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
```

---

### **23. Character Pyramid**  
#### **Pattern:**  
```
    A
   A B
  A B C
 A B C D
A B C D E
```
#### **Code:**
```python
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + " ".join(chr(65 + j) for j in range(i)))
```

---

### **24. Inverted Character Triangle**  
#### **Pattern:**  
```
A B C D E
A B C D
A B C
A B
A
```
#### **Code:**
```python
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
```

