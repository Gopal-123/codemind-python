n=int(input())
a=0
b=1
s=0
for i in range(1,n+1):
    print(s,end=" ")
    a=b
    b=s
    s=a
    s=a+b
    