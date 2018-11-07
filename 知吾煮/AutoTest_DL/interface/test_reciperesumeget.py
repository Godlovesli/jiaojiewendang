#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
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


class resumegetTest(MyTest):
    '''具有断点开盖功能的食谱列表接口'''
    url_path = '/recipe/resume/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_resumeget_success(self):
        '''传必填参数'''
        params = 'pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'pageno': '1', 'perpage': '10'}
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)



    def test_resumeget_panull(self):
        '''pageno未传'''
        params = 'perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'perpage': '10'}
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_resumeget_penull(self):
        '''perpage'''
        params = 'pageno=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'pageno': '1'}
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)


    def test_resumeget_signerror(self):
        '''sign不正确'''
        params = {'pageno': '1', 'perpage': '10'}
        r = self.signerror('GET',
                           self.url_path,
                           params,
                           # {'deviceid':'1128170','':'1558'}
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode( {'pageno': '1', 'perpage': '10'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + 'e'
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_resumeget_noncerror(self):
        '''nonce不正确'''
        params = {'pageno': '1', 'perpage': '10'}
        r = self.noncerror('GET',
                           self.url_path,
                           params,
                           # {'deviceid':'1128170','':'1558'}
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode( {'pageno': '1', 'perpage': '10'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce + 'e',
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])



