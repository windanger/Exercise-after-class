import time as t

class timer:
    def __init__(self):
        self.units =['年','月','日','時','分','秒']
        self.begin = 0
        self.ending = 0
        self.lasted = []
        self.prompt = '未開始計時'
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    def __add__(self, other):
    # 計算計時器的時間和
        result =[]
        plus = '加總共運行了'
        for index in range(0,6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index] :
                plus += str(result[index])+str(self.units[index])
        return plus
    def start(self):
    #開始
        self.begin = t.localtime()
        self.prompt = '請先stop停止計時'
        print('計時開始')
    def stop(self):
    #結束
        if not self.begin :
            print('請先start開始計時')
        else :
            self.ending = t.localtime()
            self.__cul()
            print('計時結束')
    def __cul(self):
        self.prompt = '總共運行了'
        self.lasted = []
        for index in range(0,6):
            self.lasted.append(self.ending[index]-self.begin[index])
            if self.lasted[index] :
                self.prompt += str(self.lasted[index])+str(self.units[index])
        # 為下一輪初始化變量
        self.begin = 0
        self.ending = 0
