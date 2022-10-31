n=int(input())
l=list(map(int,input().split()))
c=0
e=0
for i in range(len(l)):
    if i%2==0:
        c=c+l[i]
    else:
        e=e+l[i]
print(abs(c-e))        
        
        
