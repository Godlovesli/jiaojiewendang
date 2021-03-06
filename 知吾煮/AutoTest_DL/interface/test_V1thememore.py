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
        params = 'pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params

                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('success',js['message'])


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

    def test_thememore_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno': '1', 'perpage': '10'}
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



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'pageno=1&perpage=10'
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_thememore_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno': '1', 'perpage': '10'}
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



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'pageno=1&perpage=10'
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])