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


class ricecollectdelTest(MyTest):
    '''删除收藏记录'''
    url_path = '/ricecollect/del'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecollectdel_success(self):
        '''所有参数都传,删除收藏记录成功'''
        params = 'deviceid=1128170&riceid=1558'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid': '1128170','riceid':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("删除收藏记录成功", js['message'])


    def test_ricecollectdel_rino(self):
        '''米ID不存在'''
        params = 'deviceid=1128170&riceid=1231231231558'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid': '1128170', 'riceid': '1231231231558'}
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("删除收藏记录成功", js['message'])


    def test_ricecollectdel_deno(self):
        '''设备ID不存在'''
        params = 'deviceid=1231231128170&riceid=1558'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid': '1231231128170','riceid':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("删除收藏记录成功", js['message'])


    def test_ricecollectdel_delose(self):
        '''deviceid未传'''
        params = 'riceid=1558'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'riceid':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("删除收藏记录出现错误", js['message'])


    def test_ricecollectdel_denull(self):
        '''deviceid的值为空'''
        params = 'deviceid=&riceid=1558'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid':'','riceid':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("删除收藏记录出现错误", js['message'])


    def test_ricecollectdel_depanull(self):
        '''deviceid为空'''
        params = '=1128170&riceid=1558'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'':'1128170','riceid':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("删除收藏记录出现错误", js['message'])


    def test_ricecollectdel_rilose(self):
        '''riceid未传'''
        params = 'deviceid=1128170'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid':'1128170'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("删除收藏记录出现错误", js['message'])


    def test_ricecollectdel_rinull(self):
        '''riceid的值为空'''
        params = 'deviceid=1128170&riceid='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid':'1128170','riceid':''}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("删除收藏记录出现错误", js['message'])


    def test_ricecollectdel_ripanull(self):
        '''riceid为空'''
        params = 'deviceid=1128170&=1558'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceid':'1128170','':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("删除收藏记录出现错误", js['message'])


    def test_ricecollectdel_signerror(self):
        '''sign不正确'''
        params = {'deviceid':'1128170','riceid':'1558'}
        print params
        r = self.signerror('POST',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode( {'deviceid':'1128170','riceid':'1558'})
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
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_ricecollectdel_noncerror(self):
        '''sign不正确'''
        params = {'deviceid':'1128170','riceid':'1558'}
        print params
        r = self.noncerror('POST',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode( {'deviceid':'1128170','riceid':'1558'})
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
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
