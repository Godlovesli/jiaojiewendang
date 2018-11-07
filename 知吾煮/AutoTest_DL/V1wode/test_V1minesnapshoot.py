#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v1minesnapshootlistTest(MyTest):
    '''我的信息快照'''
    url_path = '/v1/mine/snapshoot'

    @classmethod
    def setUpClass(cls):
        pass

    def test_snapshoot_success(self):
        '''发送请求'''
        token = Login().login()  # 引用登录
        # token='Mjk0ZGQ4ZWY4OTY0OWNjYmM3NTNiNTYwZWIwMGUwZjU='
        params = 'pageno=1&perpage=6'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取用户快照成功', js['message'])


    def test_snapshoot_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno':'1','perpage':'6'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r



    def test_snapshoot_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno':'1','perpage':'6'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r

