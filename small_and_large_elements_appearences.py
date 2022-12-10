n=input()
f=[]
g=[]
for i in n:
    if i==" ":
        pass
    else:
        f.append(i)
g.append(min(f))
g.append(f.count(min(f)))
g.append(max(f))
g.append(f.count(max(f)))
print(*g)