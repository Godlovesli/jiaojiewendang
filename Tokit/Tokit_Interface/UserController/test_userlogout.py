#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 15:12
# @Author  : fengguifang
# @File    : test_userlogout.py
# @Software: PyCharm

import json
from base.base import MyTest

class loginoutTest(MyTest):
    '''用户退出，需要加密'''
    selfurl = '/api/user/logout'

    @classmethod
    def setUpClass(cls):
        pass


    def test_loginout_success(self):
        '''密码登录的token，退出成功'''
        data={'':''}
        token= "YjVmODU1NGI1Njc4YWEwMmE2ODY0OWM3NGNlZTkyNDI="
        result = self.myhttp('POST', self.selfurl,data,1,token)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_loginout_yzmsuccess(self):
        '''验证码登录的token，退出成功'''
        data={'':''}
        token= "ZTVkMTUxMGMxYmU0MGFjMzQwMzM3OGQyM2VkZTkyZDY="
        result = self.myhttp('POST', self.selfurl,data,1,token)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])