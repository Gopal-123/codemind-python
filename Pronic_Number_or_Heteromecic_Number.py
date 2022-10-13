def pro(n):
    for i in range(1,n+1):
        a=1+i
        if a*i==n:
            return True
        
           
        
    


n=int(input())
if pro(n):
    print("YES")
else:
    print("NO")