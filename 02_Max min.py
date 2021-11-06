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
