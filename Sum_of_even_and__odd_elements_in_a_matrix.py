def e(col,r,c):
    l=[]
    m=0
    d=0
    for i in range(r):
        for j in range(c):
            if col[i][j]%2==0:
                m+=col[i][j]
            else:
                d+=col[i][j]
    print(m,d)

    
                
    


r,c=map(int,input().split())
row=[[] for i in range(c)]
col=[row.copy() for i in range(r)]
for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        col[i][j]=val[j]
re=e(col,r,c)