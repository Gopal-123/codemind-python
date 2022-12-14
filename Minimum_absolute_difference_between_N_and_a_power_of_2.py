n=int(input())
l=[]
for i in range(n):
    if pow(2,i)<=n:
        k=(pow(2,i))
for i in range(n):
    if pow(2,i)>n:
        g=pow(2,i)
        break
c=n-k
d=g-n
if c<d:
    print(abs(c))
else:
    print(abs(d))