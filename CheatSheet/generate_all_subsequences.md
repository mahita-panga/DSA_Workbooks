## Recursive Approach (Backtracking)
BRUTEFORCE:
The classic recursive approach considers each element and chooses either to include it in the current subsequence or to skip it.
This generates all possible subsequences by exploring both choices for each element.

```python
def generate_subsequences(arr):
    result = []

    def backtrack(index, current):
        if index == len(arr):
            result.append(current[:])  # Add the current subsequence
            return
        # Include the current element
        current.append(arr[index])
        backtrack(index + 1, current)
        # Exclude the current element (backtrack)
        current.pop()
        backtrack(index + 1, current)

    backtrack(0, [])
    return result
```
**Time Complexity**: O(2^n), where n is the length of the array.
**Space Complexity**: O(n) for the recursion stack.


## Iterative Approach with Bit Manipulation:
Using bitwise operations, we can generate all subsequences by representing each element’s inclusion or exclusion as a bit in a binary number.
By checking if the jth bit is set


```python
def generate_subsequences(arr):
    n = len(arr)
    result = []
    for i in range(1 << n):  # 2^n possible subsequences
        subseq = []
        for j in range(n):
            if i & (1 << j):  # Check if the j-th bit is set -> 000,001,010,011 ...
                subseq.append(arr[j]) #jth bit set helps us generate subsequence for set elements
        result.append(subseq)
    return result

# Usage
arr = [1, 2, 3]
print(generate_subsequences(arr))
```
**Time Complexity : O(2^n)**
**Space Complexity : O(2^n) for storing results.**

## Using Python itertools.combinations (All Lengths)

```python
from itertools import combinations

def generate_subsequences(arr):
    result = []
    n = len(arr)
    for length in range(n + 1):  # Generate subsequences of each length
        for comb in combinations(arr, length):
            result.append(list(comb))
    return result
```

SAME TC and SC as others

## Using Dynamic Programming to Generate All Subsequences
For each element in arr, we append it to all previously generated subsequences.
This method is efficient for generating all subsequences in an iterative manner without recursion.
```python
def generate_subsequences(arr):
    result = [[]]  # Start with an empty subsequence
    for num in arr:
        result += [curr + [num] for curr in result]
    return result
```

**Time Complexity : O(2^n)**
**Space Complexity : O(2^n) for storing results.**


## GENERATING ALL SUBSTRINGS <-Backtracking->
The logic is similar to arrays, where each character is either included or excluded.
```python
def generate_subsequences(s):
    result = []

    def backtrack(index, current):
        if index == len(s):
            result.append("".join(current))
            return
        # Include the current character
        current.append(s[index])
        backtrack(index + 1, current)
        # Exclude the current character (backtrack)
        current.pop()
        backtrack(index + 1, current)

    backtrack(0, [])
    return result
```

**Time Complexity**: O(2^n), where n is the length of the array.
**Space Complexity**: O(n) for the recursion stack.
