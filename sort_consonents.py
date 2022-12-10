def fun(i):
    h=[]
    k=[]
    g=[]
    s="aeiou"
    for j in range(len(i)):
        if i[j] in s:
            h.append(j)
        else:
            k.append(i[j])
    k.sort()
    for l in h:
        k.insert(l,i[l])
    f="".join(k)
    return f



n=input()
b=n.split()
a=[]
for i in b:
    a.append(fun(i))
print(*a)
    