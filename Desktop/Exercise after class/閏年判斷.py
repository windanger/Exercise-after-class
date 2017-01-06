#判斷是否是閏年

year = input('請輸入要判斷年份 :')
y = int(year)
def leapyear(y) :
    if y % 400 == 0 :
        return True
    elif y % 4==0 and y % 100 != 0 :
        return True
    else :
        return False
if leapyear(y) == True :
    print(y,'is leapyear')
else :
    print(y,'isn\'t leapyear')
