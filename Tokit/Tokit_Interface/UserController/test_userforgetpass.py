#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 9:48
# @Author  : fengguifang
# @File    : test_userforgetpass.py
# @Software: PyCharm

import json
from base.base import MyTest

class forgetpassTest(MyTest):
    '''忘记密码'''
    selfurl = '/api/user/forgetpass'

    @classmethod
    def setUpClass(cls):
        pass


    def test_forgetpass_success(self):
        '''忘记密码'''
        data = {"id": 16,
                "mobile": "18217739372",
                "password": "a18217739372",
                "smsCode": "471219"
                }
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])