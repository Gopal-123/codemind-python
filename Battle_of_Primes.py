import math
def prime(i):
    if i==1:
        return False
    sq=int(math.sqrt(i))
    for j in range(2,sq+1):
        if i%j==0:
            return False
    return True
n=int(input())
m=int(input())
c=n+m
co=0
for i in range(1,100):
    d=c+i
    co=co+1
    if prime(d):
        break
print(co)    
    
