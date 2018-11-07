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


class showreportTest(MyTest):
    '''举报作品'''
    url_path = '/show/report'

    @classmethod
    def setUpClass(cls):
        pass

    def test_showreport_success(self):
        '''类型为其他，所有参数都传，举报成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        showId = rows['id']
        print showId
        params = 'type=15030&content=其他&showId='+str(showId)
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': 15030, 'content': u'其他', 'showId': showId},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('举报作品成功',js['message'])


    def test_showreport_sysuccess(self):
        '''类型不为其他，所有参数都传，举报成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        showId = rows['id']
        print showId
        params = 'type=15030&content=其他&showId=' + str(showId)
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': 15000, 'content': u'其他', 'showId': showId},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('举报作品成功', js['message'])


    def test_showreport_btsuccess(self):
        ''' 类型不为其他，只传必填参数举报成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        showId = rows['id']
        print showId
        params = 'type=15000&showId=' + str(showId)
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': 15000,  'showId': showId},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('举报作品成功', js['message'])


    def test_showreport_idlose(self):
        '''测试参数不完整，必填参数(showId)未传'''
        token = Login().login()  # 引用登录
        params = 'type=15000'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': 15000},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'show_id' cannot be null", js['message'])


    def test_showreport_idnull(self):
        '''必填字段(showid)的值为空'''
        token = Login().login()  # 引用登录
        params = 'type=15000&showId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': '', 'type': 15000},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'show_id' cannot be null", js['message'])


    def test_showreport_idpanull(self):
        '''必填参数(showid)为空'''
        token = Login().login()  # 引用登录
        params = 'type=15000&=907'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': '907', 'type': 15000},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'show_id' cannot be null", js['message'])


    def test_showreport_tylose(self):
        '''type未传，举报失败'''
        token = Login().login()  # 引用登录
        params = 'content=其他&showId=931'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'content': '123', 'showId': 931},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)

    def test_showreport_tynull(self):
        '''type的值为空，举报失败'''
        token = Login().login()  # 引用登录
        params = 'type=&content=其他&showId=931'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': '', 'content': '123', 'showId': 931},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)


    def test_showreport_typanull(self):
        '''type的参数为空，举报失败'''
        token = Login().login()  # 引用登录
        params = '=15030&content=其他&showId=931'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': '15030', 'content': '123', 'showId': 931},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)


    def test_showreport_ctlose(self):
        '''类型为其他，content未传，举报失败'''
        token = Login().login()  # 引用登录
        params = 'type=15030&showId=861'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': '15030', 'showId': 861},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("内容不能为空", js['message'])



    def test_showreport_ctnull(self):
        '''类型为其他，content的值为空，举报失败'''
        token = Login().login()  # 引用登录
        params = 'type=15030&content=&showId=861'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': '15030', 'content': '', 'showId': 861},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("内容不能为空", js['message'])



    def test_showreport_ctpanull(self):
        '''类型为其他，content的参数为空，举报失败'''

        token = Login().login()  # 引用登录
        params = 'type=15030&=123&showId=861'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': '15030', '': '123', 'showId': 861},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("内容不能为空", js['message'])


    def test_showreport_tokennull(self):
        '''token不传'''
        params = 'type=15030&=123&showId=861'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,
                        # {'type': '15030', '': '123', 'showId': 861},

                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn("token无效", js['message'])



    def test_showreport_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        params = 'type=15030&=123&showId=861'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'type': '15030', '': '123', 'showId': 861},
                        token+'1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn("token无效", js['message'])


    def test_showreport_signerror(self):
        '''签名错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'type': 15000,'content': u'其他','showId':861}
        print params
        r = self.signerror('POST',
                        self.url_path,
                        params,
                        self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])

        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + "1",
        #                 'token': self.token
        #                 }
        # params = urllib.urlencode({'type': 15000,'content': u'其他','showId':861})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])

    def test_showreport_nonceerror(self):
        '''nonce错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'type': 15000,'content': u'其他','showId':861}
        print params
        r = self.noncerror('POST',
                        self.url_path,
                        params,
                        self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # self.headers = {'nonce': self.nonce + "1",
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature,
        #                 'token': self.token
        #                 }
        #
        # params = urllib.urlencode({'type': 15000,'content': u'其他','showId':861})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])





