def minion_game(string):
    # your code goes here
    Vowels = "AEIOU"
    Kevin = 0
    Stuart = 0
    
    for i in range(len(s)):
        if s[i] in Vowels:
            Kevin += (len(s)-i) 

        else :
            Stuart += len(s)-i 
    if Kevin > Stuart:
        print("Kevin",Kevin)
    elif Kevin == Stuart:
        print("Draw")
    else:
        print("Stuart",Stuart)
