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

class recipeCommentaddTest(MyTest):
    '''评论\回复食谱评论'''
    url_path = '/v1/recipeComment/add'

    @classmethod
    def setUpClass(cls):
        pass

    # def test_recipeCommentadd_bt(self):
    #     '''只传必填参数，评论成功'''
    #     # token = Login().login()  # 引用登录
    #     # print token
    #     token='MzFjYTgwMTg5MjNlNjIwYjY2NjkxYTRlMzJkZmI1ZTc='
    #     r = self.myhttp('POST',#
    #                     self.url_path,
    #                     {'recipeId': 2008, 'content': u'特别好，已做'},
    #                      token
    #                      )
    #     print r
    #     js = json.loads(r)
    #     print js
    #     self.assertEqual(js['state'], 1)
    #     self.assertIn( '发表成功',js['message'])

    def test_recipeCommentadd_dc(self):
        '''只传必填参数，评论成功'''
        # token='ZDBiZWY0NWI3ZmQ0YmI0MzEwMGRiMjM3YmIwMjI1YWY='
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_recipe_comment where recipeId='256'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        ypcommentid = rows['id']
        print ypcommentid
        if data_count > 0:
            params = 'recipeId=256&content=棒=&parentId='+str(ypcommentid)
            r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'recipeId': 256, 'content': '棒','parentId':ypcommentid},
                         token
                         )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn( '发表成功',js['message'])
        else:
            r = self.myhttp('POST',
                            self.url_path,
                            {'recipeId': 256, 'content': '棒'},
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('发表成功', js['message'])

    def test_recipeCommentadd_idno(self):
        '''传入不存在的recipeId'''
        token = Login().login()  # 引用登录
        print token
        params={'recipeId': 256, 'content': '棒'}
        # params = 'recipeId=256&content=棒'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], 1)
        self.assertIn( '发表成功',js['message'])

    def test_recipeCommentadd_idlose(self):
        '''测试参数不完整，必填参数(recipeId)未传'''
        token = Login().login()  # 引用登录
        print token
        params = 'parentId=1882&content=棒&stars=4'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '发表评论发生错误',js['message'])

    def test_recipeCommentadd_idnull(self):
        '''必填字段(recipeId)的值为空'''
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId=&parentId=1882&content=棒&stars=4'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'recipeId': '', 'content': '123', 'parentId': '1882', 'stars': 4},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '发表评论发生错误',js['message'])


    def test_recipeCommentadd_idpanull(self):
        '''必填参数(recipeId)为空'''
        token = Login().login()  # 引用登录
        print token
        params = '=1661&parentId=1882&content=棒&stars=4'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': '1661', 'content': '123', 'parentId': '1882', 'stars': 4},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '发表评论发生错误',js['message'])


    def test_recipeCommentadd_ctlose(self):
        '''必填参数(content)未传'''
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId=256&stars=4'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'recipeId': '256', 'stars': 4},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( '发表成功',js['message'])

    def test_recipeCommentadd_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId=256&stars=4&content=123'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'recipeId': '256', 'content': '123','stars': 4},
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_recipeCommentadd_tokenull(self):
        '''未传入token'''
        params = 'recipeId=256&stars=4&content=123'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,
                        # {'recipeId': '256', 'content': '123', 'stars': 4},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_topiccommentdeletes_signerror(self):
        '''签名错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'recipeId': '256', 'content': '123', 'stars': 4}
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
        # params = urllib.urlencode({'recipeId': '256', 'content': '123', 'stars': 4})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_topiccommentdeletes_nonceerror(self):
        '''nonce错误'''
        # self.token = Login().login()  # 引用登录
        # print self.token
        # params ={'recipeId': '256', 'content': '123', 'stars': 4}
        # print params
        # r = self.noncerror('POST',
        #                 self.url_path,
        #                 params,
        #                 self.token
        #                    )
        # print r
        # js = json.loads(r)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])



        self.token = Login().login()  # 引用登录
        print self.token
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "POST", self.url)
        params = urllib.urlencode({'recipeId': '1661', 'content': '棒', 'stars': 4})
        encoded = encryptAES(params, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        request = urllib2.Request(self.url, data=payload)
        request.add_header('nonce', self.nonce)
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('signature', self.signature)
        request.add_header('token', self.token)
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'],-2)
        self.assertIn('拦截请求授权出错',js['message'])
