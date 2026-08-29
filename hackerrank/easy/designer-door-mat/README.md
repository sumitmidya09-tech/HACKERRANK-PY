# Designer Door Mat

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications: 

- Mat size must be $N  $X$  M$. ($N$ is an odd natural number, and $M$ is $3$ times $N$.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use `|`, `.` and `-` characters.

__Sample Designs__

```
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
```    



**Input Format**

A single line containing the space separated values of $N$ and $M$.  


**Constraints**

+ $5 < N < 101$
+ $15 < M < 303$

**Output Format**

Output the design pattern.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T03:50:14.538Z  

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

[View on HackerRank](https://www.hackerrank.com/challenges/designer-door-mat/problem)