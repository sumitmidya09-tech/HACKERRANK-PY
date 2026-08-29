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
