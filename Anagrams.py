n1=input()
n2=input()
n1=n1.lower()
n2=n2.lower()
c=0
for i in n1:
    if i in n2:
        c+=1
if c==len(n1):
    print("True")
else:
    print("False")
