n=int(input())
l=list(map(int,input().split()))
g=[]
s=0
c=0
for i in l:
    s=s+i
a=s//len(l)    
for i in l:
    if i<=a:
        c=c+1
print(c)        