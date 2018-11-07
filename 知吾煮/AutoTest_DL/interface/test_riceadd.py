#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
import requests
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cjcryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class riceaddTest(MyTest):
    '''添加米'''
    url_path = '/rice/add'

    @classmethod
    def setUpClass(cls):
        pass

    def test_riceadd_success(self):
        '''所有参数都传,添加成功'''
        params = 'deviceid=132755445&name=TSJK016&brand=brand14&ppties=testsx016&barCode=48910816550716'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid': '132755445','name':'TSJK016','brand':'brand14','ppties':'testsx016','barCode':'48910816550716'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("添加米详情成功", js['message'])


    def test_riceadd_btsuccess(self):
        '''只传必填字段，添加成功'''
        params = 'deviceid=132755445'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid': '132755445'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("添加米详情成功", js['message'])


    def test_riceadd_delose(self):
        '''deviceid未传'''
        params = 'name=TSJK016&brand=brand14&ppties=testsx016&barCode=48910816550716'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'name':'TSJK014','brand':'brand14','ppties':'testsx014','barCode':'48910816550714'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("添加米详情发生错误!deviceid null", js['message'])


    def test_riceadd_denull(self):
        '''deviceid的值为空'''
        params = 'deviceid=&name=TSJK016&brand=brand14&ppties=testsx016&barCode=48910816550716'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid':'','name':'TSJK014','brand':'brand14','ppties':'testsx014','barCode':'48910816550714'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("添加米详情发生错误!deviceid null", js['message'])


    def test_riceadd_depanull(self):
        '''deviceid为空'''
        params = '=132755445&name=TSJK016&brand=brand14&ppties=testsx016&barCode=48910816550716'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'':'132755445','name':'TSJK014','brand':'brand14','ppties':'testsx014','barCode':'48910816550714'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("添加米详情发生错误!deviceid null", js['message'])


    def test_optionalpost_signerror(self):
        '''sign不正确'''
        params = {'deviceid': '132755445','name':'TSJK014','brand':'brand14','ppties':'testsx014','barCode':'48910816550714'}
        r = self.signerror('POST',
                        self.url_path,
                        params,
                        # {'deviceid':'1128170','':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode( {'deviceid': '132755445','name':'TSJK014','brand':'brand14','ppties':'testsx014','barCode':'48910816550714'})
        # print u"传入的参数为：" + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_optionalpost_noncerror(self):
        '''nonce不正确'''
        params = {'deviceid': '132755445','name':'TSJK014','brand':'brand14','ppties':'testsx014','barCode':'48910816550714'}
        r = self.noncerror('POST',
                        self.url_path,
                        params,
                        # {'deviceid':'1128170','':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode( {'deviceid': '132755445','name':'TSJK014','brand':'brand14','ppties':'testsx014','barCode':'48910816550714'})
        # print u"传入的参数为：" + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
