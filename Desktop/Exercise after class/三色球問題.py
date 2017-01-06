# 有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。
# 先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。

print('red','yellow','green')
for r in range(0,4) :
    for y in range(0,4):
        for g in range(2,7) :
            if r+y+g == 8 :
                print(r,'\t',y,'\t',g)