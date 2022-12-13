def s(co,n,m):
    l=[]
    k=[]
    for i in range(n):
        c=0
        if i%2==0:
            for j in range(m):
                c+=co[i][j]
            l.append(c)
        else:
            d=0
            for j in range(m):
                d+=co[i][j]
            k.append(d)
    return sum(l),sum(k)
    
                
        
n,m=map(int,input().split())
row=[i for i in range(m)]
co=[row.copy() for i in range(n)]
for i in range(n):
    val=list(map(int,input().split()))
    for j in range(m):
        co[i][j]=val[j]
re=s(co,n,m)
print(*re)