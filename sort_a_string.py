n=input()
f=[]
g=[]
for i in range(len(n)):
    if ord(n[i])>=32 and ord(n[i])<=47 or ord(n[i])>=58 and ord(n[i])<=64:
        f.append(i)
    else:
        g.append(n[i])
j="".join(sorted(g))
k=list(j)
for i in f:
    k.insert(i,n[i])
    l="".join(k)
print(l)
    
