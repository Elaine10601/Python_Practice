a=1
while True:
    a=a+1
    print(a)
    if a>100:
        break


#a陣列=[0,1,2,3,4]
a=[0,1,2,3,4]
#a陣列第0個到第2個(0到1)=[3,4,5]
a[0:2]=[3,4,5]
#印出a
print(a)
##a陣列第0個到第2個(0到1)=[1,2]
a[0:2]=[1,2]
#印出a
print(a)
#a陣列第0個到第2個(0到1)=[7,4,0,6,8]
a[0:2]=[7,4,0,6,8]
#印出a
print(a)


a=[1,2,3,5]
print(4 not in a)
print(4 in a)
c=int(input('2'))
print(c in a)
