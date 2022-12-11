n=input()
c=0
for i in n:
    if ord(i)>=97 and ord(i)<=122:
        if n.count(i)==1:
            c+=1
    elif ord(i)>=65 and ord(i)<=90:
        c+=1
if c==len(n):
    print("True")
else:
    print("False")
            