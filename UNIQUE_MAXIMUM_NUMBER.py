n=int(input())
l=list(map(int,input().split()))
u=[]
for i in l:
    if l.count(i)==1:
        u.append(i)
if len(u)==0:
    print("-1")
else:
    print(max(u))