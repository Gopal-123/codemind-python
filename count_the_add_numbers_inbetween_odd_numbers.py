n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,len(l)-1):
    if l[i]%2 and l[i+1]%2 and l[i-1]%2:
        c=c+1
print(c)        
        