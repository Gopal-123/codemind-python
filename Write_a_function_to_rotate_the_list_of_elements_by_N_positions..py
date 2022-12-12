



n=int(input())
l=list(map(int,input().split()))
k=int(input())
u=[]
k=k%len(l)
for i in range(-k,0):
    u.append(l[i])
for i in range(n-k):
    u.append(l[i])
print(*u)