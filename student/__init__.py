class Student:
    num = 0             # 学号
    name = ''           # 姓名
    subject=[]          # 选科

    def __init__(self, num, name, subject):
        self.num = num
        self.name = name
        self.subject = subject