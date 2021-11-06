a=[]
r=0
a=a+[int(input('請輸入數字'))]
r=r+1
u=a[-1]
v=a[-1]
p=a[-1]
while True:
    print(a)
    if a[-1]>v:
        v=a[-1]
    elif a[-1]<p:
        p=a[-1]
    if input('結束請按0')=='0':
        break
    a=a+[int(input('請輸入數字'))]
    r=r+1
    u=u+a[-1]
print('max',v)
print('min',p)
print('len',r)
print('sum',u)
print('average',u/r)


#a:輸入數字的數量
a=0
#b:所有輸入的總和
b=0
#d:判斷是否結束
d=1
#當d不等於'0'時，重複執行
while d!='0':
    #c=輸入數字後轉為數字
    c=int(input('請輸入數字'))
    #之前輸入數字的數量+1
    a=a+1
    #之前的總和加上輸入
    b=b+c
    #輸入'0'，結束迴圈
    d=input('如需結束，請輸入0')
#印出輸入之平均
print('平均值:',b/a)


#將數字轉為數字
a=int(input('輸入數字'))
#最大值即輸入值
max=a
#最小值即輸入值
min=a
#當正確時迴圈
while True:
    #判斷結束值
    c=input('如需結束請輸入0')
    #如果判斷值等於0
    if c=='0':
        #跳出迴圈
        break
    #將數字轉為數字
    a=int(input('輸入數字'))
    #如果數字大於最大值
    if a>max:
        #最大值等於數字
        max=a
    #如果數字小於最小值
    elif a<min:
        #最小值等於數字
        min=a
#印出'最大值'
print('max:',max)
#印出'最小值'
print('min:',min)


a=[]
while True:
    a.append(int(input('請輸入數字')))
    print(a)
    if input('結束請按0')=='0':
        break
print('max',max(a))
print('min',min(a))
print('len',len(a))
print('sum',sum(a))
print('average',sum(a)/len(a))
