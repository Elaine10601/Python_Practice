with open('a.txt','w',encoding='utf=8') as f:
    import random
    z=['0']
    x=[0]
    w=[0]
    n=[0]
    y=0
    v=[0]
    t={'a':'矩形','b':'菱形','c':'三角形'}
    tt={'1':'a','2':'b','3':'c'}
    ttt={'1':'正立','2':'倒立'}
    xw=['0','1','2','3','4','5','6','7','8','9',' ']
    while True:
        y=y+1
        print('第',y,'層')
        print('a.矩形','b.菱形','c.三角形')
        z=z+[str(input('請輸入你要的圖形'))]
        if z[y]!='a' and z[y]!='b' and z[y]!='c':
            z[y]=tt[str(random.randint(1,3))]
        print('已選擇',t[z[y]])
        if z[y]=='c':
            n=n+[str(input('1.正立　2.倒立'))]
            if n[y]!='1' and n[y]!='2':
                n[y]=random.randint(1,2)
            n[y]=int(n[y])
            print('已選擇',ttt[str(n[y])])
        elif z[y]!='c':
            n=n+[0]
        x=x+[str(input('請輸入邊長'))]
        if x[y]=='':
            x[y]=str(random.randint(1,50))
        xx=set(x[y])
        if len(xx.difference(xw))>0:
            x[y]=str(random.randint(1,50))
        x[y]=int(x[y])
        print('邊長',x[y])
        w=w+[str(input('請輸入數量'))]
        if w[y]=='':
            w[y]=str(random.randint(1,1024//(2*(x[y])-1)))
        ww=set(w[y])
        if len(ww.difference(xw))>0:
            w[y]=str(random.randint(1,1024//(2*(x[y])-1)))
        w[y]=int(w[y])
        print('數量',w[y])
        if input('要再一層嗎? y/n')=='n':
            break
    for q in range(1,y+1):
        if z[q]=='a':
            v=v+[(x[q])*(w[q])]
        else:
            v=v+[(2*(x[q])-1)*(w[q])]
    u=max(v)
    for i in range(1,y+1):
        m=(u-v[i])//2
        if z[i]=='a':
            for b in range(1,x[i]+1):
                for o in range(1,m+1):
                    print('　',end='')
                    f.write('　')
                for j in range(1,w[i]+1):
                    for c in range(1,x[i]+1):
                        print('＊',end='')
                        f.write('＊')
                print('')
                f.write('\n')
        elif z[i]=='b':
            for b in range(1,2*x[i]):
                for o in range(1,m+1):
                    print('　',end='')
                    f.write('　')
                if b<=x[i]:
                    for j in range(1,w[i]+1):
                        for d in range(x[i]-b,0,-1):
                            print('　',end='')
                            f.write('　')
                        for c in range(1,2*b):
                            print('＊',end='')
                            f.write('＊')
                        for d in range(x[i]-b,0,-1):
                            print('　',end='')
                            f.write('　')
                elif b>x[i]:
                    for j in range(1,w[i]+1):
                        for g in range(1,b-x[i]+1):
                            print('　',end='')
                            f.write('　')
                        for e in range(2*x[i]-2*g-1,0,-1):
                            print('＊',end='')
                            f.write('＊')
                        for g in range(1,b-x[i]+1):
                            print('　',end='')
                            f.write('　')
                print('')
                f.write('\n')
        elif z[i]=='c':
            for b in range(1,x[i]+1):
                for o in range(1,m+1):
                    print('　',end='')
                    f.write('　')
                if n[i]==1:
                    for j in range(1,w[i]+1):
                        for d in range(x[i]-b,0,-1):
                            print('　',end='')
                            f.write('　')
                        for c in range(1,2*b):
                            print('＊',end='')
                            f.write('＊')
                        for d in range(x[i]-b,0,-1):
                            print('　',end='')
                            f.write('　')
                elif n[i]==2:
                    for j in range(1,w[i]+1):
                        for g in range(1,b):
                            print('　',end='')
                            f.write('　')
                        for e in range(1,2*(x[i]-b+1)):
                            print('＊',end='')
                            f.write('＊')
                        for g in range(1,b):
                            print('　',end='')
                            f.write('　')
                print('')
                f.write('\n')
