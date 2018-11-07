#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 13:32
# @Author  : fengguifang
# @File    : test_userregister.py
# @Software: PyCharm

import json
from base.base import MyTest

class registerTest(MyTest):
    '''用户注册'''
    selfurl = '/api/user/register'

    @classmethod
    def setUpClass(cls):
        pass


    def test_register_success(self):
        '''必填参数都传，注册成功'''
        data = {"email": "", "iconUrl": "", "limit": 0, "loginType": "", "mobile": "18217739372", "nickName": "",
                "offset": 0, "password": "a18217739372", "qq": "", "roles": "", "sex": "1", "smsCode": "581876",
                "token": "", "userName": "18217739372", "wechat": "", "weibo": "", "xiaomiun": ""
                }
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_register_yzc(self):
        '''已注册的手机号再注册，注册失败'''
        data = {"email": "", "iconUrl": "", "limit": 0, "loginType": "", "mobile": "18217739372", "nickName": "",
                "offset": 0, "password": "a18217739372", "qq": "", "roles": "", "sex": "1", "smsCode": "164067",
                "token": "", "userName": "18217739372", "wechat": "", "weibo": "", "xiaomiun": ""
                }
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(10066, js['code'])
        self.assertIn('手机号已经注册过', js['message'])

    def test_register_smserror(self):
        '''验证码错误，注册失败，验证码错误'''
        data = {"email": "", "iconUrl": "", "limit": 0, "loginType": "", "mobile": "18217739373", "nickName": "",
                "offset": 0, "password": "a18217739373", "qq": "", "roles": "", "sex": "1", "smsCode": "164067",
                "token": "", "userName": "18217739373", "wechat": "", "weibo": "", "xiaomiun": ""
                }
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(10020, js['code'])
        self.assertIn('手机短信码已过期', js['message'])

