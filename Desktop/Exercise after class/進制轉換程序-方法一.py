#將十進位轉換成二、八、十六進位

while True :
    result = input('請輸入要轉換的數(Q鍵離開) : ')
    if result != 'Q' :
        result = int(result)
        print('十進位 %d >>>二進位'%result,bin(result))
        print('十進位 %d >>>八進位 %o' %(result,result))
        print('十進位 %d >>> 十六進位 %x ' %(result,result))
    else :
        break