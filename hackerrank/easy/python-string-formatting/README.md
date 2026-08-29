# Designer Door Mat

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer, $n$, print the following values for each integer $i$ from $1$ to $n$:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

**Function Description**   

Complete the *print_formatted* function in the editor below.   

*print_formatted* has the following parameters:   

-	*int number:* the maximum value to print  

**Prints**   

The four values must be printed on a single line *in the order specified above* for each $i$ from $1$ to $number$. Each value should be space-padded to match the width of the *binary* value of $number$ and the values should be separated by a single space.

**Input Format**

A single integer denoting $n$.

**Constraints**

- $1 \le n \le 99$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T03:50:30.742Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
for i in range(n):
    if i > n//2:
        mirror_i = n-i-1
        row = ((".|." * (2*(mirror_i) + 1)).center(m, "-"))
        print(row)
    elif i == n // 2:
        print("WELCOME".center(m, "-"))
    else:
        row = (".|." * (2*i + 1)).center(m, "-")
        print(row)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-string-formatting/problem)