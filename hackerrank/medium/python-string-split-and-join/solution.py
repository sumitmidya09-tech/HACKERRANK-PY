

def split_and_join(line):
    z=list(line)
    for i in range(len(z)):
        if " "==line[i]:
            z[i]="-"
            
        else:
            z[i]=line[i]
    return ''.join(z)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
