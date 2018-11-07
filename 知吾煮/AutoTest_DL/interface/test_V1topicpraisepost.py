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

class v1topicpraisepostTest(MyTest):
    '''主题点赞/取消点赞'''
    url_path = '/v1/topic/praise/post'

    @classmethod
    def setUpClass(cls):
        pass

    def test_praise_success(self):
        '''操作类型为：praise，点赞成功'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where id not in (select mipot_topic.id from mipot_topic,mipot_topic_praise \
               where mipot_topic.id=mipot_topic_praise.topic_id and \
              mipot_topic.is_deleted='0' and mipot_topic_praise.user_id='1081') and \
              is_deleted='0'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            topicId = rows['id']
            print topicId
            params = 'praise=praise&topicId=' + str(topicId)
            print params
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('点赞成功', js['message'])
        else:
            print "请先发表话题"

    def test_praise_cpsuccess(self):
        '''点赞后，操作类型为：cancelPraise，取消点赞成功'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select mipot_topic.id from mipot_topic,mipot_topic_praise  \
               where mipot_topic.id=mipot_topic_praise.topic_id  and  \
               mipot_topic.is_deleted='0' and mipot_topic_praise.user_id='1081' "
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            topicId = rows['id']
            print topicId
            params = 'praise=cancelPraise&topicId=' + str(topicId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('取消点赞成功', js['message'])
        else:
            print "请先点赞"

    def test_praise_weiz(self):
        '''未赞时，操作类型为：cancelPraise，还没有赞过'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where id not in (select mipot_topic.id from mipot_topic,mipot_topic_praise \
                where mipot_topic.id=mipot_topic_praise.topic_id and \
                mipot_topic.is_deleted='0' and mipot_topic_praise.user_id='1081') and \
                is_deleted='0'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            topicId = rows['id']
            print topicId
            params = 'praise=cancelPraise&topicId=' + str(topicId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], -1)
            self.assertIn('还没有赞过', js['message'])
        else:
            print "请先点赞"

    def test_praise_yz(self):
        '''点赞后，操作类型为：praise，提示已经点赞'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select mipot_topic.id from mipot_topic,mipot_topic_praise  \
                where mipot_topic.id=mipot_topic_praise.topic_id  and  \
                mipot_topic.is_deleted='0' and mipot_topic_praise.user_id='1081' "
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            topicId = rows['id']
            print topicId
            params = 'praise=praise&topicId=' + str(topicId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], -4)
            self.assertIn('已经点赞', js['message'])
        else:
            print "请先点赞"


    def test_praise_prlose(self):
        '''praise未传，点赞失败'''
        token = Login().login()  # 引用登录
        params = 'topicId=6'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required String parameter 'praise' is not present", js['message'])

    def test_praise_prnull(self):
        '''praise的值为空，点赞失败'''
        token = Login().login()  # 引用登录
        params = 'topicId=6&praise='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required String parameter 'praise' is not present", js['message'])

    def test_praise_prpanull(self):
        '''praise参数为空，点赞失败'''
        token = Login().login()  # 引用登录
        params = 'topicId=6&=praise'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required String parameter 'praise' is not present", js['message'])

    def test_praise_tplose(self):
        '''topicId未传，点赞失败'''
        token = Login().login()  # 引用登录
        params = 'praise=praise'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])

    def test_praise_tpnull(self):
        '''topicId的值为空，点赞失败'''
        token = Login().login()  # 引用登录
        params = 'praise=praise&topicId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])

    def test_praise_tppanull(self):
        '''topicId的参数为空，点赞失败'''
        token = Login().login()  # 引用登录
        params = 'praise=praise&=16'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])


    def test_praise_tokennull(self):
        '''未传入token'''
        params = 'praise=praise&topicId=16'
        r = self.myhttp1('POST',
                        self.url_path,
                        params,

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_praise_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'praise=praise&topicId=16'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token+ '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_praise_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'praise': 'praise', 'topicId': '16'}
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
        # params = 'praise=praise&topicId=16'
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
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_praise_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'praise': 'praise', 'topicId': '16'}
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
        # params = 'praise=praise&topicId=16'
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
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
        #







