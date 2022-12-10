n=input()
b=n.split()
g=[]
for i in b:
    g.append(min(i))
    g.append(max(i))
print(*g)