def vow(a,b):
    s=['a','e','i','o','u','A','E','I','O','U']
    if a in s and b not in s or b in s and a not in s:
        if a==' ' or b==' ':
            return False
        return True

n=input()
b=n.split()
l=[]
m=0
j=1
for i in range(len(n)//2):
    if vow(n[i],n[-j]):
        m+=1
    j+=1
if m>0:
    print(m)
else:
    print(m)

            