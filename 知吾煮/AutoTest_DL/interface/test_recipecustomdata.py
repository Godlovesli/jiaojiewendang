#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
import MySQLdb
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipecustomdataTest(MyTest):
    '''获取自定义食谱列表'''
    url_path =  '/v1/recipe/custom/data/get'

    @classmethod
    def setUpClass(cls):
        pass


    def test_recipecustomdata_success(self):
        '''所有参数都传'''
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_custom"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            customid = rows['id']
            print customid
            params = 'groupid=1&pageno=1&perpage=5&customid='+str(customid)
            r = self.myhttp('GET',
                            self.url_path,
                            params,
                            # {'groupid': '1', 'customid':customid, 'pageno': '1', 'perpage': '5'},

                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
        else:
            print "不存在自定义食谱列表"



    def test_recipecustomdata_gidlose(self):
        '''必填参数groupid未传'''
        params = 'pageno=1&perpage=5&customid=20'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # { 'customid': 20, 'pageno': '1', 'perpage': '5'},
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)



    def test_recipecustomdata_gidnull(self):
        '''必填参数groupid的值为空'''
        params = 'groupid=&pageno=1&perpage=5&customid=20'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # { 'groupid': '','customid': 20, 'pageno': '1', 'perpage': '5'},
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_recipecustomdata_gidpanull(self):
        '''必填参数groupid为空'''
        params = '=1&pageno=1&perpage=5&customid=20'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # { '': '1','customid': 20, 'pageno': '1', 'perpage': '5'},
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)



    def test_recipecustomdata_cidlose(self):
        '''必填参数customid未传'''
        params = 'groupid=1&pageno=1&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # { 'groupid': '1', 'pageno': '1', 'perpage': '5'},
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("发送异常", js['message'])

    def test_recipecustomdata_cidnull(self):
        '''必填参数customid的值为空'''
        params = 'groupid=1&pageno=1&perpage=5&customid='
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # { 'groupid': '1','customid': '', 'pageno': '1', 'perpage': '5'},
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("发送异常", js['message'])

    def test_recipecustomdata_cidpanull(self):
        '''必填参数customid为空'''
        params = 'groupid=1&pageno=1&perpage=5&=20'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # { 'groupid': '1','': '20', 'pageno': '1', 'perpage': '5'},
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("发送异常", js['message'])


    def test_recipecustomdata_signerror(self):
        '''sign不正确'''
        params ={ 'groupid': '1','customid': '20', 'pageno': '1', 'perpage': '5'}
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
        # params = urllib.urlencode( { 'groupid': '1','customid': '20', 'pageno': '1', 'perpage': '5'})
        # print '输入参数：'+params
        # request = urllib2.Request(self.url + '?' + params)
        # request.add_header('nonce',self.nonce)
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature+'1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_recipecustomdata_noncerro(self):
        '''nonce不正确'''
        params ={ 'groupid': '1','customid': '20', 'pageno': '1', 'perpage': '5'}
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
        # params = urllib.urlencode( { 'groupid': '1','customid': '20', 'pageno': '1', 'perpage': '5'})
        # print '输入参数：'+params
        # request = urllib2.Request(self.url + '?' + params)
        # request.add_header('nonce',self.nonce+'1')
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])














