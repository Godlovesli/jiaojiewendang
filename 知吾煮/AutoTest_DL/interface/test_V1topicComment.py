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

class v1topiccommitCommentTest(MyTest):
    '''主题评论'''
    url_path = '/v1/topic/comment/commitComment'

    @classmethod
    def setUpClass(cls):
        pass


    def test_topiccomment_success(self):
        '''所有字段都传，评论成功'''

        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT A.* from  mipot_topic_comment A,mipot_topic B where A.is_deleted != 1 and B.is_deleted !=1 and A.topic_id =B.id"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            topicId = rows['topic_id']
            parentId = rows['id']
            print topicId
            print parentId
            params = 'content=test&topicId=' + str(topicId)+'&parentId='+str(parentId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('发表成功', js['message'])
        else:
            print "请先发表话题"


    def test_topiccomment_btsuccess(self):
        '''只传必填字段，评论成功'''

        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT A.* from  mipot_topic_comment A,mipot_topic B where A.is_deleted != 1 and B.is_deleted !=1 and A.topic_id =B.id "
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            topicId = rows['topic_id']
            print topicId
            params = 'content=test&topicId=' + str(topicId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('发表成功', js['message'])
        else:
            print "请先发表话题"

    def test_topiccomment_ctlose(self):
        '''content未传，举报失败'''
        token = Login().login()  # 引用登录
        params = 'topicId=6'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("回复失败", js['message'])


    def test_topiccomment_ctnull(self):
        '''content的值为空，评论失败'''
        token = Login().login()  # 引用登录
        params = 'content=&topicId=6'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("回复失败", js['message'])


    def test_topiccomment_ctpanull(self):
        ''' content参数为空，评论失败'''
        token = Login().login()  # 引用登录
        params = '=hao&topicId=6'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("回复失败", js['message'])


    def test_topiccomment_tplose(self):
        '''topicId未传，举报失败'''
        token = Login().login()  # 引用登录
        params = 'content=hao'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        # self.assertIn("may not be null", js['message'])


    def test_topiccomment_tpnull(self):
        '''topicId的值为空，评论失败'''
        token = Login().login()  # 引用登录
        params = 'content=hao&topicId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        # self.assertIn("may not be null", js['message'])


    def test_topiccomment_tppanull(self):
        '''topicId参数为空，评论失败'''
        token = Login().login()  # 引用登录
        params = 'content=hao&=6'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        # self.assertIn("may not be null", js['message'])


    def test_topiccomment_tokennull(self):
        '''未传入token'''
        params = 'content=hao&topicId=6'
        r = self.myhttp1('POST',
                        self.url_path,
                        params,

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_topiccomment_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'content=hao&topicId=6'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token+ '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_topiccomment_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'topicId':'6','content':'hao'}
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
        # params = 'content=hao&topicId=6'
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + 'e',
        #                 'token': self.token
        #                 }
        # request = urllib2.Request(self.url, data=payload, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_topiccomment_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'topicId':'6','content':'hao'}
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
        # params = 'content=hao&topicId=6'
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # self.headers = {'nonce': self.nonce+ 'e',
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature ,
        #                 'token': self.token
        #                 }
        # request = urllib2.Request(self.url, data=payload, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])







