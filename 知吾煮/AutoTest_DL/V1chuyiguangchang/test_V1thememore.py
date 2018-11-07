#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
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


class v1thememoreTest(MyTest):
    '''获取更多话题'''
    url_path = '/v1/community/theme/more'

    @classmethod
    def setUpClass(cls):
        pass

    def test_thememore_success(self):
        '''所有参数都传'''
        params = 'pageno=1&perpage=100'
        r = self.myhttp('GET',
                        self.url_path,
                        params

                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('success',js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            # print js['result'][i]['content']
            print js['result'][i]['title']
            # print js['result'][i]['deleted']


    def test_thememore_pano(self):
        '''所有参数都不传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params

                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('success',js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['content']
            print js['result'][i]['deleted']


    def test_thememore_signerror(self):
        '''sign不正确'''
        params = {'pageno': '1','perpage':'100'}
        r = self.signerror('GET',
                           self.url_path,
                           params
                           )

        print r



    def test_thememore_noncerror(self):
        '''nonce不正确'''
        params = {'pageno': '1','perpage':'100'}
        r = self.noncerror('GET',
                           self.url_path,
                           params
                           )

        print r