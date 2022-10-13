def selfdividing(i):
    tem=i
    while tem:
        d=tem%10
        tem=tem//10
        if d==0:
            return False
        if i%d==0:
            continue
        return False  
    return True    



n=int(input())
m=int(input())
for i in range(n,m+1):
    if selfdividing(i):
        print(i,end=" ")