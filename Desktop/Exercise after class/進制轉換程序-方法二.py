#將十進位轉換成二、八、十六進位

while True :
    result = input('請輸入要轉換的數(Q鍵離開) : ')
    if result != 'Q' :
        result = int(result)
        print('十進位 {} >>> \n二進位 : {:#b}\n1八進位 : {:#o}\n十六進位 : {:x}'.format(result,result,result,result))
    else :
        break