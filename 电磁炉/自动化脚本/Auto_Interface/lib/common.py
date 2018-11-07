#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 17:33
# @Author  : fengguifang
# @File    : common.py
# @Software: PyCharm
# import os,sys
# BASE_PATH = os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__))
# )
# sys.path.insert(0,BASE_PATH)  # 把ATP加入环境变量
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xlrd,requests
from conf.setting import CASE_PATH,REPORT_PATH
from lib.dcl_cry import generateSignature
from xlutils import copy
# from urllib import parse
import urlparse
from chardet.universaldetector import UniversalDetector


class OpCase(object):
    def get_case(self,file_path):
        self.file_path = file_path
        cases = []  # 存放测试用例
        if file_path.endswith('.xls') or  file_path.endswith('.xlsx'):
            book = xlrd.open_workbook(file_path)
            sheet = book.sheet_by_index(0)
            try:
                for i in range(1,sheet.nrows):
                    case = []  # 存放单行用例
                    row_data = sheet.row_values(i)
                    xm = row_data[0]  # 项目
                    mk = row_data[1]  # 模块
                    id = row_data[2]  # 用例ID
                    name = row_data[3]  # 用例描述
                    host = row_data[4]  # host
                    api_url = row_data[5]  # 请求url
                    method = row_data[6]  # 请求方式
                    is_token = str(row_data[7])  # 是否需要token
                    is_sign = str(row_data[8])  # 是否需要sign
                    data = eval(row_data[9])  # 请求数据
                    Expected_result = row_data[10]  # 预期结果
                    Actual_result = row_data[11]  # 返回结果
                    test_result = row_data[12]  # 测试结果
                    tester = row_data[13]  # 测试人员
                    case.append(host)
                    case.append(api_url)
                    case.append(method)
                    case.append(is_token)
                    case.append(is_sign)
                    case.append(data)
                    case.append(Expected_result)
                    cases.append(case)
                print('共读取%s条用例' % (len(cases)))
                self.file_path = file_path
            except Exception as e:
                print('【%s】用例获取失败，错误信息：%s' % (file_path, e))
        else:
            print('用例文件不合法%s' % file_path)
        print(cases)
        return cases


    def my_request(self,host,api_url,method,token=None,cry=None,data=None):
        url = urlparse.urljoin(host, api_url)  # 拼接好url
        method = method.upper()
        signature = generateSignature(method, api_url)
        if cry and token:
            headers = {"Accept": "application/json;charset=UTF-8",
                        "token": token,
                        "signature": signature}
        elif cry:
            headers = {"Accept": "application/json;charset=UTF-8",
                       "signature": signature}
        elif token:
            headers = {"Accept": "application/json;charset=UTF-8",
                       "token": token}
        else:
            headers = {"Accept": "application/json;charset=UTF-8"
                      }
        try:
            if method == 'GET':
                res = requests.get(url, params=data, headers=headers, verify=False).text

            elif method == 'POST':
                res = requests.post(url, data=data, headers=headers, verify=False).text
            else:
                res = '请求方式不暂时不支持...'
        except Exception as e:
            msg = '【%s】接口调用失败，%s' % (url, e)
            res = msg
        print type(res)

        return res


    def check_res(self, res, check):
        res = res.replace('":"', '=').replace('":', '=').replace('"'," ")
        # res = res.replace('":"', '=')
        for c in check.split('，'):
           if c not in res:
                    print u'预期结果：【%s】,实际结果【%s】' % (c, res)
                    return u'失败'
        return u'成功'

    def write_excel(self,cases_res,report_file):
        #修改excel
        book = xlrd.open_workbook(self.file_path)
        new_book = copy.copy(book)
        sheet = new_book.get_sheet(0)
        row =1
        for case_res in cases_res:
            sheet.write(row,11,case_res[0].decode('utf8'))
            sheet.write(row,12, case_res[1].decode('utf8'))
            sheet.write(row,13, u'周莉')
            row += 1
        new_book.save(report_file)
        return report_file
        # print report_file

        # 三、修改excel

        # 思路
        # 1、打开原来的excel
        # 2、拷贝一个新的excel
        # 3、获取一个sheet页
        # 4、修改excel
        # 想要修改更多数据，可以循环修改
        # 5、关闭excel
        # import xlrd
        # from xlutils import copy
        # copy.copy()#要用这个方法复制原来的文件
        #开始
        # book1 = xlrd.open_workbook(‘lyn.xls‘)  # 打开原来的excel
        # new_book = copy.copy(book1)  # 拷贝一个新的excel
        # sheet = new_book.get_sheet(0)  # 获取一个sheet页
        # # 修改excel
        # sheet.write(1, 3,‘18‘)
        # sheet.write(1, 1,‘萧何‘)
        # new_book.save(‘lyn.xls‘)  # 关闭excel

