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


class ricecollectallTest(MyTest):
    '''获取用户收藏的米信息'''
    url_path = '/v1/ricecollect/allfavricebydid'

    @classmethod
    def setUpClass(cls):
        pass


    def test_allfavricebydid_success(self):
        '''所有参数都传，获取成功'''
        params = 'deviceid=1128170&pageno=2&perpage=2'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'deviceid': '1128170','pageno ':'2','perpage':'2'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("查找记录成功", js['message'])

    def test_allfavricebydid_btsuccess(self):
        '''只传必填参数，获取成功'''
        params = 'deviceid=1128170'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("查找记录成功", js['message'])


    def test_allfavricebydid_delose(self):
        '''deviceid未传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn(" parameter 'deviceid' is not present", js['message'])


    def test_allfavricebydid_denull(self):
        '''deviceid的值为空'''
        params = 'deviceid='
        r = self.myhttp('GET',
                        self.url_path,
                        params
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn(" parameter 'deviceid' is not present", js['message'])


    def test_allfavricebydid_depanull(self):
        '''deviceid为空'''
        params = '=1128170'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn(" parameter 'deviceid' is not present", js['message'])


    def test_allfavricebydid_signerror(self):
        '''sign不正确'''
        params = {'deviceid': '1128170'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])





    def test_allfavricebydid_noncerror(self):
        '''nonce不正确'''
        params = {'deviceid': '1128170'}
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
        # params = urllib.urlencode({'id': 1})
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