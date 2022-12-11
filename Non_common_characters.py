s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
c=""
d=""
for i in a:
    if i not in b and i!=" ":
        c=c+i
for i in b:
    if i not in a and i!=" ":
        c+=i
for i in c:
    if i not in d:
        d+=i
print(len(d))