n=int(input())
l=list(map(int,input().split()))
d=int(input())
c=0
for i in range(len(l)):
    if l[i]==d:
        c=c+1
print(c)        
    

