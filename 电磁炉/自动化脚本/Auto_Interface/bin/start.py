#! /usr/bin/env python
#coding=utf-8
import sys
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
# sys.path.insert(0,BASE_PATH)  # 把Auto_interface加入环境变量
from lib.common import OpCase
# from lib.common1 import OpCase
from lib.send_mail import sendmail
from conf import setting
from chardet.universaldetector import UniversalDetector
class CaseRun(object):

    def find_cases(self):
        op = OpCase()
        report_abs_path = os.path.join(setting.REPORT_PATH, 'Vplugin_report3.xls')
        # print report_abs_path

        for f in os.listdir(setting.CASE_PATH):  #每次循环的时候读一个excel
            abs_path = os.path.join(setting.CASE_PATH,f)
            print(abs_path)
            case_list = op.get_case(abs_path)
            # print('ddd:',case_list)
            res_list = []
            pass_count = 0
            fail_count = 0
            for case in case_list:  #循环每个excel里面所有用例
                host,api_url,method,is_token,is_sign,data,check=case
                res = op.my_request(host,api_url,method,is_token,is_sign,data)
                print("打印接口返回的结果：%s"%res)
                status = op.check_res(res,check)
                res_list.append([res,status])
                if status =='成功':
                    pass_count += 1
                else:
                    fail_count += 1
            file_path=op.write_excel(res_list,report_abs_path)  #写入excel
            print file_path
            msg = '''
            各位好：
                本次共运行%s条用例，通过%s条，失败%s条。
            '''%(len(res_list),pass_count,fail_count)
            print msg
            # sendmail('测试用例运行结果',content=msg,attrs=report_abs_path)




CaseRun().find_cases()