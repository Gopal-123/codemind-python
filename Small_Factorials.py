def fact(a):
    if a==0:
        return 1
    return a*fact(a-1)



n=int(input())
for i in range(0,n):
    a=int(input())
    print(fact(a))
