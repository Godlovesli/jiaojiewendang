#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
from base.mydb import MyDB
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class devicestatusgetTest(MyTest):
    '''是否注册'''
    url_path = '/v2/device/status/get'

    @classmethod
    def setUpClass(cls):
        pass


    def test_devicestatusget_deno(self):
        '''传入不存在的deviceId'''
        token = Login().login()  # 引用登录
        print token
        params = 'deviceId=1231231231'
        r = self.myhttp('GET',
                    self.url_path,
                        params,
                    token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 2)
        self.assertIn('没有注册',js['message'])


    def test_devicestatusget_deycz(self):
        '''传入存在的deviceId'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_device where userId='54644930' order by id DESC "
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        deviceId = rows['deviceId']
        print deviceId
        if data_count>0:
            params = 'deviceId='+str(deviceId)
            r = self.myhttp('GET',
                        self.url_path,
                            params,
                       token )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('已经注册',js['message'])
        else:
            print '没有注册'



    def test_devicestatusget_delose(self):
        ''' 测试参数不完整，必填参数(deviceId)未传'''
        token = Login().login()  # 引用登录
        print token
        params = ''
        r = self.myhttp('GET',
                    self.url_path,
                        params,
                    token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'deviceId' is not present",js['message'])


    def test_devicestatusget_denull(self):
        '''必填字段(deviceId)的值为空'''
        token = Login().login()  # 引用登录
        print token
        params = 'deviceId='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token)
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'deviceId' is not present", js['message'])

    def test_devicestatusget_depanull(self):
        '''必填字段(deviceId)为空'''
        token = Login().login()  # 引用登录
        print token
        params = '=81251117'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token)
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'deviceId' is not present", js['message'])


    def test_devicestatusget_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'deviceId=81251117'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+'ee')
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_devicestatusget_tokennull(self):
        '''未传入token'''
        params = 'deviceId=81251117'
        r = self.myhttp1('GET',
                        self.url_path,
                         params
                       )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_devicestatusget_signerror(self):
        '''sign不正确'''
        params = {'deviceId': '81251114'}
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
        # params = urllib.urlencode({'deviceId': '81251114'})
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2=self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature +'e')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_devicestatusget_noncerror(self):
        '''nonce不正确'''
        params = {'deviceId': '81251114'}
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
        # params = urllib.urlencode({'deviceId': '81251114'})
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2=self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce +'e')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])