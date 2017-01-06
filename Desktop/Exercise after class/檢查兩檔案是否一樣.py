def compare(f1,f2) :
    f1 = open(f1)
    f2 = open(f2)
    line = 0
    differ = []

    for line1 in f1 :
        line2 = f2.readline()
        line +=1
        if line1 != line2 :
            differ.append(line)

    f1.close()
    f2.close()
    return differ

f1 = input('請輸入檔名1 :')
f2 = input('請輸入檔名2 :')
differ = compare(f1,f2)

if len(differ) == 0 :
    print('兩文件完全一樣')
else :
    print('兩文件共{}處不同'.format(len(differ)))
    for each in differ :
        print('第{}行不同'.format(each))
