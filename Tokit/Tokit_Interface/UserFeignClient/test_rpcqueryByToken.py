#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 10:41
# @Author  : fengguifang
# @File    : test_rpcqueryByToken.py
# @Software: PyCharm

import json
from base.base import MyTest

class rpcqueryByTokenTest(MyTest):
    '''根据用户token查询用户信息'''
    selfurl = '/user/rpc/queryByToken'

    @classmethod
    def setUpClass(cls):
        pass


    def test_rpcquerytoken_success(self):
        '''查看某个用户的信息'''
        data = {'token': 'ZDNjYjYxZWM4NTk4YjgxNmViZDE1NzFmZTVkNGRjNWU='}
        token='ZDNjYjYxZWM4NTk4YjgxNmViZDE1NzFmZTVkNGRjNWU='
        result = self.myhttp('POST',self.selfurl,data,1,token)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])