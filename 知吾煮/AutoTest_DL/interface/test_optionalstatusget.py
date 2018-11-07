#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
import requests
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class optionalstatusgetTest(MyTest):
    '''查询食谱是不是自选食谱'''
    url_path = '/recipe/optional/status/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_optionalstatusget_success(self):
        '''查询食谱是不是自选食谱'''
        token = Login().login()  # 引用登录
        params = 'deviceIds=994706&recipeId=256'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        # self.assertEqual(js['state'], 1)

    def test_optionalstatusget_delose(self):
        '''测试参数不完整，必填参数(deviceId)未传'''
        token = Login().login()  # 引用登录
        params = 'recipeId=256'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js


    def test_optionalstatusget_relose(self):
        '''测试参数不完整，必填参数(reviceId)未传'''
        token = Login().login()  # 引用登录
        params = 'deviceIds=994706'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js


    def test_optionalstatusget_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        params = 'deviceIds=994706&recipeId=256'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+'e'
                        )
        print r
        js = json.loads(r)
        print js


    def test_devicecheckget_tokennull(self):
        '''未传入token'''
        params = 'deviceIds=994706&recipeId=256'
        r = self.myhttp1('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        print js

    def test_devicecheckget_signerror(self):
        '''sign不正确'''
        params ={'deviceIds': '994706', 'recipeId': '256'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'deviceIds': '994706', 'recipeId': '256'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])



    def test_devicecheckget_noncerror(self):
        '''nonce不正确'''
        params ={'deviceIds': '994706', 'recipeId': '256'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'deviceIds': '994706', 'recipeId': '256'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])