#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v1themedetailTest(MyTest):
    '''获取话题详情'''
    url_path = '/v1/community/theme/detail/'

    @classmethod
    def setUpClass(cls):
        pass

    def test_themedetail_success(self):
        '''所有参数都传'''

        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_theme where deleted!='1'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            cursor.scroll(0)
            rows = cursor.fetchone()
            print rows
            id = rows['id']
            print id
            self.url_path=self.url_path + str(id)
            params = ''
            r = self.bujiami('GET',
                            self.url_path,
                             params
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('success', js['message'])
        else:
            print "不存在话题"


    def test_themedetail_signerror(self):
        '''sign不正确'''
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_theme where deleted!='1'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        self.url_path = self.url_path + str(id)
        params = {'': ''}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        #
        # self.url = self.base_url + self.url_path + str(id)
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # request = urllib2.Request(self.url)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])




    def test_themedetail_noncerror(self):
        '''nonce不正确'''
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_theme where deleted!='1'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        self.url_path = self.url_path + str(id)
        params = {'': ''}
        print params
        r = self.noncerror('GET',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])

        # self.url = self.base_url + self.url_path + str(id)
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # request = urllib2.Request(self.url)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

