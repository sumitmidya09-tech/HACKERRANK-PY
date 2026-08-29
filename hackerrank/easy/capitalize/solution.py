

# Complete the solve function below.
def solve(s):
     l=s.split(" ") 
     l=[ sub if sub.isdigit() else sub.capitalize() for sub in l]
     return " ".join(l)
