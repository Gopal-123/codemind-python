n=int(input())
row = [[] for i in range(n)]
d=[row.copy() for i in range(n)]
for i in range(n):
    v=list(map(int,input().split()))
    for j in range(n):
       d[i][j]=v[j]
row1 = [[] for i in range(n)]
d1=[row1.copy() for i in range(n)]
for i in range(n):
    v=list(map(int,input().split()))
    for j in range(n):
       d1[i][j]=v[j]
row2 = [[] for i in range(n)]
d2=[row2.copy() for i in range(n)]
for i in range(len(d)):
    c=0
    for j in range(len(d[i])):
        a=abs(d[i][j]-d1[i][j])
        d2[i][j]=a
for i in d2:
    print(*i)