def c(i):
    d=0
    while i:
        i=i//10
        d+=1
    return d  


n=int(input())
l=list(map(int,input().split()))
a=[]
k=[]
for i in l:
    a.append(c(abs(i)))
for i in a:
    if i==max(a):
        k.append(i)
for i in l:
    if c(abs(i)) in k:
        print(i,end=" ")