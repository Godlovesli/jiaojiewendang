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

class test_showcommentdelpostTest(MyTest):
    '''删除作品评论'''
    url_path = '/show/comment/del/post'

    @classmethod
    def setUpClass(cls):
        pass


    def test_showcommentdpost_zj(self):
        '''所有参数都传，删除自己的评论，删除成功'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show_comment where user_id='1053'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            commentId = rows['id']
            showId = rows['recipe_show_id']
            print showId
            params = 'showId='+str(showId)+'&commentId='+str(commentId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'showId': showId, 'commentId': commentId},
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('删除成功', js['message'])
        else:
            print "不存在评论"


    def test_test_showcommentdelpost_ysc(self):
        '''删除已删除的评论，提示已删除'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show_comment where user_id!='1053'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            commentId = rows['id']
            showId = rows['recipe_show_id']
            print showId
            params = 'showId=' + str(showId) + '&commentId=' + str(commentId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'showId': showId, 'commentId': commentId},
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], -1)
            self.assertIn('删除失败', js['message'])
        else:
            print "不存在评论"


    def test_showcommentdpost_sidlose(self):
        '''测试参数不完整，必填参数(showId)未传'''
        token = Login().login()  # 引用登录
        params = 'commentId=1021'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'commentId': '1021'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showcommentdpost_sidnull(self):
        '''必填字段(showid)的值为空'''
        token = Login().login()  # 引用登录
        params = 'showId=&commentId=1021'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': '', 'commentId': '1021'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showcommentdpost_sidpanull(self):
        '''必填参数(showid)为空'''
        token = Login().login()  # 引用登录
        params = '=907&commentId=1021'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': '907', 'commentId': '1021'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个作品", js['message'])


    def test_showcommentdpost_cidlose(self):
        '''测试参数不完整，必填参数(commentId)未传'''
        token = Login().login()  # 引用登录
        params = 'showId=907'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': '908'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个评论", js['message'])


    def test_showcommentdpost_cidnull(self):
        '''必填字段(commentId)的值为空'''
        params = 'showId=907&commentId='
        token = Login().login()  # 引用登录
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': '908', 'commentId': ''},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个评论", js['message'])


    def test_showcommentdpost_cidpanull(self):
        '''必填参数(commentId)为空'''
        token = Login().login()  # 引用登录
        params = 'showId=907&=1021'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': '907', '': '1021'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("请选择一个评论", js['message'])


    def test_showcommentdpost_tokenull(self):
        '''token不传'''
        params = 'showId=816&commentId=1021'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,
                        # {'showId': '816','commentId': '1021'},

                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_showcommentdpost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'showId=816&commentId=1021'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': '816','commentId': '1021'},
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_showdelpost_signerror(self):
        '''签名错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId':909,'commentId':'1020'}
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
        # params = urllib.urlencode({'showId':909,'commentId':'1020'})
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
        params ={'showId':909,'commentId':'1020'}
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
        # params = urllib.urlencode({'showId':909,'commentId':'1020'})
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
