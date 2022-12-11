s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
c=a.split()
d=b.split()
for i in d:
    if i in c:
        print(i,end=" ")