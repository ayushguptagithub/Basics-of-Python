

### 1. **Digit Transformation Challenge**  
You are given an integer. Perform the following operations:  
1. Reverse the digits of the number.  
2. Compute the product of digits at prime index positions.  
3. Compute the sum of digits at non-prime index positions.  
4. Return the difference between the product and sum.  

**Example:**  
Input: `123456`  
Output:  
Reversed: `654321`  
Prime Index Product: `4 * 3 * 1 = 12`  
Non-Prime Index Sum: `6 + 5 + 2 = 13`  
Result: `12 - 13 = -1`  

---

### 2. **Cyclic Character Shift**  
You are given a string `S`. Perform the following operations:  
1. Convert all vowels to the next vowel in the sequence: `a → e`, `e → i`, `i → o`, `o → u`, `u → a`.  
2. Convert all consonants to the next consonant in the alphabet.  
3. Print the modified string.  

**Example:**  
Input: `hello`  
Output: `jimmu`  
Explanation:  
- `h → j`, `e → i`, `l → m`, `l → m`, `o → u`  

---

### 3. **Digit Alternating Sum**  
Given an integer `N`, reverse its digits and then compute the alternating sum:  
- Start with addition for the first digit.  
- Alternate between subtraction and addition for the following digits.  

**Example:**  
Input: `12345`  
Output:  
Reversed: `54321`  
Alternating Sum: `5 - 4 + 3 - 2 + 1 = 3`  

---

### 4. **Substring Rotation Check**  
You are given two strings, `A` and `B`. Determine if `B` is a rotated version of `A`.  

**Example:**  
Input:  
```
A = "abcde"
B = "cdeab"
```  
Output: `YES`  

---

### 5. **Index-Wise Character Shuffling**  
Given a string `S`,  
1. Extract characters at even indices and sort them.  
2. Extract characters at odd indices and reverse them.  
3. Merge them back while maintaining the original even-odd positions.  

**Example:**  
Input: `computer`  
Output: `cmtureop`  

---

### 6. **Number Spiral Diagonal Sum**  
You are given an `N × N` square matrix where numbers are filled in a spiral order. Find the sum of both diagonals.  

**Example:**  
For `N = 3`:  
```
1  2  3  
8  9  4  
7  6  5  
```  
Diagonal Sum: `1 + 9 + 5 + 3 + 7 = 25`  

---

### 7. **Sum of Odd and Even ASCII Values**  
Given a string, compute:  
1. The sum of ASCII values of characters at odd indices.  
2. The sum of ASCII values of characters at even indices.  
3. Return the absolute difference.  

**Example:**  
Input: `"abcd"`  
Output:  
Odd Index ASCII Sum: `98 + 100 = 198`  
Even Index ASCII Sum: `97 + 99 = 196`  
Result: `|198 - 196| = 2`  

---

### 8. **Digit Swapping Game**  
Given an integer `N`,  
1. Swap the first and last digit.  
2. Swap the second and second-last digit.  
3. Continue this pattern and return the new number.  

**Example:**  
Input: `123456`  
Output: `653421`  

---

### 9. **Mirror Image of a String**  
Given a string, replace each letter with its mirror image in the alphabet (`a ↔ z`, `b ↔ y`, etc.).  

**Example:**  
Input: `"abc"`  
Output: `"zyx"`  

---

### 10. **Prime Position Character Shift**  
Given a string `S`:  
1. Shift characters at prime indices forward by 2 positions in ASCII.  
2. Shift non-prime indexed characters backward by 1 position.  

**Example:**  
Input: `"abcdef"`  
Output: `"cbfdgd"`  

---
