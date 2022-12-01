n=input()
b=n.split()
s=[97,101,105,111,117,65,69,73,79,85]
g=[]
for i in b:
    d=0
    if len(b)==1:
        for j in i:
            if ord(j) in s:
                print("1")
                break
    else:
        for j in i:
            if ord(j) in s:
                d=d+1
        g.append(d)
print(g.count(max(g)))