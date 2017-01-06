#import random
times = 3
secret = 3
#secret = random.randint(1,10)
print('start game')

guess = 0
while guess != secret and times>0 :
    temp = input('猜一個數 : ')
    guess = int(temp)
    times -= 1
    if guess == secret :
        print( 'Bingo 答對啦~')
    else :
        if guess > secret :
            print('太大')
        else :
            print('太小')
        if times > 0:
            print('再試試')
        else :
            print('沒機會啦~!')

print('遊戲結束')
