#coding=utf-8
import xlrd
class ExcelUtil():
    def __init__(self,excelPath,sheetName):
        self.data=xlrd.open_workbook(excelPath)
        self.table=self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1): #共三行
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)   #python群   	2222

                for x in range(self.colNum):  #两列 self.colNum=2
                    s[self.keys[x]] = values[x]           #[u'python\u7fa4', u'2222']
                r.append(s)
                j += 1
            return r

if __name__ =="__main__":
    filepath = "./testdata.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print data.dict_data()


        # s[self.keys[x]] = values[x]是将列名作为key，对应行的内容作为value存入字典s。
        # 通过分析返回的结果就可以看出来














