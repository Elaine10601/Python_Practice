a=[5,4,3,2,1,0]
for j in range(1,len(a)):
    for i in range(0,len(a)-j):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
            #a[i],a[i+1]=a[i+1],a[i]
print(a)


#a.sort()
