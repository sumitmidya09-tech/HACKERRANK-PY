def merge_the_tools(string, k):
    # your code goes here
    st = set()
    for i in range(0, len(string)):
        if i%k==0 and i!=0:
            st=set()
            print()
        if string[i] not in st:
            print(string[i], end="")
            st.add(string[i])
