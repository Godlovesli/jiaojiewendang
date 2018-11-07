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


class ricebarcodeTest(MyTest):
    '''根据ID获取米详情'''
    url_path = '/rice/barcode'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricebarcode_success(self):
        '''扫码获取米详情,所有参数都传'''
        # db = MyDB().getCon()
        # cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        # sql = "SELECT A.barCode ,B.deviceid FROM mipot_rice A,mipot_device B WHERE A.state='2200'"
        # data_count = cursor.execute(sql)
        # print data_count
        # cursor.scroll(0)
        # rows = cursor.fetchone()
        # print rows
        # barCode = rows['barCode']
        # deviceid = rows['deviceid']
        # print barCode
        # print deviceid
        params = 'barCode=1&deviceid=1082455'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'barCode': 1,
                        # 'deviceid':1082455 }
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取米详情成功", js['message'])


    def test_ricebarcode_btsuccess(self):
        '''扫码获取米详情,所有参数都传'''
        # # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        # db = MyDB().getCon()
        # cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        # sql = "SELECT A.barCode ,B.deviceid FROM mipot_rice A,mipot_device B WHERE A.state='2200'"
        # data_count = cursor.execute(sql)
        # print data_count
        # cursor.scroll(0)
        # rows = cursor.fetchone()
        # print rows
        # barCode = rows['barCode']
        # deviceid = rows['deviceid']
        # print barCode
        # print deviceid
        params = 'barCode=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'barCode': 1
                        #  }
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取米详情成功", js['message'])



    def test_ricebarcode_cdno(self):
        '''传入不存在的barCode'''
        params = 'barCode=20161219080987638'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'barCode': '20161219080987638'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 0)
        self.assertIn("没有找到此米信息", js['message'])



    def test_ricebarcode_idno(self):
        '''barCode未传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'': ''}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'barCode' is not present", js['message'])


    def test_ricebarcode_cdnull(self):
        '''barCode的值为空'''
        params = 'barCode='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'barCode': ''}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'barCode' is not present", js['message'])


    def test_ricebarcode_cdpanull(self):
        '''barCode为空'''
        params = '=589524678'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'': '589524678'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'barCode' is not present", js['message'])


    def test_riceid_signerror(self):
        '''sign不正确'''
        params = {'barCode': 589524678}
        r = self.signerror('GET',
                        self.url_path,
                        params,
                        # {'deviceid':'1128170','':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'barCode': 589524678})
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



    def test_riceid_noncerror(self):
        '''nonce不正确'''
        params = {'barCode': 589524678}
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        # {'deviceid':'1128170','':'1558'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'barCode': 589524678})
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