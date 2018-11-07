#coding=utf-8
import xlrd
#打开excel表格
data = xlrd.open_workbook('testdata.xlsx')
table=data.sheet_by_index(0)
print table.nrows  #获取总行数
print table.ncols  #获取总列数
print table.row_values(1)   #获取第er行值
print table.col_values(0)   #获取第一列值
print table.col_values(1)   #如果excel数据中有纯数字的一定要右键》设置单元格格式》文本格式，要不然读取的数据是浮点数
for i in range(table.nrows - 1):  # 共三行
    print  table.row_values(i)