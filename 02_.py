#陣列a
a=[]
#r等於輸入數量
r=0
#在陣列中加入數字
a=a+[int(input('請輸入數字'))]
#輸入數量加一
r=r+1
#u等於總和
u=a[-1]
#v等於最大值
v=a[-1]
#p等於最小值
p=a[-1]
#印出陣列
print(a)
#當正確時迴圈
while True:
    #如果判斷值等於0
    if input('結束請按0')=='0':
        #跳出迴圈
        break
    #在陣列中加入數字
    a=a+[int(input('請輸入數字'))]
    #輸入數量加一
    r=r+1
    #總和加上輸入值
    u=u+a[-1]
    #如果輸入值大於最大值
    if a[-1]>v:
        #最大值等於輸入值
        v=a[-1]
    #如果輸入值小於最小值
    elif a[-1]<p:
        #最小值等於輸入值
        p=a[-1]
    #印出陣列
    print(a)
#印出'最大值'
print('max',v)
#印出'最小值'
print('min',p)
#印出'輸入數量'
print('len',r)
#印出'總和'
print('sum',u)
#印出'平均值'
print('average',u/r)
