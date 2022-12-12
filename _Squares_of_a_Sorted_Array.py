n=int(input())
l=list(map(int,input().split()))
h=[]
for i in l:
    h.append(abs(i*i))
h.sort()
print(*h)