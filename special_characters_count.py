n=input()
c=0
for i in n:
    if ord(i)>=33 and ord(i)<=64 or ord(i)>=91 and ord(i)<=96 or ord(i)>=123 and ord(i)<=199:
        c=c+1
print(c)        