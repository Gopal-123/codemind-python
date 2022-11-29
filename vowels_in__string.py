n=input()
s=[97,101,105,111,117,65,69,73,79,85]
g=[]
for i in n:
    if ord(i) in s:
        if i not in g:
            g.append(i)
print(*g)
        