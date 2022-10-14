def divi(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c=c+i
    return c

n=int(input())
m=int(input())
a=divi(n)
b=divi(m)
if a==m and b==n:
    print("Amicable")
else:
    print("Not Amicable")

