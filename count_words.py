def d(a,b):
    s="a,e,i,o,u,A,E,I,O,U"
    if a in s and b not in s:
        return True
    return False



n=input()
b=n.split()
k=1
l=[]
u=0
for i in b:
    c=0
    f=0
    for j in range(len(i)):
        if d(i[j],i[-k]):
            c+=1
        else:
            f+=1
        if c==1 and f==0:
            u+=1
print(u)

    