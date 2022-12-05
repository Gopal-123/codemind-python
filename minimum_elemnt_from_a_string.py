n=input()
b=n.split()
for i in b:
    d=i
f=min(d)

if chr(ord(f)+32) in d:
    print(chr(ord(f)+32))
else:
    print(min(d))

    