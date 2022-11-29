n=input()
s=[97,101,105,111,117]
g=[]
k=[]
for i in n:
    if ord(i) in s:
        g.append(ord(i))
for i in s:
    if i not in g:
        k.append(i)
if len(k)==0:
    print("0")
else:
    for i in k:
        print(chr(i),end=" ")
        
        
    