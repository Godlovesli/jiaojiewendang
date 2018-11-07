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


class v1minemsglistTest(MyTest):
    '''消息中心'''
    url_path = '/v1/mine/msg/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_msglist_success(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        params = 'pageno=1&perpage=6'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        # js = json.loads(r)
        # self.assertEqual(js['state'], 1)
        # self.assertIn('success', js['message'])

    def test_msglist_success1(self):
        '''所有参数都不传'''
        token = Login().login()  # 引用登录
        params = ''
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        # js = json.loads(r)
        # self.assertEqual(js['state'], 1)
        # self.assertIn('success', js['message'])

    def test_msglist_signerror(self):
        '''sign不正确'''
        token = Login().login()
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "GET", self.url)
        params = ''
        print '传入的参数:' + params
        encoded = encryptAES(params, self.key)
        datas = {'data': encoded}
        payload = urllib.urlencode(datas)
        url2 = self.url + '?' + payload
        request = urllib2.Request(url2)
        request.add_header('nonce', self.nonce)
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('signature', self.signature + '1')
        request.add_header('token', token)
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])

    def test_msglist_noncerror(self):
        '''nonce不正确'''
        token = Login().login()
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "GET", self.url)
        params = ''
        print '传入的参数:' + params
        encoded = encryptAES(params, self.key)
        datas = {'data': encoded}
        payload = urllib.urlencode(datas)
        url2 = self.url + '?' + payload
        request = urllib2.Request(url2)
        request.add_header('nonce', self.nonce + '1')
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('signature', self.signature)
        request.add_header('token', token)
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])
