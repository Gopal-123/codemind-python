n=input()
s=[]
g=[]
k=[]
m=[]
v="aeiouAEIOU"
for i in range(len(n)):
    if n[i] in v:
        s.append(i)
        k.append(i)
    else:
        g.append(n[i])
    
s.reverse()
h="".join(g)
for i in s:
    m.append(n[i])
for i in range(len(k)):
    g.insert(k[i],m[i])
f="".join(g)
print(f)
    
        