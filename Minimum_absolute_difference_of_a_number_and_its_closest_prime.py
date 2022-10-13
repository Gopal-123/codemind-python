import math
def prime(n):
    if n==1:
        return False
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True    

n=int(input())
for i in range(n+1,n*n,+1):
    if prime(i):
        break
for j in range(n,0,-1):
    if prime(j):
        break
c=n-j
d=i-n
if c<d:
    print(c)
else:
    print(d)
    
