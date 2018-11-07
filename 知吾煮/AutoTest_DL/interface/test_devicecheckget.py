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

class devicecheckgetTest(MyTest):
    '''同步小米记录的设备和纯米记录的设备'''
    url_path = '/v1/device/check/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_devicecheckget_success(self):
        '''所有参数都传，操作成功'''
        token = Login().login()  # 引用登录
        params = 'deviceId=994706'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], 1)
        self.assertIn('操作成功',js['message'])


    def test_devicecheckget_delose(self):
        '''测试参数不完整，必填参数(deviceId)未传'''
        token = Login().login()  # 引用登录
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], 1)
        self.assertIn('操作成功',js['message'])


    def test_devicecheckget_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        params = 'deviceId=994706'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+'e'
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_devicecheckget_tokennull(self):
        '''未传入token'''
        params = 'deviceId=994706'
        r = self.myhttp1('GET',
                        self.url_path,
                         params,

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_devicecheckget_signerror(self):
        '''sign不正确'''
        params = {'deviceId': '994706'}
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
        # params = urllib.urlencode( {'deviceId': '994706'})
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
        #


    def test_devicecheckget_noncerror(self):
        '''nonce不正确'''

        params = {'deviceId': '994706'}
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
        # params = urllib.urlencode( {'deviceId': '994706'})
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