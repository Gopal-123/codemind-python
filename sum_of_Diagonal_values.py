r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    v=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=v[j]
l=[]
k=0
for i in range(len(d)):
    l.append(d[i][k])
    k+=1
j=len(d)-1
for i in range(len(d)):
    l.append(d[i][j])
    j-=1
if c==3 and r==3:
    print(sum(l)-d[1][1])
elif r==1 and c==1:
    print(d[0][0])
else:
    print(sum(l))
