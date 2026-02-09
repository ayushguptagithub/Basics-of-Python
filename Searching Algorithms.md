## 🔍 1. Linear Search (Unsorted / Sorted)

```python
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Example
arr = [10, 40, 20, 50, 30]
key = 50
print(linear_search(arr, key))
```

## 🔍 2. Binary Search (Sorted Only)

```python
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example
arr = [10, 20, 30, 40, 50]
key = 30
print(binary_search(arr, key))
```

---

## 🔍 3. Jump Search (Sorted Only)

```python
import math

def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == key:
            return i

    return -1


# Example
arr = [10, 20, 30, 40, 50, 60, 70]
key = 60
print(jump_search(arr, key))
```

---

## 🔍 8. Hashing Search (Using Hash Table)

```python
def hashing_search(arr, key):
    hash_table = {}

    for i in range(len(arr)):
        hash_table[arr[i]] = i

    if key in hash_table:
        return hash_table[key]
    else:
        return -1


# Example
arr = [15, 25, 35, 45]
key = 35
print(hashing_search(arr, key))
```

---
