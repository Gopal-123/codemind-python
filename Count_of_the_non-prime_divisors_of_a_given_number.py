import math
def np(i):
    sq=int(math.sqrt(i)) 
    for j in range(2,sq+1):
        if i%j==0:
            return True
    return False   
n=int(input())  
c=1
for i in range(2,n+1):
    if n%i==0:
        if np(i):
             c=c+1
print(c)    