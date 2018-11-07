#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 16:53
# @Author  : fengguifang
# @File    : test_smssend.py
# @Software: PyCharm

import json
from base.base import MyTest


class smssendTest(MyTest):
    '''发送短信'''
    selfurl = '/api/sms/send/'
    mobile = '18217739372'

    @classmethod
    def setUpClass(cls):
        pass

    def test_smssend_success(self):
        '''必填参数都传，发送成功'''
        selfurl=self.selfurl+self.mobile
        print (selfurl)
        result = self.myhttp('GET', selfurl,'',0)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])