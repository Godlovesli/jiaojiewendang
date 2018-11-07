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


class v1minefollowerlistTest(MyTest):
    '''我的关注者'''
    url_path = '/v1/social/follower/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_followerlist_success(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        # token='ODIwYWUwYTkwYTVhNzg4MzAwZGI2MzkzYzhjYjQyZjg='
        params = 'targetCustomerId=1096&pageno=1&perpage=20&customerid=1081'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取粉丝列表成功', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['nickname']


    # def test_followerlist_success1(self):
    #     '''所有参数都不传'''
    #     token = Login().login()  # 引用登录
    #     params = 'targetCustomerId=1078'
    #     print params
    #     r = self.myhttp('GET',
    #                     self.url_path,
    #                     params,
    #                     token
    #                     )
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['state'], 1)
    #     self.assertIn('获取粉丝列表成功', js['message'])
    #     print len(js['result'])
    #     for i in range(len(js['result'])):
    #         print js['result'][i]['nickname']

    def test_followerlist_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        # params = 'targetCustomerId=1096&pageno=1&perpage=20&customerid=1081'
        params = {'targetCustomerId': '1096','pageno':'1','perpage':'20','customerid':'1081'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r



    def test_followerlist_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        # params = 'targetCustomerId=1096&pageno=1&perpage=20&customerid=1081'
        params = {'targetCustomerId': '1096','pageno':'1','perpage':'20','customerid':'1081'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r

