#陣列a
a=[]
#當正確時迴圈
while True:
    #在陣列中加入數字
    a.append(int(input('請輸入數字')))
    #印出陣列
    print(a)
    #如果判斷值等於0
    if input('結束請按0')=='0':
        #跳出迴圈
        break
#印出'最大值'
print('max',max(a))
#印出'最小值'
print('min',min(a))
#印出'輸入數量'
print('len',len(a))
#印出'總和'
print('sum',sum(a))
#印出'平均值'
print('平均',sum(a)/len(a))
