n=input()
b=n.split()
g=[]
for i in b:
    g.append(ord(max(i))-ord(min(i)))
print(*g)    