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
import MultipartPostHandler
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class searchapphotgetTest(MyTest):
    '''大家都在搜接口'''
    url_path = '/community/search/app/hot/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_searchapphotget_success(self):
        '''签名正确'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'':''}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_searchapphotget_success1(self):
        '''签名正确'''
        params = 'content=饭'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'content':'饭'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_searchapphotget_signerror(self):
        '''sign不正确'''
        params = {'': ''}
        print params
        r = self.signerror('GET',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + 'e'
        #                 }
        # request = urllib2.Request(self.url, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])

    def test_searchapphotget_noncerror(self):
        '''nonce不正确'''
        params = {'': ''}
        print params
        r = self.noncerror('GET',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # self.headers = {'nonce': self.nonce + 'e',
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature
        #                 }
        # request = urllib2.Request(self.url, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
