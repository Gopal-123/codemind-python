def fun(i):
    k=[]
    g=[]
    f=[]
    for j in range(len(i)):
        if ord(i[j])>=33 and ord(i[j])<=47 or ord(i[j])>=58 and ord(i[j])<=64:
            f.append(j)
        else:
            k.append(i[j])
    k.sort()
    for l in f:
        k.insert(l,i[l])
    f="".join(k)
    return f
n=input()
b=n.split()
a=[]
for i in b:
    a.append(fun(i))
print(*a)