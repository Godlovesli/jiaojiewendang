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


class topicreportpostTest(MyTest):
    '''举报话题'''
    url_path = '/topic/report/post'

    @classmethod
    def setUpClass(cls):
        pass

    def test_topicdpost_success(self):
        '''类型为其他，所有参数都传，举报成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id='1081' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                        self.url_path,
                           {'type': 15030, 'content': u'其他', 'topicId': id},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('举报成功',js['message'])

    def test_topicreportpost_sysuccess(self):
        '''类型不为其他，传所有参数举报成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1081' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': 15000, 'content': u'其他', 'topicId': id},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('举报成功', js['message'])

    def test_topicreportpost_btsuccess(self):
        '''类型不为其他，只传必填参数举报成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1081' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': 15000,'topicId':323},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('举报成功', js['message'])

    def test_topicreportpost_idlose(self):
        '''topicId未传，举报失败'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {'content': u'其他','type':15000},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请选择话题', js['message'])

    def test_topicreportpost_idnull(self):
        '''topicId的值为空，举报失败'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': '15000', 'content': u'其他', 'topicId': ''},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请选择话题', js['message'])

    def test_topicreportpost_idpanull(self):
        '''topicId的参数为空，举报失败'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1053' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': '15030', 'content': u'其他', '': id},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请选择话题', js['message'])

    def test_topicreportpost_tylose(self):
        '''type未传，举报失败'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1053' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'content': u'其他', 'topicId': id},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请选择举报类型', js['message'])

    def test_topicreportpost_tynull(self):
        '''type的值为空，举报失败'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1053' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': '', 'content': u'其他', 'topicId': id},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请选择举报类型', js['message'])


    def test_topicreportpost_typanull(self):
        '''type的参数为空，举报失败'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1053' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'': '15030', 'content': u'其他', 'topicId': id},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请选择举报类型', js['message'])

    def test_topicreportpost_ctlose(self):
        '''类型为其他，content未传，举报失败'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1053' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': '15030', 'topicId': id},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请填写举报内容', js['message'])

    def test_topicreportpost_ctnull(self):
        '''类型为其他，content的值为空，举报失败'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1053' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': '15030', 'content': '', 'topicId': id},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请填写举报内容', js['message'])

    def test_topicreportpost_ctpanull(self):
        '''类型为其他，content的参数为空，举报失败'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1053' and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': '15030', '': u'其他', 'topicId': 323},
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('举报失败:请填写举报内容', js['message'])


    def test_topicreportpost_tokennull(self):
        '''token不传'''
        r = self.topicpost1('POST',
                           self.url_path,
                           {'type': 15000, 'content': u'其他', 'topicId': 323}
                           , )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_topicreportpost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {'type': 15000, 'content': u'其他', 'topicId': 323},
                           token+'3e')

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])





