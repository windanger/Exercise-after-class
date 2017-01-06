#計算當前目錄檔案大小

import os
all_file = os.listdir(os.curdir)
file_dict = dict()
for each_file in all_file :
    if os.path.isfile(each_file) :
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size

for each in file_dict.keys():
    print('%s是%dBytes'%(each,file_dict[each]))
