#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
from base.mydb import MyDB
import requests
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class showdelpostTest(MyTest):
    '''删除作品'''
    url_path = '/show/del/post'

    @classmethod
    def setUpClass(cls):
        pass

    def test_showdelpost_success(self):
        '''删除自己发布的作品'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where user_id='1081'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            print showId
            params = 'showId='+str(showId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'showId':showId},
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('删除成功', js['message'])
        else:
            print "不存在作品"


    def test_showdelpost_br(self):
        '''删除别人的作品'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show where user_id!='1081'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            print showId
            params = 'showId=' + str(showId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'showId': showId},
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], -1)
            self.assertIn('没有权限删除此作品', js['message'])
        else:
            print "不存在作品"



    def test_showdelpost_IDlose(self):
        '''showId未传，删除失败'''
        token = Login().login()  # 引用登录
        params = ''
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': ''},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showdelpost_IDnull(self):
        '''必填字段(showid)的值为空'''
        token = Login().login()  # 引用登录
        params = 'showId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': ''},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showdelpost_IDpanull(self):
        '''必填参数(showid)为空'''
        token = Login().login()  # 引用登录
        params = '=784'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': '784'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showdelpost_tokennull(self):
        '''token不传'''
        params = 'showId=784'
        r = self.myhttp1('POST',
                         self.url_path,
                         params
                         # {'showId': '816'},

                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_showdelpost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'showId=784'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': '816'},
                        token+ '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_showdelpost_signerror(self):
        '''签名错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId': '818'}
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



        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + "1",
        #                 'token': self.token
        #                 }
        # params = urllib.urlencode({'showId':'913'})
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

    def test_showdelpost_noncerror(self):
        '''nonce错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId': '818'}
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
        # params = urllib.urlencode({'showId':'913'})
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
        #



