#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
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

class recipeCommentdelpostTest(MyTest):
    '''删除评论'''
    url_path = '/recipeComment/del/post'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeCommentdelpost_zj(self):
        '''所有参数都传，删除自己的评论，删除成功'''

        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select A.* from mipot_recipe_comment A,mipot_recipe B where A.userid ='1081' and B.state='2200' and A.recipeId=B.id"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            ypcommentid = rows['id']
            print ypcommentid
            params = 'commentId=' + str(ypcommentid)
            r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'commentId': ypcommentid},
                         token
                         )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn( '删除成功',js['message'])
        else:
            print '删除失败 : 该评论已经被删除'


    def test_recipeCommentdelpost_br(self):
        '''所有参数都传，删除别人的评论，删除失败'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select A.* from mipot_recipe_comment A,mipot_recipe B where A.userid !='1081' and B.state='2200' and A.recipeId=B.id"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            cursor.scroll(0)
            rows = cursor.fetchone()
            print rows
            ypcommentid = rows['id']
            print ypcommentid
            params = 'commentId=' + str(ypcommentid)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'commentId': ypcommentid},
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], -1)
            self.assertIn('删除失败 : 您没有权限删除此评论', js['message'])
        else:
            print '删除失败 : 该评论已经被删除'


    def test_recipeCommentdelpost_ysc(self):
        '''删除已删除的评论，提示已删除'''
        token = Login().login()  # 引用登录
        params = 'commentId=1231220161250'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'commentId': '1231220161250'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('删除失败 : 该评论已经被删除', js['message'])


    def test_recipeCommentdelpost_idlose(self):
        '''测试参数不完整，必填参数(commentId)未传'''
        token = Login().login()  # 引用登录
        params = ''
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'commentId' is not present", js['message'])

    def test_recipeCommentdelpost_idnull(self):
        '''必填字段(commentId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'commentId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'commentId' is not present", js['message'])

    def test_recipeCommentdelpost_idpanull(self):
        '''必填参数(commentId)为空'''
        token = Login().login()  # 引用登录
        params = '=902'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'commentId' is not present", js['message'])


    def test_recipeCommentdelpost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'commentId=902'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_recipeCommentdelpost_tokenull(self):
        '''未传入token'''
        params = 'commentId=902'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_recipeCommentdelpost_signerror(self):
        '''签名错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'commentId': '902'}
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
        # params = urllib.urlencode({'commentId': '1'})
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

    def test_recipeCommentdelpost_noncerror(self):
        '''nonce错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'commentId': '902'}
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
        # params = urllib.urlencode({'commentId': '902'})
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