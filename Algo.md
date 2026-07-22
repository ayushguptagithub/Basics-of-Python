The **Sliding Window** technique is an optimization method used to solve problems involving **subarrays** or **substrings** efficiently. Instead of checking every possible subarray (which takes **O(n²)**), we maintain a "window" and slide it across the array/string, reducing the time complexity to **O(n)** in many cases.

---

# Types of Sliding Window

## 1. Fixed Size Sliding Window

The window size is constant.

### Example

Find the maximum sum of any subarray of size `k`.

### Brute Force

* Find every subarray of size `k`
* Calculate its sum

Time Complexity: **O(n × k)**

### Sliding Window

1. Calculate sum of first `k` elements.
2. Store it as answer.
3. Slide window one position:

   * Remove left element.
   * Add new right element.
4. Update maximum.

### Java Code

```java
public class FixedWindow {
    public static int maxSum(int[] arr, int k) {
        int sum = 0;

        for (int i = 0; i < k; i++)
            sum += arr[i];

        int max = sum;

        for (int i = k; i < arr.length; i++) {
            sum = sum - arr[i - k] + arr[i];
            max = Math.max(max, sum);
        }

        return max;
    }

    public static void main(String[] args) {
        int[] arr = {2,1,5,1,3,2};
        int k = 3;

        System.out.println(maxSum(arr, k));
    }
}
```

Output

```
9
```

Subarray = `[5,1,3]`

Time Complexity: **O(n)**

Space Complexity: **O(1)**

---

# Dry Run

Array

```
2 1 5 1 3 2
```

Window Size = 3

Initial Window

```
[2 1 5] = 8
```

Slide

```
Remove 2
Add 1

[1 5 1] = 7
```

Slide

```
Remove 1
Add 3

[5 1 3] = 9
```

Slide

```
Remove 5
Add 2

[1 3 2] = 6
```

Maximum = **9**

---

# 2. Variable Size Sliding Window

The window size changes depending on a condition.

Example:

* Longest substring without repeating characters
* Smallest subarray with sum ≥ K
* Maximum consecutive ones

---

## General Algorithm

```
left = 0

for(right = 0 to n-1){

    expand window

    while(condition is false){
        shrink window
        left++
    }

    update answer
}
```

---

# Example

Longest Substring Without Repeating Characters

Input

```
abcabcbb
```

Output

```
3
```

Substring

```
abc
```

### Java Code

```java
import java.util.HashSet;

public class VariableWindow {

    public static int lengthOfLongestSubstring(String s) {

        HashSet<Character> set = new HashSet<>();

        int left = 0;
        int max = 0;

        for (int right = 0; right < s.length(); right++) {

            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }

            set.add(s.charAt(right));
            max = Math.max(max, right - left + 1);
        }

        return max;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abcabcbb"));
    }
}
```

Output

```
3
```

Time Complexity

```
O(n)
```

---

# When to Use Sliding Window

Use it when the problem involves:

* ✅ Contiguous subarray
* ✅ Contiguous substring
* ✅ Longest/Shortest window
* ✅ Maximum/Minimum window
* ✅ Fixed size `k`
* ✅ Sum/Average/Product
* ✅ Distinct characters/elements
* ✅ At most K / Exactly K elements

---

# Common LeetCode Problems

| Problem                                           | Difficulty        | Type     |
| ------------------------------------------------- | ----------------- | -------- |
| 643. Maximum Average Subarray I                   | Easy              | Fixed    |
| 209. Minimum Size Subarray Sum                    | Medium            | Variable |
| 3. Longest Substring Without Repeating Characters | Medium            | Variable |
| 424. Longest Repeating Character Replacement      | Medium            | Variable |
| 567. Permutation in String                        | Medium            | Fixed    |
| 438. Find All Anagrams in a String                | Medium            | Fixed    |
| 1004. Max Consecutive Ones III                    | Medium            | Variable |
| 904. Fruit Into Baskets                           | Medium            | Variable |
| 76. Minimum Window Substring                      | Hard              | Variable |
| 239. Sliding Window Maximum                       | Hard (uses Deque) | Fixed    |

---

# Sliding Window Pattern

### Fixed Size

```java
// Create first window
for(int i = 0; i < k; i++)
    sum += arr[i];

for(int i = k; i < arr.length; i++){
    sum -= arr[i - k];
    sum += arr[i];
}
```

### Variable Size

```java
int left = 0;

for(int right = 0; right < n; right++){

    // Expand window

    while(window is invalid){
        // Shrink window
        left++;
    }

    // Update answer
}
```

---

## How to Identify a Sliding Window Problem

Ask yourself:

1. Is the problem about a **contiguous** subarray or substring?
2. Do I need the **longest**, **shortest**, **maximum**, or **minimum** contiguous segment?
3. Can I update the answer by adding one element and removing one element instead of recalculating everything?

If the answer is **yes**, the sliding window technique is often the right approach.
