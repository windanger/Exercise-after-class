#寫一个密码安全性检查的脚本代码
#低级密码要求：
#1. 密码由单纯的数字或字母组成
#2. 密码长度小于等于8位

#中级密码要求：
#1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#2. 密码长度不能低于8位

#高级密码要求：
#1.密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#2.密码只能由字母开头
#3.密码长度不能低于16位

symbols = '~!@#$%^&*()_=-/,.?<>;:[]{}\|'
number = '123456789'
character = 'abcdefghijklmnopqrstuvwxyz'
password = input('請輸要入要設置的密碼 : ')
def check_len(passwoard) :
    if 0<len(password) <= 8 :
        return 0
    elif 8<len(password)<=16 :
        return 1
    else :
        return 2

def char(password) :
    result = 0
    for each in password :
        if each in character :
            result =1
    return result

def num(password) :
    result  = 0
    for each in number :
        if each in number :
            result =1
    return result

def sym(password) :
    result  = 0
    for each in password :
        if each in symbols :
            result =1
    return result
def letter(password) :
    if password[0] in character :
        return True
    else :
        return False

if check_len(password) == 0 and char(password)+num(password) >1 and sym(password) == 0 :
    print('Low')
elif check_len(password) == 1 and char(password)+num(password)+sym(password) >= 2 :
    print('MID')
elif check_len(password) == 2 and char(password)+num(password)+sym(password) ==3 and letter(password) == True :
    print('HIGH')
else :
    print('輸入錯誤請重新輸入')
