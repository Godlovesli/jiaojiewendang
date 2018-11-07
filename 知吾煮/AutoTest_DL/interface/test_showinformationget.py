#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
from base.mydb import MyDB
import unittest
import json
import MySQLdb
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class showinformationgetTest(MyTest):
    '''(APP接口)作品详情'''
    url_path = '/show/information/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_showinformationget_wpbr(self):
        '''不存在评论记录及未点赞，发布者查看详情：评论列表为空，"praised":false，"praiseCount":0'''
        # token='MWIyNWYyNTg2N2UyM2EwYmFlOTlmOWQxM2JiMjcyOGE='
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where praise_count =0 and user_id='1081'  \
               and id not in (select recipe_show_id from mipot_recipe_show_comment)"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            print showId
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                            self.url_path,
                            params,
                            # {'showId':showId},
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
            self.assertEqual(0, js['result'][0]['commentSize'])
            self.assertEqual(False, js['result'][0]['praised'])
            self.assertEqual(0, js['result'][0]['showing']['praiseCount'])

        else:
            print "不存在对应作品记录"


    def test_showinformationget_wptr(self):
        ''' 不存在评论记录及未点赞，其他人查看详情：评论列表为空，"praised":false，"praiseCount":0'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where praise_count =0 and user_id!='1081'  " \
              "and id not in (select recipe_show_id from mipot_recipe_show_comment) order by id DESC"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            print showId
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                             self.url_path,
                            params,
                             # {'showId': showId},
                             token
                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
            self.assertEqual(0, js['result'][0]['commentSize'])
            self.assertEqual(False, js['result'][0]['praised'])
            self.assertEqual(0, js['result'][0]['showing']['praiseCount'])

        else:
            print "不存在对应作品记录"


    def test_showinformationget_ypbr(self):
        ''' 存在评论记录，发布者查看详情，查看到评论列表'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where  praise_count =0 and  \
              user_id='1081' and id in (select recipe_show_id from mipot_recipe_show_comment)"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            print showId
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                             self.url_path,
                             params,
                             # {'showId': showId},
                             token
                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
            self.assertEqual(False, js['result'][0]['praised'])
            self.assertEqual(0, js['result'][0]['showing']['praiseCount'])
            self.assertIsNot(0, js['result'][0]['commentSize'])

        else:
            print "不存在对应作品记录"


    def test_showinformationget_ypplz(self):
        '''  存在评论记录，评论者查看，查看到评论列表'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where  id in (select recipe_show_id from mipot_recipe_show_comment where user_id='1081')"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            praisecount = rows['praise_count']
            print showId
            print praisecount
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                             self.url_path,
                             params,
                             # {'showId': showId},
                             token
                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
            self.assertEqual(js['state'], 1)
            self.assertEqual(praisecount, js['result'][0]['showing']['praiseCount'])
            self.assertIsNot(0, js['result'][0]['commentSize'])
        else:
            print "不存在对应作品记录"


    def test_showinformationget_yptr(self):
        '''存在评论记录，其他人查看，查看到评论列表'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where user_id!='1081' and  \
              id in (select recipe_show_id from mipot_recipe_show_comment where user_id!='1081')"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            print showId
            praisecount = rows['praise_count']
            print praisecount
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                             self.url_path,
                             params,
                             # {'showId': showId},
                             token
                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
            self.assertEqual(praisecount, js['result'][0]['showing']['praiseCount'])
            self.assertIsNot(0, js['result'][0]['commentSize'])
        else:
            print "不存在对应作品记录"


    def test_showinformationget_yzdzr(self):
        '''已被点赞，点赞用户查看，"praised":true'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where user_id!='1081' and " \
              "id in (select recipe_show_id from mipot_recipe_show_praise where user_id='1081')"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            praisecount = rows['praise_count']
            print showId
            print praisecount
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                             self.url_path,
                             params,
                             # {'showId': showId},
                             token
                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
            self.assertEqual(True, js['result'][0]['praised'])
            self.assertEqual(praisecount, js['result'][0]['showing']['praiseCount'])

        else:
            print "不存在对应作品记录"


    def test_showinformationget_yztr(self):
        '''已被点赞，非点赞用户查看，"praised":false'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where user_id!='1081' and  \
              id in (select recipe_show_id from mipot_recipe_show_praise where user_id!='1081')"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            praisecount = rows['praise_count']
            print showId
            print praisecount
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                             self.url_path,
                             params,
                             # {'showId': showId},
                             token
                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
            self.assertEqual(False, js['result'][0]['praised'])
            self.assertEqual(praisecount, js['result'][0]['showing']['praiseCount'])

        else:
            print "不存在对应作品记录"



    def test_showinformationget_tokenno(self):
        '''token不传'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where id in (select recipe_show_id from mipot_recipe_show_praise)"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            praisecount = rows['praise_count']
            print showId
            print praisecount
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                             self.url_path,
                            params,
                             # {'showId': showId},

                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
            self.assertEqual(False, js['result'][0]['praised'])
            self.assertEqual(praisecount, js['result'][0]['showing']['praiseCount'])

        else:
            print "不存在对应作品记录"


    def test_showinformationget_idlose(self):
        '''测试参数不完整，必填参数(showid)未传'''
        params = ''
        token = Login().login()  # 引用登录
        r = self.myhttp('GET',
                         self.url_path,
                         params,
                         # {'': ''},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showinformationget_idnull(self):
        '''必填字段(showid)的值为空'''
        token = Login().login()  # 引用登录
        params = 'showId='
        r = self.myhttp('GET',
                         self.url_path,
                         params,
                         # {'showId': ''},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showinformationget_idpanull(self):
        '''必填参数(showid)为空'''
        token = Login().login()  # 引用登录
        params = '=784'
        r = self.myhttp('GET',
                         self.url_path,
                         params,
                         # {'': '784'},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showinformationget_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId': 874}
        print params
        r = self.signerror('GET',
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
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'showId': 874})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + 'e',
        #                 'token': self.token
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_showinformationget_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId': 874}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])

        #
        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'showId': 874})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce+ 'e',
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature ,
        #                 'token': self.token
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
        #



