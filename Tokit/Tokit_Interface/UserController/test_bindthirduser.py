#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 15:07
# @Author  : fengguifang
# @File    : test_bindthirduser.py
# @Software: PyCharm

import json
from base.base import MyTest

class bindthirduserTest(MyTest):
    '''根据Token绑定三方账户'''
    selfurl = '/api/user/bindThirdUser'

    @classmethod
    def setUpClass(cls):
        pass


    def test_bindthirduser_success(self):
        '''第三方登录   type   1:weibo,0:qq,2:wechat,3:xiaomiun'''
        token = 'YjVmODU1NGI1Njc4YWEwMmE2ODY0OWM3NGNlZTkyNDI='
        data = {'qq': '363632945'}
        result = self.myhttp('POST', self.selfurl, json.dumps(data), 1,token)
        print(result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])
