n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]%2==0:
        c=i
print(c)        
    