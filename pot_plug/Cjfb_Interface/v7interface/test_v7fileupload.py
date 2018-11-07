#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 13:32
# @Author  : fengguifang
# @File    : test_v7fileupload.py
# @Software: PyCharm
import unittest
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class uploadTest(unittest.TestCase):
    '''上传文件'''


    def setUp(self):

        self.base_url = 'http://pre-plugapi.joyami.com'
        self.url_path = '/v7/file/upload'



    def test_upload_success(self):
        '''上传文件成功'''
        url = self.base_url + self.url_path
        file = {'filename': open(r'D:\test.jpg', 'rb')}
        r=requests.post(url,files=file) #文件附件用files提交
        result=r.content
        print result
        js = json.loads(result)
        self.assertEqual(js['state'], 1)