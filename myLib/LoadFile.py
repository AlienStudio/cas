# -*- coding:GBK -*-
import xlrd
import Student

# ��������
ClassNum = 13


# ����ѧ����Ϣ������stuList�б�
def LoadFile(fileName):

    data = xlrd.open_workbook(fileName)
    stuList = [Student for i in range(0, 1400)]

    for i in range(0, ClassNum):
        table = data.sheets()[i]
        for j in range(1, table.nrows):
            subject = []
            num = table.cell(j, 0)
            name = table.cell(j, 1)
            for k in range(2, 11):
                subject.append(table.cell(j, k))
            stuList[int(num % 10000)] = Student.Student(num, name, subject)

    return stuList
