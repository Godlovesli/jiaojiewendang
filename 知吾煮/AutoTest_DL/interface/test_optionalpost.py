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

class optionalpostTest(MyTest):
    '''把食谱设置成设备的自选食谱'''
    url_path = '/recipe/optional/post'

    @classmethod
    def setUpClass(cls):
        pass

    def test_optionalpost_success(self):
        '''所有参数都填，操作成功'''
        token = Login().login()  # 引用登录
        params = 'deviceId=994706&recipeId=256'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], 1)
        self.assertIn('操作成功',js['message'])


    def test_optionalpost_delose(self):
        '''测试参数不完整，必填参数(deviceId)未传'''
        params = 'recipeId=256'
        token = Login().login()  # 引用登录
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('操作失败',js['message'])


    def test_optionalpost_denull(self):
        '''必填字段(deviceId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'deviceId=&recipeId=256'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('操作失败',js['message'])


    def test_optionalpost_depanull(self):
        '''必填字段(deviceId)为空'''
        token = Login().login()  # 引用登录
        params = '=994706&recipeId=256'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('操作失败',js['message'])

    def test_optionalpost_relose(self):
        '''测试参数不完整，必填参数(reviceId)未传'''
        token = Login().login()  # 引用登录
        params = 'deviceId=994706'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('操作失败', js['message'])

    def test_optionalpost_renull(self):
        '''必填字段(reviceId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'deviceId=994706&recipeId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('操作失败', js['message'])

    def test_optionalpost_repanull(self):
        '''必填字段(reviceId)为空'''
        params = 'deviceId=994706&=256'
        token = Login().login()  # 引用登录
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('操作失败', js['message'])

    # 文档上写错了，因为要适配插件版，所以把token取消了
    # def test_optionalpost_tokenerror(self):
    #     '''token错误'''
    #     token = Login().login()  # 引用登录
    #     r = self.myhttp('POST',
    #                     self.url_path,
    #                     {'deviceId': '994706',
    #                      'recipeId': '256'},
    #                     token+'e'
    #                     )
    #     print r
    #     js = json.loads(r)
    #     print js
    #     self.assertEqual(js['state'], -3)
    #     self.assertIn('token无效', js['message'])
    #
    #
    # def test_optionalpost_tokennull(self):
    #     '''未传入token'''
    #     r = self.myhttp('POST',
    #                     self.url_path,
    #                     {'deviceId': '994706', 'recipeId': '256'},
    #
    #                     )
    #     print r
    #     js = json.loads(r)
    #     print js
    #     self.assertEqual(js['state'], -3)
    #     self.assertIn('token无效', js['message'])


    def test_optionalpost_signerror(self):
        '''sign不正确'''

        params ={'deviceId': '994706', 'recipeId': '256'}
        print params
        r = self.signerror('POST',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode(  {'deviceId': '994706', 'recipeId': '256'})
        # print u"传入的参数为：" + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # request.add_header('token', self.token )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_optionalpost_noncerror(self):
        '''nonce不正确'''
        params = {'deviceId': '994706', 'recipeId': '256'}
        print params
        r = self.noncerror('POST',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode(  {'deviceId': '994706', 'recipeId': '256'})
        # print u"传入的参数为：" + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature )
        # request.add_header('token', self.token )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
