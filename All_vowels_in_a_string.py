n=input()
s=['a','e','i','o','u']
g=['A','E','I','O','U']
l=[]
m=[]
k=[]
for i in n:
    if i in s:
        l.append(i)
    elif i in g:
        m.append(i)
for i in l:
    if i not in k and i in s:
        k.append(i)
if len(k)==len(s):
    print("True")
else:
    print("False")
    
        
    
    