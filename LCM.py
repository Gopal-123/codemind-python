def lcm(n,m):
    for i in range(1,n*m):
        s1=n*i
        for j in range(1,n*m):
            s2=m*j
            if s1==s2:
                return s1
                break
        

n,m=map(int,input().split())
a=lcm(n,m)
print(a)
