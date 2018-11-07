#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 11:18
# @Author  : fengguifang
# @File    : test_userthirdlogin.py
# @Software: PyCharm

import json
from base.base import MyTest

class forgetpassTest(MyTest):
    '''第三方登录，需要加密，如果响应不包含result，则用户未注册'''
    selfurl = '/api/user/thirdlogin'

    @classmethod
    def setUpClass(cls):
        pass


    def test_thirdlogin_success(self):
        '''第三方登录   type   1:weibo,0:qq,2:wechat,3:xiaomiun'''
        data = {'':''}
        result = self.myhttp('POST', self.selfurl, json.dumps(data), 1)
        print(result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_thirdlogin_successqq(self):
        '''第三方登录   type   1:weibo,0:qq,2:wechat,3:xiaomiun'''
        data = { "type": "0", 'qq': '623447784'}
        result = self.myhttp('POST', self.selfurl, json.dumps(data), 1)
        print(result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])


    def test_thirdlogin_successxm(self):
        '''第三方登录   type   1:weibo,0:qq,2:wechat,3:xiaomiun'''
        data = { "type": "3", 'xiaomiun': '54644930'}
        result = self.myhttp('POST', self.selfurl, json.dumps(data), 1)
        print(result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_thirdlogin_successwb(self):
        '''第三方登录   type   1:weibo,0:qq,2:wechat,3:xiaomiun'''
        data = { "type": "1", 'weibo': '1234fee'}
        result = self.myhttp('POST', self.selfurl, json.dumps(data), 1)
        print(result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_thirdlogin_successwc(self):
        '''第三方登录   type   1:weibo,0:qq,2:wechat,3:xiaomiun'''
        data = { "type": "2", 'wechat': '18217739372'}
        result = self.myhttp('POST', self.selfurl, json.dumps(data), 1)
        print(result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])