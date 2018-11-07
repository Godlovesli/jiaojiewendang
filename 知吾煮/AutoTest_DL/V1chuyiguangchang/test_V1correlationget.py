#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class V1correlationgetTest(MyTest):
    '''关联食谱查询'''
    url_path = '/recipe/correlation/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_correlationget_success(self):
        '''搜索关联食谱成功'''
        token = Login().login()  # 引用登录
        # params = {'perpage': '20', 'pageno': '1', 'content': '土豆'}
        params = 'content=土豆&pageno=1&perpage=20'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_correlationget_btsuccess(self):
        '''只传必填字段，搜索关联食谱成功'''
        token = Login().login()  # 引用登录
        print token
        # params = {'perpage': '20', 'pageno': '1'}
        params = 'pageno=1&perpage=20'
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_correlationget_palose(self):
        '''pageno未传'''
        token = Login().login()  # 引用登录
        print token
        # params = {'perpage': '6'}
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
        '''pageno的参数为空'''
        token = Login().login()  # 引用登录
        print token
        # params = {'perpage': '6', '': '1'}
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
        '''pageno的值为空'''
        token = Login().login()  # 引用登录
        print token
        # params = {'perpage': '6', 'pageno': ''}
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
        '''perpage未传'''
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
        '''perpage的参数为空'''
        token = Login().login()  # 引用登录
        print token
        params = {'': '6', 'pageno': '1'}
        # params = 'pageno=1&=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_correlationget_penull(self):
        '''perpage的参数为空'''
        token = Login().login()  # 引用登录
        print token
        # params = {'perpage': '', 'pageno': '1'}
        params = 'pageno=1&perpage='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)



    def test_correlationget_tokenull(self):
        '''未传入token'''
        # params = {'perpage': '6', 'pageno': '1'}
        params = 'pageno=1&perpage=6'
        r = self.myhttp1('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])



    def test_correlationget_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        # params = {'perpage': '6', 'pageno': '1'}
        params = 'pageno=1&perpage=6'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         token+'3e'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_correlationget_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'perpage': '6', 'pageno': '1'}
        # params = 'pageno=1&perpage=6'
        r = self.signerror('GET',
                        self.url_path,
                        params,
                        )
        print r


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
        params = {'perpage': '6', 'pageno': '1'}
        # params = 'pageno=1&perpage=6'
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        )
        print r


        #
        #
        #
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

