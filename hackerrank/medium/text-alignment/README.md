# Text Alignment

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In Python, a string of text can be aligned *left, right* and *center*.

__.ljust(width)__

This method returns a left aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.ljust(width,'-')
    HackerRank----------  

---    
__.center(width)__

This method returns a centered string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.center(width,'-')
    -----HackerRank-----

---
__.rjust(width)__

This method returns a right aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.rjust(width,'-')
    ----------HackerRank
    
---
__Task__

You are given a partial code that is used for generating the _HackerRank Logo_ of variable _thickness_.  
Your task is to replace the blank (`______`) with *rjust, ljust* or *center*.




**Input Format**

 A single line containing the _thickness_ value for the logo.
 
 __Constraints__  

The *thickness* must be an *odd* number.  
$ 0 < thickness < 50$

**Output Format**

Output the desired logo.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T15:36:46.464Z  

```py
if __name__ == '__main__':
    t = int(input())
    s = 'H'
    l = t - 1
    rl = t - 1    
    def top(t, s, l):
        for x in range(t):
            Rjust = l + 1
            for x in range(2 * t - 2 * l - 1):
                print(s.rjust(Rjust), end = '')
                Rjust = 0
            l -= 1
            print("")    
    def middleTop(t, s, l):
        for x in range(t + 1):
            Rjust = t - t//2
            R1just = t * 3 + 1
            for x in range(t):
                print(s.rjust(Rjust), end = '')
                Rjust = 0
            for x in range(t):
                print(s.rjust(R1just), end = '')
                R1just = 0
            print("")    
    def middle(t, s, l):
        for x in range(t//2 + 1):
            Rjust = t - t//2
            for x in range(t * 5):
                print(s.rjust(Rjust), end = '')
                Rjust = 0
            print("")    
    def bottom(t, s, l, rl):
        for x in range(t):
            Rjust = 5 * t - l 
            for x in range((2 * t + 2 * rl) // 2):
                print(s.rjust(Rjust), end = '')
                Rjust = 0
            l -= 1
            rl -= 2
            print("")    
    top(t, s, l)
    middleTop(t, s, l)
    middle(t, s, l)
    middleTop(t, s, l)
    bottom(t, s, l, rl)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/text-alignment/problem)