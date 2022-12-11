a=input()
a=a.lower()
b=a.split()
d=b[0]
s=[]
for i in d:
    c=0
    for j in range(1,len(b)):
        if i in b[j]:
           c=c+1
    if c==len(b)-1:
        s.append(i)
if len(s)==0:
    print("-1")
else:
   t="".join(s)
   print(t)
