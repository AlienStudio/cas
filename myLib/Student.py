# -*- coding:GBK -*-


# ���ڴ洢ѧ����Ϣ����
class Student:
    num = 0             # ѧ��
    name = ''           # ����
    subject=[]          # ѡ��

    def __init__(self, num, name, subject):
        self.num = num
        self.name = name
        self.subject = subject
