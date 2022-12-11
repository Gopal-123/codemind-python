n=int(input())
l=list(map(int,input().split()))
k=[]
eo=[]
for i in l:
    if i not in k:
        k.append(i)
c=0
o=0
for i in l:
    if i%2==0:
        c+=1
    elif i%2:
        o+=1
eo.append(c)
eo.append(o)
print(*eo)