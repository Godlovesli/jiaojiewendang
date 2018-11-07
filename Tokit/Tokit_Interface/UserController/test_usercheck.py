#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 14:55
# @Author  : fengguifang
# @File    : test_usercheck.py
# @Software: PyCharm

import json
from base.base import MyTest

class usercheckTest(MyTest):
    '''根据手机号查询该手机号是否注册'''
    selfurl = '/api/user/check/'


    @classmethod
    def setUpClass(cls):
        pass


    def test_usercheck_success(self):
        '''已注册的手机号，返回结果为Flase'''
        mobile = '18217739372'
        selfurl = self.selfurl + mobile
        result = self.myhttp('GET', selfurl,'',1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])
        self.assertEqual(False, js['result'])

    def test_usercheck_success1(self):
        '''未注册的手机号，返回结果为True'''
        mobile = '18217739378'
        # mobile = '15666666666'
        selfurl = self.selfurl + mobile
        result = self.myhttp('GET', selfurl,'',1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])
        self.assertEqual(True, js['result'])