# coding=utf-8
import xlrd
import time
import os
from xlutils.copy import copy

dir_path = os.path.dirname(os.getcwd())


# excel 文件操作工具类
# xlrd 只能操作 .xls
# 若要操作.xlsx 需要openpyxl
#
class ExcelUtil:

    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            self.excel_path = os.path.abspath(dir_path + '/config/casedata.xls')
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]
        # [[],[]]

    # 获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        # 行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格的数据
    def get_col_value(self, row, col):
        # print
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)#复制一份修改后,再存储
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)
        time.sleep(1)


if __name__ == '__main__':
    path = os.path.abspath(dir_path + '/config/keyword.xls')
    ex = ExcelUtil(path)
    print(ex.get_col_value(10, 8))
