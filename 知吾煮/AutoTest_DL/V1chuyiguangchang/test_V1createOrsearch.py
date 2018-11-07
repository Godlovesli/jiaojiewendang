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


class v1createOrsearchTest(MyTest):
    '''创建及搜索话题'''
    url_path = '/v1/community/theme/searchOrcreate'

    @classmethod
    def setUpClass(cls):
        pass

    def test_createOrsearch_success(self):
        '''所有参数都传'''
        # params = {'perpage': '6', 'pageno': '1', 'keyword':'5'}
        params = 'pageno=1&perpage=6&keyword=美'
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


    def test_createOrsearch_btsuccess(self):
        '''所有参数都传'''
        params = 'keyword=知'
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

