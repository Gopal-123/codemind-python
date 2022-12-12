def c(i):
    c=0
    while i:
        i=i//10
        c+=1
    return c
k=[]
n=int(input())
l=list(map(int,input().split()))
for i in l:
    k.append(c(i))
c=0
for i in k:
    if i%2==0:
        c+=1
print(c)