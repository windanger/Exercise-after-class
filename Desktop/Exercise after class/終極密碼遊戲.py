# 從0~100猜一數字，猜中者輸掉比賽，數字範圍會因為回合數愈多而愈小
import random
number = random.randint(1,50)
guess = int(input('請猜數字 :'))
if guess == number :
    print('恭喜啦,答案是:',guess)
else :
    while True:
        if guess > number :
            print(guess,'再小一點')
        elif guess < number :
            print(guess,'再大一點')
        else :
            print('恭喜啦,答案是:',guess)
            break
        guess = int(input('再猜猜 :'))