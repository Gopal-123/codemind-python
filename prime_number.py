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
if prime(n):
    print("prime")
else:
    print("not a prime")