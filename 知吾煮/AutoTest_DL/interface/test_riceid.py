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


class riceidTest(MyTest):
    '''根据ID获取米详情'''
    url_path = '/rice/id'

    @classmethod
    def setUpClass(cls):
        pass

    def test_riceid_success(self):
        '''所有参数都传'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM mipot_rice WHERE state='2200'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        riceid = rows['id']
        print riceid
        params = 'id='+str(riceid)
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'id': riceid}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取米详情成功", js['message'])


    def test_riceid_idno(self):
        '''传入不存在的米ID'''
        params = 'id=20161219080987638'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'id': '20161219080987638'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 0)
        self.assertIn("没有找到此米详情", js['message'])


    def test_riceid_idlose(self):
        '''id未传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'': ''}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'id' is not present", js['message'])


    def test_riceid_idnull(self):
        '''id的值为空'''
        params = 'id='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'id': ''}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'id' is not present", js['message'])


    def test_riceid_idpanull(self):
        '''id为空'''
        params = '=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'': '1'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'id' is not present", js['message'])

    def test_riceid_signerror(self):
        '''sign不正确'''
        params = {'pageno': '1','perpage':'5'}
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
        # params = urllib.urlencode({'id': 1})
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
        params = {'pageno': '1', 'perpage': '5'}
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