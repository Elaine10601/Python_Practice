while True:
    a=int(input('輸入十進位整數'))
    b=int(input('輸入十進位小數'))
    n=int(input('要轉換的進制(2~9)'))
    c=0.1**len(str(b))
    d=0.1
    f=0
    while a!=0:
        j=a%n
        d=d*10
        f=f+(j*d)
        a=a//n
    e=1
    g=0
    i=b*c
    h=0
    while i!=0:
        i=i*n
        e=e/10
        if i<0:
            k=0
        else:
            k=i//1
        g=g+k*e
        i=i-k
        h=h+1
        if h==10:
            break
    print(n,'進制:',f+g)
    if input('輸入end,結束')=='end':
        break

#just to binary      
while True:
    a=int(input('輸入十進位整數'))
    p=int(input('輸入十進位小數'))
    k=0.1**len(str(p))
    c=0.1
    d=0
    v=a//1
    while v!=0:
        b=v%2
        v=v//2
        c=c*10
        d=d+(b*c)
    g=1
    f=0
    e=p*k
    while e!=0:
        e=e*2
        g=g/10
        if e>=1:
            i=1
        else:
            i=0
        f=f+i*g
        if e>=1:
            e=e-1
    print('二進制',d+f)
    if input('輸入end,結束')=='end':
        break

        
a=int(input('輸入十進制'))
b=''
n=0
while a>2**n:
    n=n+1
n=n-1
while n>=0:
    if a>=2**n:
        a=a-2**n
        b=b+'1'
    else:
        b=b+'0'
    n-=1
print(b+'B')


a=int(input('輸入十進位'))
c=0
d=0
e=0
while a!=0:
    b=a%2
    d=d+1
    c=b*10**d
    e=e+c
    a=a//2
print('二進制',e)


a=int(input('輸入十進位'))
c=''
while a!=0:
    b=str(a%2)
    c=b+c
    a=a//2
print('二進制',c)
