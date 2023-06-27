r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    v=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=v[j]
l=[]
for i in range(len(d)):
    c=0
    for j in range(len(d[i])):
        c+=d[i][j]
    l.append(c)
print(max(l))
    
