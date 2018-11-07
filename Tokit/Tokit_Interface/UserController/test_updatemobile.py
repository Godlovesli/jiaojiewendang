#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 17:43
# @Author  : fengguifang
# @File    : test_userupdate.py
# @Software: PyCharm

import json
from base.base import MyTest

class userupdatemobileTest(MyTest):
    '''修改绑定手机'''
    selfurl = '/api/user/profile/updatemobile'

    @classmethod
    def setUpClass(cls):
        pass


    def test_userupdatemobile_success(self):
        '''修改nickname'''
        data = {"id":16, "mobile": "18621798631","newMobile":'18217739372','smsCode':'908356','newSmsCode':'633184'}
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])