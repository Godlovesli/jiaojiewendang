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


class v1minepublishlistTest(MyTest):
    '''我发布的'''
    url_path = '/v1/operation/history/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_publishlist_success(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        # token ='ZWRjOTMxYjg5YTNlNjZjOTU5NmY5ZGZkMDFmMmM4Mzc='
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
        self.assertIn('操作成功', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['content']
            # print js['result'][i]['type']


    def test_publishlist_success1(self):
        '''所有参数都不传'''
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
        self.assertIn('操作成功', js['message'])

    def test_publishlist_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+'ee'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],  -3)
        self.assertIn('token无效', js['message'])

    def test_publishlist_tokenull(self):
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


    def test_publishlist_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'': ''}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r



    def test_publishlist_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'': ''}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r


