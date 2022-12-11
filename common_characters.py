s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
g=[]
k=[]
for i in a:
    if i in b and i!=" ":
        g.append(i)
for i in b:
    if i in a and i!=" ":
        g.append(i)
for i in g:
    if i not in k:
        k.append(i)
k.sort()
if len(k)>0:
    f="".join(k)
    print(f)
elif len(k)==0:
    print('-1')