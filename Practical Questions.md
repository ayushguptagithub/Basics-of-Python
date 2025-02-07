
### 1. Reverse a List  
**Question**: Write a Python program to reverse a list without using any built-in functions.  
**Solution**:
```python
# Input list
lst = [1, 2, 3, 4, 5]
reversed_lst = []

# Reversing the list
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])

print("Reversed List:", reversed_lst)
```

---

### 2. Find the Maximum Element  
**Question**: Write a Python program to find the maximum element in a list without using `max()`.  
**Solution**:
```python
# Input list
lst = [10, 20, 30, 5, 15]
max_element = lst[0]

# Finding the maximum element
for num in lst:
    if num > max_element:
        max_element = num

print("Maximum Element:", max_element)
```

---

### 3. Find the Second Largest Element  
**Question**: Write a Python program to find the second largest element in a list.  
**Solution**:
```python
# Input list
lst = [12, 35, 1, 10, 34, 1]
largest = second_largest = float('-inf')

# Finding the second largest element
for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Element:", second_largest)
```

---

### 4. Remove Duplicates from a List  
**Question**: Write a Python program to remove duplicates from a list without using `set()`.  
**Solution**:
```python
# Input list
lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = []

# Removing duplicates
for num in lst:
    if num not in unique_lst:
        unique_lst.append(num)

print("List without Duplicates:", unique_lst)
```

---

### 5. Rotate a List to the Left  
**Question**: Write a Python program to rotate a list to the left by `k` positions.  
**Solution**:
```python
# Input list and rotation count
lst = [1, 2, 3, 4, 5]
k = 2
rotated_lst = []

# Rotating the list
n = len(lst)
for i in range(n):
    rotated_lst.append(lst[(i + k) % n])

print("Left Rotated List:", rotated_lst)
```

---

### 6. Merge Two Sorted Lists  
**Question**: Write a Python program to merge two sorted lists into a single sorted list without using `sorted()`.  
**Solution**:
```python
# Input sorted lists
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged_lst = []

# Merging the lists
i = j = 0
while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged_lst.append(lst1[i])
        i += 1
    else:
        merged_lst.append(lst2[j])
        j += 1

# Adding remaining elements
while i < len(lst1):
    merged_lst.append(lst1[i])
    i += 1

while j < len(lst2):
    merged_lst.append(lst2[j])
    j += 1

print("Merged Sorted List:", merged_lst)
```

---

### 7. Check if a List is a Palindrome  
**Question**: Write a Python program to check if a list is a palindrome.  
**Solution**:
```python
# Input list
lst = [1, 2, 3, 2, 1]
is_palindrome = True

# Checking for palindrome
for i in range(len(lst) // 2):
    if lst[i] != lst[len(lst) - 1 - i]:
        is_palindrome = False
        break

print("Is Palindrome:", is_palindrome)
```

---

### 8. Count the Frequency of Elements  
**Question**: Write a Python program to count the frequency of each element in a list.  
**Solution**:
```python
# Input list
lst = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}

# Counting frequencies
for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequencies:", freq)
```


---

### 1. Reverse a String  
**Question**: Write a Python program to reverse a string without using any built-in functions.  
**Solution**:
```python
# Input string
s = "hello"
reversed_s = ""

# Reversing the string
for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]

print("Reversed String:", reversed_s)
```

---

### 2. Check if a String is a Palindrome  
**Question**: Write a Python program to check if a string is a palindrome.  
**Solution**:
```python
# Input string
s = "racecar"
is_palindrome = True

# Checking for palindrome
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        is_palindrome = False
        break

print("Is Palindrome:", is_palindrome)
```

---

### 3. Find the Frequency of Characters  
**Question**: Write a Python program to count the frequency of each character in a string.  
**Solution**:
```python
# Input string
s = "hello"
freq = {}

# Counting frequencies
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequencies:", freq)
```

---

### 4. Check if Two Strings are Anagrams  
**Question**: Write a Python program to check if two strings are anagrams of each other.  
**Solution**:
```python
# Input strings
s1 = "listen"
s2 = "silent"

# Checking if they are anagrams
if len(s1) != len(s2):
    is_anagram = False
else:
    freq1 = {}
    freq2 = {}
    
    # Count characters in both strings
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    is_anagram = freq1 == freq2

print("Are Anagrams:", is_anagram)
```

---

### 5. Find the First Non-Repeating Character  
**Question**: Write a Python program to find the first non-repeating character in a string.  
**Solution**:
```python
# Input string
s = "swiss"
freq = {}

# Counting frequencies
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Finding the first non-repeating character
first_non_repeating = None
for char in s:
    if freq[char] == 1:
        first_non_repeating = char
        break

print("First Non-Repeating Character:", first_non_repeating)
```

---

### 6. Remove Duplicates from a String  
**Question**: Write a Python program to remove duplicate characters from a string.  
**Solution**:
```python
# Input string
s = "programming"
result = ""

# Removing duplicates
for char in s:
    if char not in result:
        result += char

print("String without Duplicates:", result)
```

---

### 7. Count the Number of Vowels and Consonants  
**Question**: Write a Python program to count the number of vowels and consonants in a string.  
**Solution**:
```python
# Input string
s = "hello world"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

# Counting vowels and consonants
for char in s:
    if char.isalpha():  # Check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
```

---

### 8. Find All Substrings of a String  
**Question**: Write a Python program to find all substrings of a given string.  
**Solution**:
```python
# Input string
s = "abc"
substrings = []

# Generating all substrings
for i in range(len(s)):
    for j in range(i, len(s)):
        substrings.append(s[i:j + 1])

print("Substrings:", substrings)
```

---

### 9. Check if a String Contains Only Unique Characters  
**Question**: Write a Python program to check if a string contains only unique characters.  
**Solution**:
```python
# Input string
s = "abcdef"
has_unique_chars = True

# Checking for unique characters
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            has_unique_chars = False
            break
    if not has_unique_chars:
        break

print("Has Only Unique Characters:", has_unique_chars)
```

---

### 10. Find the Longest Word in a Sentence  
**Question**: Write a Python program to find the longest word in a sentence.  
**Solution**:
```python
# Input sentence
sentence = "The quick brown fox jumps over the lazy dog"
words = []
word = ""

# Splitting sentence into words
for char in sentence:
    if char != " ":
        word += char
    else:
        words.append(word)
        word = ""
words.append(word)  # Add the last word

# Finding the longest word
longest_word = ""
for w in words:
    if len(w) > len(longest_word):
        longest_word = w

print("Longest Word:", longest_word)
```

---
