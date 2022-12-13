def e(col,r,c):
    co=0
    for i in range(r):
        for j in range(c):
            co+=col[i][j]
    print(co)
r,c=map(int,input().split())
row=[[] for i in range(c)]
col=[row.copy() for i in range(r)]
for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        col[i][j]=val[j]
re=e(col,r,c)