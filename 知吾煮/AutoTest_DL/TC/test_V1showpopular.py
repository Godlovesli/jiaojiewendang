#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import requests
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class showpopularTest(MyTest):
    '''获取食谱相关优秀作品'''
    url_path =  '/v1/show/popular'

    @classmethod
    def setUpClass(cls):
        pass


    def test_showpopular_success(self):
        '''获取成功'''
        token = Login().login()  # 引用登录
        r = self.nosign('GET',
                         self.url_path,
                         { 'recipeId': '256'},
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取成功', js['message'])

    def test_showpopular_success1(self):
        '''获取成功'''
        token = Login().login()  # 引用登录
        r = self.nosign('GET',
                         self.url_path,
                         { 'recipeId': '256'},
                        token
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取成功', js['message'])


    def test_showpopular_success11(self):
        self.base_url = 'http://10.0.10.100:17002'
        self.url = self.base_url + '/v1/show/popular'
        self.nonce = generateNonce()
        self.key = getSessionSecurity(self.nonce)
        self.signature = generateSignature(self.nonce, 'GET', self.url)
        token='OTIxZWIxMjhhMGU4YmU3ZDljM2I4MWJmMTI1MGU2ZDQ='
        self.headers = {'User-Agent': 'chunmiapp',
                       'token': token
                   }
        params = {'recipeId': '256'}
        # payload1 = urllib.urlencode(params)
        # print payload1
        # encoded = encryptAES(payload1, self.key)
        # data = {'data': encoded}
        # print data
        # payload = urllib.urlencode(data)
        # print payload
        r = requests.get(self.url, params=params,  headers=self.headers)
        print r
        code =r.status_code
        print code
        result = r.text.encode()
        print result
        # s = decryptAES(result, self.key)
        # print s
        # js = json.loads(s)
        # self.assertEqual(js['state'], 1)


