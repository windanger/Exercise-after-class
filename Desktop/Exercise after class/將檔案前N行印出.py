#顯示指定文件行數

def file_view(file_name,line_num) :
    if line_num.strip() == ':':
        begin = '1'
        end = '-1'

        (begin,end) = line_num.split(':')

        if begin == '' :
            begin = '1'
        if end =='' :
            end = '-1'

        if begin == '1' and end == '-1' :
            prompt = '的全文'
        elif begin == '1' :
            prompt = '從開始到%s'%end
        elif end == '-1':
            prompt = '從%s到結束'%begin
        else :
            prompt = '從%s行到第%s行'%(begin,end)

        print('\n文件%s%s的內容如下:\n'%(file_name,prompt))

        begin = int(begin)-1
        end = int(end)
        lines = end-begin

        f = open(file_name)
        for i in range(begin):
            f.readline()
        if lines < 0 :
            print(f.readline())
        else :
            for j in range(lines) :
                print(f.readline())
        f.close()


file_name = input('filename')
line_num = input('格式')
file_view(file_name,line_num)
