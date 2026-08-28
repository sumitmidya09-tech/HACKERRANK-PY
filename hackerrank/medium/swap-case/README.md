# sWAP cASE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string and your task is to *swap cases*. In other words, convert all lowercase letters to uppercase letters and vice versa.

**For Example:**

    Www.HackerRank.com → wWW.hACKERrANK.COM
    Pythonist 2 → pYTHONIST 2  
    
    
**Function Description**   

Complete the *swap_case* function in the editor below.   

*swap_case* has the following parameters:   

- *string s:* the string to modify   

**Returns**   

- *string:* the modified string   

**Input Format**

A single line containing a string $s$.





**Constraints**

$0 \lt len(s) \le 1000$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T15:32:53.654Z  

```py
def swap_case(s):
    z=list(s)
    for i in range(len(z)):
        if z[i]==z[i].lower():
            z[i]=z[i].upper()
        else:
            z[i]=z[i].lower()
    return "".join(z)


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/swap-case/problem)