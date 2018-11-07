#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 15:58
# @Author  : fengguifang
# @File    : test_getuser.py
# @Software: PyCharm

import json
from base.base import MyTest

class getuserTest(MyTest):
    '''根据Token获取用户信息'''
    selfurl = '/api/user/getUser'

    @classmethod
    def setUpClass(cls):
        pass


    def test_getuser_success(self):
        '''根据Token获取用户信息'''
        token = 'YjVmODU1NGI1Njc4YWEwMmE2ODY0OWM3NGNlZTkyNDI='
        data = {'': ''}
        result = self.myhttp('GET', self.selfurl, data, 1,token)
        print(result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])