def f(i):
    j=1
    s=""
    for k in range(len(i)):
        s=s+i[-j]
        j+=1
    return s
n=input()
n=n.lower()

a=f(n)
if a==n:
    print("True")
else :
    print("False")