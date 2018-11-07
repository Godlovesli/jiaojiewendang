#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
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


class v1recipeminegetTest(MyTest):
    '''我创建的食谱'''
    url_path = '/v1/recipe/mine/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipemineget_success(self):
        '''传必填参数'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_recipemineget_palose(self):
        '''pageno未传，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'perpage=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_correlationget_papanull(self):
        '''pageno的参数为空，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = '=2&perpage=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_correlationget_panull(self):
        '''pageno的值为空，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=&perpage=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_correlationget_pelose(self):
        '''perpage未传，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_correlationget_pepanull(self):
        '''perpage的参数为空，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=1&=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_correlationget_penull(self):
        '''perpage的参数值为空，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=1&perpage='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_correlationget_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageno=1&perpage=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+'3e'
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])

    def test_correlationget_tokenull(self):
        '''未传入token'''
        params = 'pageno=1&perpage=6'
        r = self.myhttp1('GET',
                        self.url_path,
                        params,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])



    def test_correlationget_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno': '1','perpage':'6'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params,
                        self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'pageno=1&perpage=6'
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_correlationget_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno': '1','perpage':'6'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'pageno=1&perpage=6'
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])











