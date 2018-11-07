#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import random
import requests
import MySQLdb
import MultipartPostHandler
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v1recipeminegetTest(MyTest):
    '''我创建的食谱'''
    url_path = '/recipe/mine/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipemineget_success(self):
        '''传必填参数'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_recipemineget_palose(self):
        '''pageno未传，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'perpage=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_recipemineget_papanull(self):
        '''pageno的参数为空，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = '=2&perpage=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_recipemineget_panull(self):
        '''pageno的值为空，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=&perpage=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_recipemineget_pelose(self):
        '''perpage未传，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_recipemineget_pepanull(self):
        '''perpage的参数为空，获取失败'''
        params = 'pageno=1&=6'
        token = Login().login()  # 引用登录
        print token
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_recipemineget_penull(self):
        '''perpage的参数为空，获取失败'''
        params = 'pageno=1&perpage='
        token = Login().login()  # 引用登录
        print token
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_recipemineget_tokenerror(self):
        '''token错误'''
        params = 'pageno=1&perpage=6'
        token = Login().login()  # 引用登录
        print token
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+'3e'
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])

    def test_recipemineget_tokenull(self):
        '''未传入token'''
        params = 'pageno=1&perpage=6'
        r = self.myhttp1('GET',
                        self.url_path,
                        params,
                        )

        print 'xfjs:'+ r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])




    def test_recipemineget_signerror(self):
        '''sign不正确'''
        params = {'perpage': '10', 'pageno': '1'}
        # params = 'pageno=1&perpage='
        token = Login().login()  # 引用登录
        print token
        r = self.signerror('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r



    def test_recipemineget_noncerror(self):
        '''nonce不正确'''
        params = {'perpage': '10', 'pageno': '1'}
        # params = 'pageno=1&perpage='
        token = Login().login()  # 引用登录
        print token
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r












