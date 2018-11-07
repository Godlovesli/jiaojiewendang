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

class topiccommentdeleteTest(MyTest):
    '''删除话题评论'''
    url_path = '/topic/comment/del/post'

    @classmethod
    def setUpClass(cls):
        pass

    def test_topiccommentdeletes_success(self):
        '''删除自己的话题评论成功，用户1053'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from  mipot_topic A,mipot_topic_comment B where \
              A.id=B.topic_id and A.is_deleted !=1 and B.user_id='1053' and B.is_deleted != 1"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            commentId = rows['id']
            print commentId
            params = 'commentId='+str(commentId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'commentId': commentId},
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('删除成功', js['message'])
        else:
            print "请先发表评论"


    def test_topiccommentdeletes_plys(self):
        '''评论已经被删除，用户1053'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from  mipot_topic A,mipot_topic_comment B where \
              A.id=B.topic_id and A.is_deleted !=1 and B.user_id='1053' and B.is_deleted = 1"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            commentId = rows['id']
            print commentId
            params = 'commentId=' + str(commentId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'commentId': commentId},
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('该评论已经被删除', js['message'])
        else:
            print "您不存在已经删除的话题评论"


    def test_topiccommentdeletes_htys(self):
        '''话题已经被发布者删除，用户1053'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from  mipot_topic A,mipot_topic_comment B \
               where A.id=B.topic_id and A.is_deleted =1 and B.user_id='1053' and B.is_deleted != 1"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            commentId = rows['id']
            print commentId
            params = 'commentId=' + str(commentId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'commentId': commentId},
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], -1)
            self.assertIn('该评论已经被删除', js['message'])
        else:
            print "话题已被删除"

    def test_topiccommentdeletes_other(self):
        '''删除别人的话题评论'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from  mipot_topic A,mipot_topic_comment B where  \
              A.id=B.topic_id and A.is_deleted !=1 and B.user_id!='1053' and B.is_deleted != 1"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            commentId = rows['id']
            print commentId
            params = 'commentId=' + str(commentId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'commentId': commentId},
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], -1)
            self.assertIn('没有权限删除此评论', js['message'])
        else:
            print "不存在他人的评论"


    def test_topiccommentdeletes_idlose(self):
        '''commentId未传'''
        token = Login().login()  # 引用登录
        params = ''
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': ""},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'commentId' is not present", js['message'])


    def test_topiccommentdeletes_idnull(self):
        '''commentId的值为空'''
        token = Login().login()  # 引用登录
        params = 'commentId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'commentId': ""},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'commentId' is not present", js['message'])


    def test_topiccommentdeletes_idpanull(self):
        '''commentId的字段为空，删除失败'''
        token = Login().login()  # 引用登录
        params = '=488'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': "488"},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'commentId' is not present", js['message'])


    def test_praise_tokennull(self):
        '''未传入token'''
        params = 'commentId=13'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,
                        # {'commentId': 13},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_praise_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'commentId=13'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'commentId': 13},
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_topiccommentdeletes_signerror(self):
        '''签名错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'commentId': 13}
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
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + "1",
        #                 'token': self.token
        #                 }
        #
        # params = urllib.urlencode({'commentId': 13})
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

    def test_topiccommentdeletes_nonceerror(self):
        '''nonce错误'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'commentId': 13}
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



        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # self.headers = {'nonce': self.nonce+"1",
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature ,
        #                 'token': self.token
        #                 }
        #
        # params = urllib.urlencode({'commentId': 13})
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





