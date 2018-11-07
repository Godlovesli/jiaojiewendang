#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.mydb import MyDB
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


class articletopadvTest(MyTest):
    '''常用banner、自选banner、列表banner(6201常用banner、6202自选banner、6203列表banner)'''
    url_path =  '/v1/article/topadv'

    @classmethod
    def setUpClass(cls):
        pass

    def test_articletopadv_sysuccess(self):
        '''传所有参数'''
        db = MyDB().getCon()
        #db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM mipot_article WHERE type = '6202'and state='2200' and devicemodel_groupid='1'"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchall()
        print rows
        for row in rows:
            print row
        params = 'type=6202&dmid=45423531'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'type': '6202',
                        #  'dmid':'45423531'}
                        )
        print r
        js = json.loads(r)
        if data_count > 0:
            self.assertEqual(js['state'], 1)
            self.assertIn('banner数据获取成功', js['message'])
            print row['title']
            print js['result'][0]['title']
            # print js['result'][1]['title']

        else:
            self.assertEqual(js['state'], 0)
            self.assertIn('头部banner没有数据', js['message'])


    def test_articletopadv_cysuccess(self):
        '''6201常用banner'''
        db = MyDB().getCon()
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM mipot_article WHERE type = '6201'and state='2200'"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchall()
        print rows
        for row in rows:
            print row
        params = 'type=6202'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'type': '6201'}
                        )
        print r
        js = json.loads(r)
        if data_count > 0:
            self.assertEqual(js['state'], 1)
            self.assertIn('banner数据获取成功', js['message'])
            print row['title']
            print js['result'][0]['title']
            # print js['result'][1]['title']

        else:
            self.assertEqual(js['state'], 0)
            self.assertIn('头部banner没有数据', js['message'])


    def test_articletopadv_zxsuccess(self):
        '''6202自选banner'''
        db = MyDB().getCon()
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM mipot_article WHERE type = '6202'and state='2200'"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchall()
        print rows
        for row in rows:
            print row
        params = 'type=6202'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'type': '6202'}
                        )
        print r
        js = json.loads(r)
        if data_count > 0:
            self.assertEqual(js['state'], 1)
            self.assertIn('banner数据获取成功', js['message'])
            print row['title']
            print js['result'][0]['title']
            # print js['result'][1]['title']

        else:
            self.assertEqual(js['state'], 0)
            self.assertIn('头部banner没有数据', js['message'])


    def test_articletopadv_lbsuccess(self):
        '''6203列表banner'''
        db = MyDB().getCon()
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM mipot_article WHERE type = '6203'and state='2200'"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchall()
        print rows
        for row in rows:
            print row
        params = 'type=6203'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'type': '6203'}
                        )
        print r
        js = json.loads(r)
        if data_count > 0:
            self.assertEqual(js['state'], 1)
            self.assertIn('banner数据获取成功', js['message'])
            self.assertEqual(row['title'],js['result'][0]['title'])
            print row['title']
            print js['result'][0]['title']
        else:
            self.assertEqual(js['state'], 0)
            self.assertIn('头部banner没有数据', js['message'])


    def test_articletopadv_tylose(self):
        '''type未传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'':''}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'type' is not present", js['message'])

    def test_articletopadv_tynull(self):
        '''type的值为空'''
        params = 'type='
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'type':''}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'type' is not present", js['message'])


    def test_articletopadv_typanull(self):
        '''type为空'''
        params = '=6201'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'':'6201'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'type' is not present", js['message'])


    def test_articletopadv_signerror(self):
        '''sign不正确'''
        params ={'type':'6201'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'type':'6201'})
        # request = urllib2.Request(self.url+params)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_articletopadv_noncerror(self):
        '''nonce不正确'''
        params ={'type':'6201'}
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
        # params = urllib.urlencode({'type': '6201'})
        # request = urllib2.Request(self.url + params)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])



