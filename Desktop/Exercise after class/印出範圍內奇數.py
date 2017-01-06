#列出給定範圍內之所有奇數

start = int(input('請輸入起始所需數字'))
end = int(input('請樹入結束所需數字'))
list = range(start,end+1)
for number in list :
    if number % 2 != 0 :
        print(number)
