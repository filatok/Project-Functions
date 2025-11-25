def wordScore(s):
    n=0
    s = s.lower()
    for i in s:
        if i=='a' or i=='o' or i=='e' or i=='i' or i=='y':
            n+=2
        elif i=='m' or i=='r' or i=='g':
            n+=3
        else:
            n+=1
    return n


s = input("Word: ")
print(wordScore(s))
print("gfds")