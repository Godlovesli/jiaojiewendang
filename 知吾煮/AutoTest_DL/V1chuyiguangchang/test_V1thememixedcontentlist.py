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


class v1thememixedcontentlistTest(MyTest):
    '''广场广场混合内容列表'''
    url_path = '/v1/community/theme/mixedcontentlist'

    @classmethod
    def setUpClass(cls):
        pass

    def test_thememixedcontentlist_success(self):
        '''所有参数都传'''
        # token = Login().login()  # 引用登录
        params = 'pageno=1&perpage=6'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('success', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['contentId']

    def test_thememixedcontentlist_btsuccess(self):
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



    def test_thememixedcontentlist_signerror(self):
        '''sign不正确'''
        token = Login().login()  # 引用登录
        params = {'': ''}
        r = self.signerror('GET',
                           self.url_path,
                           params,
                           token
                           )

        print r


    def test_thememixedcontentlist_noncerror(self):
        '''nonce不正确'''
        token = Login().login()  # 引用登录
        params = {'': ''}
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
