#寫一個能統計當前目錄下不同文件類型及其數量的程式

import os

all_files = os.listdir(os.curdir)
type_dict = dict()
for each_file in all_files :
    if os.path.isdir(each_file) :
        type_dict.setdefault('資料夾',0)
        type_dict['資料夾'] += 1
    else :
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext,0)
        type_dict[ext] +=1

for each_type in type_dict.keys():
    print('類型有%s共%s個'%(each_type,type_dict[each_type]))
