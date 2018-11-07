#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 17:43
# @Author  : fengguifang
# @File    : test_userupdate.py
# @Software: PyCharm

import json
from base.base import MyTest

class userupdateTest(MyTest):
    '''修改个人信息（含个人图像、性别、昵称、密码），需要加密，密码需要MD5后再传输'''
    selfurl = '/api/user/profile/update'

    @classmethod
    def setUpClass(cls):
        pass


    def test_userupdate_success(self):
        '''修改nickname'''
        data = {"id":16, "nickName": "nn18217739372"}
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_userupdate_successx(self):
        '''修改sex'''
        data = {"id":16,"sex": "0"}
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_userupdate_successicon(self):
        '''修改iconUrl'''
        data = {"id":16,"iconUrl": "https://img.joyami.com/img/20180522/b08c25f6fe714810b934372d5bfef3ea.jpg"}
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_userupdate_successpw(self):
        '''修改密码'''
        data = { "id":16,"mobile": "18217739372", "password": "d18217739372", "smsCode": "471219"}
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])