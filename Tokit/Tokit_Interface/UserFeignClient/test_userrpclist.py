#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 16:41
# @Author  : fengguifang
# @File    : test_userrpclist.py
# @Software: PyCharm

import json
from base.base import MyTest

class rpclistTest(MyTest):
    '''分页获取用户列表'''
    selfurl = '/user/rpc/list'

    @classmethod
    def setUpClass(cls):
        pass


    def test_rpclist_success(self):
        '''查看存在的某个用户的信息'''
        data={'limit':'1','offset':'10'}
        result = self.myhttp('GET',self.selfurl,data,1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])