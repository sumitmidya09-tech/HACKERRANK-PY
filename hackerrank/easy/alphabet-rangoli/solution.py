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
