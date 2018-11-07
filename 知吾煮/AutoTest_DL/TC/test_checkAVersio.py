#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
from base.login import Login
import unittest
import json
import requests
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class checkAVersioTest(MyTest):
    '''APP获取最新版本(ANDROID)'''
    url_path = '/app/checkAVersion'

    @classmethod
    def setUpClass(cls):
        pass

    def test_checkAVersio_success(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        # token='OWE2ODAwMzUxZjJjZjYxNmUwM2IwYTY1NGFjZTJkYmY='
        # params = ''
        # print params
        r = self.bujiami('GET',
                        self.url_path,
                         {'':''}

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('新版本获取成功', js['message'])


    def test_checkAVersio_success1(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        # token='OWE2ODAwMzUxZjJjZjYxNmUwM2IwYTY1NGFjZTJkYmY='
        # params = ''
        # print params
        r = self.bujiami('GET',
                         self.url_path,
                         {'': ''},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('新版本获取成功', js['message'])

    def test_checkAVersio_success11(self):
        self.base_url = 'http://10.0.10.100:17002'
        self.url = self.base_url + '/app/checkAVersion'
        self.nonce = generateNonce()
        self.key = getSessionSecurity(self.nonce)
        self.signature = generateSignature(self.nonce, 'GET', self.url)
        self.headers = {'nonce': self.nonce,
                        'User-Agent': 'chunmiapp',
                        'signature': self.signature
                        }
        r = requests.get(self.url,  headers=self.headers)
        print r
        code =r.status_code
        print code
        result = r.text.encode()
        print result
        s = decryptAES(result, self.key)
        print s
        js = json.loads(s)
        self.assertEqual(js['state'], 1)
        self.assertIn('新版本获取成功', js['message'])

