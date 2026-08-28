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
