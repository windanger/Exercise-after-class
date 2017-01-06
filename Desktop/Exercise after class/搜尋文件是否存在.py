#輸入文件名及起始目錄，可以搜索該文件是否存在

import os

def search_file(start_dir,target) :
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if each_file == target :
            print(os.getcwd()+os.sep+each_file)
        if os.path.isdir(each_file):
            search_file(each_file,target)
            os.chdir(os.pardir)


start_dir = input('請輸入起始目錄 :')
target = input('請輸入搜尋文件名稱 :')
search_file(start_dir,target)