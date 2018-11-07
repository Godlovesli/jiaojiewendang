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


class v1followingattentionCancelTest(MyTest):
    '''取消关注'''
    url_path = '/v1/social/following/attentionCancel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_followingattentionC_success(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        print token
        # token = 'NDQzOTU0NWNmOGVhMTYyNDRhODYzNzRkZmU1Njg0ZTk='
        params = 'followingid=1062'
        print params
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('取关成功', js['message'])



    def test_followingattentionC_success1(self):
        '''所有参数都不传'''
        token = Login().login()  # 引用登录
        params = ''
        print params
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required long parameter 'followingid' is not present", js['message'])

    def test_followingattentionC_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'followingid=1117'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token+'ee'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],  -3)
        self.assertIn('token无效', js['message'])

    def test_followingattentionC_tokenull(self):
        '''未传入token'''
        params = 'followingid=1117'
        r = self.myhttp('POST',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_followingattentionC_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'followingid': '1117'}
        print params
        r = self.signerror('POST',
                        self.url_path,
                            params,
                           self.token
                           )
        print r



    def test_followingattentionC_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'followingid': '1117'}
        print params
        r = self.noncerror('POST',
                        self.url_path,
                            params,
                           self.token
                           )
        print r



