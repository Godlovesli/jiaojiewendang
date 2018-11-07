#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 15:19
# @Author  : fengguifang
# @File    : test_fileupload.py
# @Software: PyCharm
#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
requests.packages.urllib3.disable_warnings()
class articletopadv1Test(MyTest):
    '''获取头部Banner'''
    url_path = '/file/upload'

    @classmethod
    def setUpClass(cls):
        pass

    def test_fileupload(self):
        '''所有参数都传'''
        url = self.base_url + self.url_path
        print url
        # file = {'filename':open(r'C:\Users\lzhou\Desktop\test.jpg', 'rb')}
        file = {'filename': open(r'D:\test.jpg', 'rb')}
        r = requests.post(url, files=file)  # 文件附件用files提交
        result = r.content
        print result
        js = json.loads(result)
        self.assertEqual(js['code'], 1)
