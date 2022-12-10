n=input()
b=n.split()
f=[]
g=[]
h=0
for i in b:
    i=len(i)
    if i>h:
        h=i
for i in range(1,h+1):
    for j in b:
        if len(j)==i:
            f.append(j)
    f.sort()
    c=list(f)
    for m in c:
        g.append(m)
    f.clear()
print(*g)

