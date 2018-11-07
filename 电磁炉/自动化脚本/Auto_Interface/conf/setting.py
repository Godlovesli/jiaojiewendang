#coding=utf-8
import os
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
print BASE_PATH

MAIL_HOST = 'smtp.qq.com'
MAIL_USER = '1107095622@qq.com'
MAIL_PASSWRD='zl19911018123456'  # 邮箱授权码
TO=[ '742720781@qq.com',
'1107095622@qq.com'
]


CASE_PATH = os.path.join(BASE_PATH,'cases') #存放用例的路径

REPORT_PATH = os.path.join(BASE_PATH,'reports') #存放报告的路径
print REPORT_PATH

