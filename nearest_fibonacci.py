n=int(input())
a=0
b=1
s=0
c=0
for i in range(1,n+1):
    a=b 
    b=s
    s=a
    s=a+b
    if s<n:
        g=s
    elif(s>n):
        y=s
        break
z=n-g
k=y-n
if z<k:
    print(g)
elif z>k:
    print(y)
else:
    print(g,y)
