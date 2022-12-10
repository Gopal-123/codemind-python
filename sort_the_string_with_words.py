n=input()
b=n.split()
f=[]
g=[]
for i in b:
    for j in b:
        if i[0]==j[0]:
            f.append(j)
for i in f:
    if i not in g:
        g.append(i)
g.sort()
print(*g)