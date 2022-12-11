n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(100):
    if i*i in l:
        sum=sum+i*i
print(sum)