# 筆記本資料寫入
ff=open('data.txt',mode='a',encoding='utf-8')
#a:add附加
# ff=open('data.txt','w',encoding='utf-8')
# ff=物件名稱->'data.txt'，執行後產生一個檔 
# w:寫入(覆蓋原先檔案) en..正在編碼 utf-8:編碼器名稱
ff.write('5\n25\n')
ff.write('abc\n')
ff.write('第一行\n')
# 中文字需使用編碼器
# \n換行
ff.close()


#with指定一個物件名稱(ff)在後面 自動關閉檔案
with open('d525.txt',mode='a',encoding='utf-8') as ff:
    ff.write('5,25\n')

    
with open('dd.txt',mode='a',encoding='utf-8') as ff:
    while True:
        s=input('請輸入資料')
        if s=='':
            ff.write('\n')
        elif s=='-1':
            break
        else:
            ff.write(s)
    # ff.write('5,25\n')
    #s=input('請輸入資料:)
    #ifs='' 換行  ='-1' 結束 其他寫入


with open('a.txt','a',encoding='utf=8') as f:
    while True:
        b=input('請輸入數字')
        if b=='':
            f.write('\n')
        elif b=='-1':
            break
        else:
            f.write(b)
            f.write(',')


with open('a.txt','r',encoding='utf=8') as f:
    b=f.read()
    c=b.split(',')
d=[]
for i in range(0,len(c)-1):
    d=d+[int(c[i])]
print('總和',sum(d))
print('長度',len(d))
print('平均',sum(d)/len(d))


with open('d525.txt',mode='r',encoding='utf=8') as ff:
    a=ff.read()
    b=a.split(',')
c=[]
for i in range(0,len(b)-1):
    c=c+[int(b[i])]
print(a)
print(b)
print(c)
print(sum(c))
print(len(c))
print(sum(c)/len(c))
