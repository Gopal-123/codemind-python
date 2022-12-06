def c(n):
    c=0
    while(n):
        d=n%10
        n=n//10
        c+=1
    return c
n=int(input())
p={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
Q={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
R={1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
f=c(n)
if f==1:
    if n in p.keys():
        print(p[n])
elif f==2:
    if n in Q.keys():
        print(Q[n])
    else:
        d=n%10
        n=n//10
        if d==0:
            if n in R.keys():
                print(R[n])
        else:
            if n in R.keys():
                print(R[n])
            if d in p.keys():
                print(p[d])
elif f==3:
    d=n%100
    n=n//100
    if d==00:
        if n in p.keys():
            print(p[n],'hundred')
    else:
        k=d%10
        g=d//10
        if n in p.keys():
            print(p[n],'hundred',end=' ')
        if d in Q.keys():
            print(Q[d])
        else:
            
            if k==0:
                if g in R.keys():
                    print(R[g])
            else:
                if g in R.keys():
                    print(R[g],end=' ')
                if k in p.keys():
                    print(p[k])
elif f==4:
    d=n%1000
    n=n//1000
    if d==000:
        if n in p.keys():
            print(p[n],end='thousand')
    else:
        k=d%100
        g=d//100
        m=k%10
        b=k//10
        if n in p.keys():
            print(p[n],'thousand',end=' ')
        if k==00:
            if g in p.keys():
                print(p[g],'hundred')
        else:
            if g in p.keys():
                print(p[g],'hundred',end=' ')
            if k in Q.keys():
                print(Q[k])
            else:
                if m==0:
                    if b in R.keys():
                        print(R[b],end=' ')
                else:
                    if b in R.keys():
                        print(R[b],end=' ')
                    if m in p.keys():
                        print(p[m])