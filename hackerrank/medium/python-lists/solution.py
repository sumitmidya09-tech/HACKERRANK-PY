if __name__ == '__main__':
    N = int(input())
    list=[]
    pi=[]
  
    for i in range (N):
        list.append(input().split())
    for j in list:
        if "insert"==j[0]:
            pi.insert(int(j[1]), int(j[2]))
        elif j[0]=="append":
            pi.append(int(j[1]))
        elif j[0]=="print":
            print(pi)
        elif j[0]=="remove":
            pi.remove(int(j[1]))
        elif j[0]=="sort":
            pi.sort()
        elif j[0]=="pop":
            pi.pop(-1)
        elif j[0]=="reverse":
            pi.reverse()



 
