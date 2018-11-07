#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 16:12
# @Author  : fengguifang
# @File    : test_rpcuserinfo.py
# @Software: PyCharm

import json
from base.base import MyTest

class rpcuserinfoTest(MyTest):
    '''获取用户信息'''
    selfurl = '/user/rpc/16/info'

    @classmethod
    def setUpClass(cls):
        pass


    def test_rpcuserinfo_success(self):
        '''查看存在的某个用户的信息'''
        result = self.myhttp('GET', self.selfurl,'',1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])


    def test_rpcuserinfo_success1(self):
        '''查看不存在的某个用户的信息'''
        selfurl = '/user/rpc/111/info'
        result = self.myhttp('GET', selfurl, '', 1)
        print(result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])