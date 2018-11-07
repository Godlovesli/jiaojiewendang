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

class V1searchapphintrecipegetTest(MyTest):
    '''搜索框关键字提示接口--搜原创'''
    url_path = '/v1/community/search/app/hint/recipe/get'

    @classmethod
    def setUpClass(cls):
        pass


    def test_searchapphintrecipeget_success(self):
        '''传入必填参数'''
        params = 'content=红烧&pageno=1&perpage=200'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']

    def test_searchapphintrecipeget_success1(self):
        '''传入必填参数'''
        params = 'content=米饭'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']


        # url = self.base_url + self.url_path
        # nonce = generateNonce()
        # signature = generateSignature(nonce, "GET", url)
        # key = getSessionSecurity(nonce)
        # payload1='content=米饭'
        # encoded1 = encryptAES(payload1, key)
        # data1 = {"data": encoded1}
        # payload1 = urllib.urlencode(data1) # 把参数进行编码
        # url2= url+'?'+payload1
        # headers = {'nonce': nonce,
        #            'User-Agent': 'chunmiapp',
        #            'signature': signature}
        # request = urllib2.Request(url2,headers=headers)
        # print request
        # response = urllib2.urlopen(request)
        # result = response.read()
        # r = decryptAES(result, key)
        # print r
        # js = json.loads(r)
        # self.assertEqual(js['state'], 1)


    def test_searchapphintrecipeget_cnlose(self):
        '''必填参数content未传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_searchapphintrecipeget_cnnull(self):
        '''必填参数content的值为空'''
        params = 'content='
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_searchapphintrecipeget_cnpanull(self):
        '''必填参数content的参数为空'''
        params = '=饭'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_searchapphintrecipeget_signerror(self):
        '''sign不正确'''
        params = {'content': '饭'}
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
        # params = 'content=饭'
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
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])

    def test_searchapphintrecipeget_noncerror(self):
        '''nonce不正确'''
        params = {'content': '饭'}
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
        # params = 'content=饭'
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
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
