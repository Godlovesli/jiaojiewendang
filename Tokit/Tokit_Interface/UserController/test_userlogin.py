#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:17
# @Author  : fengguifang
# @File    : test_userlogin.py
# @Software: PyCharm

import json
from base.base import MyTest

class loginTest(MyTest):
    '''用户登入，密码登录loginType为空,1为验证码登录'''
    selfurl = '/api/user/login'

    @classmethod
    def setUpClass(cls):
        pass


    def test_login_success(self):
        '''密码登录loginType为空，登录成功'''

        data = { "loginType": "","mobile": "18217739372", "password": "a18217739372"}
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])
        #{"code":200,"message":"操作成功","result":{"id":11,"userName":"tokit_11","nickName":"tokit_11","mobile":"18217739372","email":"","sex":"1","iconUrl":"","xiaomiun":"","token":"ODkxMDEyNmNhZjdmMTYyMDIyOTcwOTg0ZTk2MmJjZmM="}}


    def test_login_yzmdr(self):
        '''验证码登录，loginType为1，登录成功'''
        data = {"email": "", "iconUrl": "", "limit": 0, "loginType": "1", "mobile": "18217739372", "nickName": "",
                "offset": 0, "password": "", "qq": "", "roles": "", "sex": "", "smsCode": "755442",
                "token": "", "userName": "", "wechat": "", "weibo": "", "xiaomiun": ""
                }
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])

    def test_login_pswderror(self):
        '''密码登录loginType为空，密码错误，登录失败'''
        data = {"email": "", "iconUrl": "", "limit": 0, "loginType": "", "mobile": "18217739372", "nickName": "",
                "offset": 0, "password": "18217739372", "qq": "", "roles": "", "sex": "", "smsCode": "878291",
                "token": "", "userName": "", "wechat": "", "weibo": "", "xiaomiun": ""
                }
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        # self.assertEqual(10020, js['code'])
        self.assertIn('用户名或密码错误', js['message'])

    def test_login_mblerror(self):
        '''密码登录loginType为空，手机号错误，登录失败'''
        data = {"email": "", "iconUrl": "", "limit": 0, "loginType": "", "mobile": "a18217739372", "nickName": "",
                "offset": 0, "password": "a18217739372", "qq": "", "roles": "", "sex": "", "smsCode": "",
                "token": "", "userName": "", "wechat": "", "weibo": "", "xiaomiun": ""
                }
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        # self.assertEqual(10020, js['code'])
        self.assertIn('用户名或密码错误', js['message'])

    def test_login_mberror(self):
        '''用未注册的手机号登录，登录失败'''
        data = {"email": "", "iconUrl": "", "limit": 0, "loginType": "1", "mobile": "18217739373", "nickName": "",
                "offset": 0, "password": "", "qq": "", "roles": "", "sex": "", "smsCode": "242395",
                "token": "", "userName": "", "wechat": "", "weibo": "", "xiaomiun": ""
                }
        result = self.myhttp('POST', self.selfurl,json.dumps(data),1)
        print (result)
        js = json.loads(result)
        # self.assertEqual(10020, js['code'])
        self.assertIn('手机短信码已过期', js['message'])

