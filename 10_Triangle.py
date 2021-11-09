x=int(input('輸入數字'))
b=1
for i in range(x,0,-1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,b*2):
        print('*',end='')
    print("")
    b=b+1
    
    
x=int(input('輸入數字'))
for i in range(x,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print("")
x=int(input('輸入數字'))
for i in range(1,x+1):
    for j in range(1,x+1-i+1):
        print("*",end="")
    print("")
    
    
x=int(input('輸入數字'))
for i in range(x,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print("")
