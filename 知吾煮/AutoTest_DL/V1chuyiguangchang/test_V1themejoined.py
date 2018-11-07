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


class v1themejoinedTest(MyTest):
    '''我参与过的话题'''
    url_path = '/v1/community/theme/joined'

    @classmethod
    def setUpClass(cls):
        pass

    def test_themejoined_success(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        print token
        params = 'perpage=20'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('success', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['title']

    def test_themejoined_btsuccess(self):
        '''只传必填参数'''
        token = Login().login()  # 引用登录
        params = ''
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('success', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['title']

    def test_themejoined_tokennull(self):
        '''未传入token'''
        params = ''
        r = self.myhttp1('GET',
                        self.url_path,
                        params,

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_themejoined_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+ '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_themejoined_signerror(self):
        '''sign不正确'''
        token = Login().login()
        params = {'': ''}
        r = self.signerror('GET',
                           self.url_path,
                           params,
                           token
                           )

        print r

    def test_themejoined_noncerror(self):
        '''nonce不正确'''
        token = Login().login()
        params = {'': ''}
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r

