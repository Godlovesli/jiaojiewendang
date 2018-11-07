#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
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

class recipehintgetTest(MyTest):
    '''食谱详-搜索框关键字提示接口'''
    url_path = '/recipe/app/hint/get'

    @classmethod
    def setUpClass(cls):
        pass


    def test_recipehintget_success(self):
        '''所有参数都传'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_device where deviceModelId='1'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        deviceid = rows['deviceId']
        print deviceid
        params = 'content=饭&deviceid='+str(deviceid)
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_recipehintget_successbt(self):
        '''只传必填参数'''
        params = 'deviceid=45423531'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_recipehintget_successbc(self):
        '''只传必填参数'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_recipequeryget_signerror(self):
        '''sign不正确'''
        params ={'deviceid': '45423531'}
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
        # params = urllib.urlencode({'deviceid': '45423531'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + 'e'
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_recipequeryget_noncerror(self):
        '''nonce不正确'''
        params ={'deviceid': '45423531'}
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
        # params = urllib.urlencode({'deviceid': '45423531'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce + 'e',
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
