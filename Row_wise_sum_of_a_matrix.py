r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    v=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=v[j]
l=[]
for i in d:
    l.append(sum(i))
print(*l)