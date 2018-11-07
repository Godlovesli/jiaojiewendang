#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.V1base import MyTest
from base.mydb import MyDB
from base.login import Login
import unittest
import requests
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class checkIVersionTest(MyTest):
    '''APP获取最新版本(IOS)'''
    url_path = '/app/checkIVersion'

    @classmethod
    def setUpClass(cls):
        pass

    def test_checkIVersion_success(self):
        '''所有参数都传'''
        # token='OWE2ODAwMzUxZjJjZjYxNmUwM2IwYTY1NGFjZTJkYmY='
        params = ''
        print params
        r = self.bujiami('GET',
                        self.url_path,
                         params

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('新版本获取成功', js['message'])

    def test_checkIVersion_success11(self):
        self.base_url = 'http://10.0.10.100:17002'
        self.url = self.base_url + '/app/checkIVersion'
        self.nonce = generateNonce()
        self.key = getSessionSecurity(self.nonce)
        self.signature = generateSignature(self.nonce, 'GET', self.url)
        self.headers = {'nonce': self.nonce,
                        'User-Agent': 'chunmiapp',
                        'signature': self.signature

                        }
        params = {'': ''}
        payload1 = urllib.urlencode(params)
        print payload1
        encoded = encryptAES(payload1, self.key)
        data = {'data': encoded}
        print data
        payload = urllib.urlencode(data)
        print payload
        r = requests.get(self.url, params=payload,  headers=self.headers)
        print r
        code =r.status_code
        print code
        result = r.text.encode()
        print result
        s = decryptAES(result, self.key)
        print s
        js = json.loads(s)
        self.assertEqual(js['state'], 1)
        # self.assertIn('get recipecooktempletscript success', js['message'])


