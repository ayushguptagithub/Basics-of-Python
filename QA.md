

### **1. Reverse a List Without Using `reverse()`**
#### **Input:**  
`[1, 2, 3, 4, 5]`  
#### **Output:**  
`[5, 4, 3, 2, 1]`  
#### **Code:**
```python
arr = [1, 2, 3, 4, 5]
reversed_arr = []

for i in range(len(arr) - 1, -1, -1):  # Traverse from last to first
    reversed_arr.append(arr[i])

print(reversed_arr)
```

---

### **2. Find Maximum and Minimum in a List**
#### **Input:**  
`[12, 5, 20, 8]`  
#### **Output:**  
`(20, 5)`  
#### **Code:**
```python
arr = [12, 5, 20, 8]
max_val = arr[0]
min_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(max_val, min_val)
```

---

### **3. Sum of List Elements Without `sum()`**
#### **Input:**  
`[1, 2, 3, 4, 5]`  
#### **Output:**  
`15`  
#### **Code:**
```python
arr = [1, 2, 3, 4, 5]
total = 0

for num in arr:
    total += num

print(total)
```

---

### **4. Check if a List is Palindrome**
#### **Input:**  
`[1, 2, 3, 2, 1]`  
#### **Output:**  
`True`  
#### **Code:**
```python
arr = [1, 2, 3, 2, 1]
is_palindrome = True

for i in range(len(arr) // 2):  # Compare first half with second half
    if arr[i] != arr[-(i + 1)]:
        is_palindrome = False
        break

print(is_palindrome)
```

---

### **5. Remove Duplicates from a List**
#### **Input:**  
`[1, 2, 2, 3, 4, 4, 5]`  
#### **Output:**  
`[1, 2, 3, 4, 5]`  
#### **Code:**
```python
arr = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for num in arr:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)
```

---

### **6. Find the Second Largest Element**
#### **Input:**  
`[12, 35, 1, 10, 34, 1]`  
#### **Output:**  
`34`  
#### **Code:**
```python
arr = [12, 35, 1, 10, 34, 1]
largest = second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)
```

---

### **7. Merge Two Sorted Lists Without `sorted()`**
#### **Input:**  
`[1, 3, 5]`, `[2, 4, 6]`  
#### **Output:**  
`[1, 2, 3, 4, 5, 6]`  
#### **Code:**
```python
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = []
i, j = 0, 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1

print(merged)
```

---

### **8. Rotate a List by `k` Positions**
#### **Input:**  
`[1, 2, 3, 4, 5]`, `k = 2`  
#### **Output:**  
`[4, 5, 1, 2, 3]`  
#### **Code:**
```python
arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)

rotated = arr[-k:] + arr[:-k]  # Slicing method to rotate
print(rotated)
```

---

### **9. Find Pairs with a Given Sum**
#### **Input:**  
`[2, 4, 3, 5, 7, 8, 9]`, `target = 10`  
#### **Output:**  
`[(2, 8), (3, 7)]`  
#### **Code:**
```python
arr = [2, 4, 3, 5, 7, 8, 9]
target = 10
pairs = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))

print(pairs)
```

---

### **10. Find the Missing Number in a Consecutive List**
#### **Input:**  
`[1, 2, 4, 5, 6]`  
#### **Output:**  
`3`  
#### **Code:**
```python
arr = [1, 2, 4, 5, 6]
n = len(arr) + 1  # One missing number
expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
actual_sum = sum(arr)

missing_num = expected_sum - actual_sum
print(missing_num)
```

---

### **11. Find Intersection of Two Lists**
#### **Input:**  
`[1, 2, 3, 4]`, `[2, 4, 6, 8]`  
#### **Output:**  
`[2, 4]`  
#### **Code:**
```python
arr1 = [1, 2, 3, 4]
arr2 = [2, 4, 6, 8]
intersection = []

for num in arr1:
    if num in arr2 and num not in intersection:
        intersection.append(num)

print(intersection)
```

---

### **12. Find Subarrays with Zero Sum**
#### **Input:**  
`[4, 2, -3, 1, 6]`  
#### **Output:**  
`[(2, -3, 1)]`  
#### **Code:**
```python
arr = [4, 2, -3, 1, 6]

for i in range(len(arr)):
    sum_ = 0
    for j in range(i, len(arr)):
        sum_ += arr[j]
        if sum_ == 0:
            print(arr[i:j+1])
```

---
