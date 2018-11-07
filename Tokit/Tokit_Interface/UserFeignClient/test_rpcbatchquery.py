#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 16:31
# @Author  : fengguifang
# @File    : test_rpcbatchquery.py
# @Software: PyCharm

import json
from base.base import MyTest

class rpcuserqueryTest(MyTest):
    '''根据用户ID查询用户信息'''
    selfurl = '/user/rpc/batch/query'

    @classmethod
    def setUpClass(cls):
        pass


    def test_rpcuserquery_success(self):
        '''查看存在的某个用户的信息'''
        userIds=[10,11]
        result = self.myhttp('POST',self.selfurl,json.dumps(userIds),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])
