while True:
    d=int(input('如需繼續，請輸入end'))
    if d=='end':
        a=int(input('請輸入數字a='))
        b=int(input('請輸入數字b='))
        c=input('請輸入運算子')
        if c=='+':
            print('a+b=',a+b)
        elif c=='-':
            print('a-b=',a-b)
        elif c=='*':
            print('a*b=',a*b)
        elif c=='/':
            print('a/b=',a/b)
    else:
        break
