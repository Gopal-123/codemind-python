def f(i):
    j=1
    s=""
    for k in range(len(i)):
        s=s+i[-j]
        j+=1
    return s



n=input()
n=n.lower()
b=n.split()
c=0
for i in b:
    if i==f(i):
        c+=1
print(c)