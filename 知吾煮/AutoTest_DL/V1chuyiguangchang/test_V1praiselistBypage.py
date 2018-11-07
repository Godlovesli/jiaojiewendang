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


class v1praiselistBypageTest(MyTest):
    '''查询主题点赞列表'''
    url_path = '/v1/topic/praise/listBypage'

    @classmethod
    def setUpClass(cls):
        pass

    def test_praiselistBypage_success(self):
        '''获取成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from  mipot_topic where is_deleted != '1' and praiseCount > '0' "
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'pageno=1&perpage=10&topicId=' + str(id)
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])

    def test_praiselistBypage_palose(self):
        ''' pageno未传'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from  mipot_topic where is_deleted != '1' and praiseCount > '0'  "
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'perpage=10&topicId=' + str(id)
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])


    def test_praiselistBypage_pelose(self):
        '''perpage未传'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from  mipot_topic where is_deleted != '1' and praiseCount > '0' "
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'pageno=1&topicId=' + str(id)
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])

    def test_praiselistBypage_idlose(self):
        '''topicId未传，获取失败'''
        params = 'pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])


    def test_praiselistBypage_idpanull(self):
        '''topicId的参数为空，获取失败'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from  mipot_topic where is_deleted != '1' and praiseCount > '0' "
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'pageno=1&perpage=10&'+ str(id)
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])


    def test_praiselistBypage_idnull(self):
        '''topicId的值为空，获取失败'''
        params = 'pageno=1&perpage=10&topicId='
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])


    def test_praiselistBypage_signerror(self):
        '''sign不正确'''
        params = {'perpage': '10', 'pageno': '1','topicId':'6'}
        # params = 'pageno=1&perpage=10&topicId=6'
        r = self.signerror('GET',
                        self.url_path,
                        params,
                        )
        print r



    def test_praiselistBypage_noncerror(self):
        '''nonce不正确'''
        params = {'perpage': '10', 'pageno': '1','topicId':'6'}
        # params = 'pageno=1&perpage=10&topicId=6'
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        )
        print r











