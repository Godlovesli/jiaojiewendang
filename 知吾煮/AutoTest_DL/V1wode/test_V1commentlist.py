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


class v1minecommentlistTest(MyTest):
    '''评论与赞[评论]'''
    url_path = '/v1/mine/comment/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_commentlist_success(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        # token='OWE2ODAwMzUxZjJjZjYxNmUwM2IwYTY1NGFjZTJkYmY='
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
        self.assertIn('获取评论成功', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['content']

    def test_commentlist_success1(self):
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
        self.assertIn('获取评论成功', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['content']

    def test_commentlist_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno': '1','perpage':'6'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r


    def test_commentlist_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno': '1','perpage':'6'}
        print params
        r = self.noncerror('GET',
                           self.url_path,
                           params,
                           self.token
                           )
        print r

