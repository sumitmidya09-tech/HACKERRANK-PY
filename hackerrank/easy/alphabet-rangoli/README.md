# Alphabet Rangoli

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer, $N$. Your task is to print an alphabet rangoli of size $N$.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

```
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
```

The center of the rangoli has the first alphabet letter *a*, and the boundary has the $N$$^{th}$ alphabet letter (in alphabetical order).   

**Function Description**   

Complete the *rangoli* function in the editor below.   

*rangoli* has the following parameters:   

- *int size:*  the size of the rangoli  

**Returns**   

- *string:* a single string made up of each of the lines of the rangoli separated by a newline character (\n)

**Input Format**

Only one line of input containing $size$, the size of the rangoli.


**Constraints**

$ 0 < size < 27 $

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T03:57:08.227Z  

```py
def print_rangoli(size):
    # your code goes here
    rows = size*2-1
    columns = (n*2-1)+(n*2-2)
    k = (rows // 2)+1
    j = k - 1

    for i in range(1,rows+1):
        if(k >= i):
            l1 = [chr(x) for x in range((96+size),(96+size-i),-1)]
            l2 = [chr(x) for x in range((96+size-i+2),(96+size+1))]       
        else:
            l1 = [chr(x) for x in range((96+size),(96+size-j),-1)]
            l2 = [chr(x) for x in range((96+size-j+2),(96+size+1))]          
            j -= 1
        l = l1+l2
        string = '-'.join(l)
        print(string.center(columns,'-'))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/alphabet-rangoli/problem)