s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
c=a.split()
d=b.split()
g=[]
for i in c:
    if i in d and i!=" ":
        g.append(i)
for i in d:
    if i in c and i!=" ":
        g.append(i)
f=[]
for i in g:
    if i not in f:
        f.append(i)
print(len(f))   