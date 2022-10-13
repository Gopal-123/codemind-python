import math
n=int(input())
for i in range(1,n+1):
    m=int(input())
    sq=int(math.sqrt(m))
    d=sq*sq
    if d==m:
        print("True")
    else:
        print("False")