n=input()
s=[97,101,105,111,117,65,69,73,79,85]
c=0
for i in n:
    if ord(i) in s:
        c=c+1
print(c)
        