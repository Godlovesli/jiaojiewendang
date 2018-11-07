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


class v1themesearchTest(MyTest):
    '''根据关键字搜索话题'''
    url_path = '/v1/community/theme/search'

    @classmethod
    def setUpClass(cls):
        pass

    def test_themesearch_success(self):
        '''所有参数都传'''
        params = 'pageno=1&perpage=6&keyword=的'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                            params
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('success', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['title']



    def test_themesearch_signerror(self):
        '''sign不正确'''
        params = {'pageno': '1','perpage':'6','keyword':'的'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params
                        )
        print r



    def test_themesearch_noncerror(self):
        '''nonce不正确'''

        params = {'pageno': '1','perpage':'6','keyword':'的'}
        r = self.noncerror('GET',
                           self.url_path,
                           params
                           )

        print r
