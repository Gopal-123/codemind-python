l=list(map(int,input().split(',')))
g=[]
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=j
    if c in l:
        g.append(i)
if len(g)==0:
    print("-1")
else:
    g.sort()
    print(*g)