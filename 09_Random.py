import random


print(int(random.random()*50+1))
print(random.randint(1,50))
print(random.randrange(1,51,1))
#產生1-50的變數
print(random.sample(range(1,51),6))


a=[]
e=1
while e<=6:
    c=random.randint(1,6)
    if c not in a:
        a=a+[c]
        e=e+1
print(a)


import random
a=[random.randint(1,6)]
e=1
while e<6:
    c=random.randint(1,6)
    if c not in a:
        a=a+[c]
        e=e+1
print(a)


a=[0,0,0,0,0,0]
e=0
while e!=6:
    b=0
    c=random.randint(1,50)
    print(c)
    while True:
        if c!=a[b]:
            b=b+1
            if b==5:
                a[e]=c
                e=e+1
                break
        else:
            break
print(a)


#random.seed()
