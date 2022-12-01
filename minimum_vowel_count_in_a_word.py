n=input()
b=n.split()
s=[97,101,105,111,117,65,79,73,79,85]
g=[]
for i in b:
    d=0
    for j in i:
        if ord(j) in s:
            d=d+1
    g.append(d)
print(min(g))    
    
