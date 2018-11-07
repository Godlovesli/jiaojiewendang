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
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class V1topicdpostTest(MyTest):
    '''删除主题'''
    url_path = '/v1/topic/delete/post'

    @classmethod
    def setUpClass(cls):
        pass

    def test_topicdpost_success(self):
        '''删除自己的主题，删除成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id='1081' and is_deleted ='0' order by id desc"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'topicId=' + str(id)
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('删除成功',js['message'])


    def test_topicdpost_br(self):
        '''删除别人的主题，删除失败'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_topic where user_id!='1081'and is_deleted ='0'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'topicId=' + str(id)
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('删除话题失败',js['message'])

    def test_topicdpost_bcz(self):
        '''删除不存在的主题，删除失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'topicId=992018273742455'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('删除话题失败',js['message'])


    def test_topicdpost_IDlose(self):
        '''主题ID未传，删除失败'''
        token = Login().login()  # 引用登录
        print token
        params = ''
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('删除话题失败', js['message'])


    def test_topicdpost_IDpanull(self):
        '''主题ID的参数为空，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = '=80'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('删除话题失败', js['message'])


    def test_topicdpost_IDnull(self):
        '''主题ID的值为空，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'topicId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('删除话题失败', js['message'])


    def test_topicdpost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'topicId=80'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token+'ee'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],  -3)
        self.assertIn('token无效', js['message'])

    def test_topicdpost_tokenull(self):
        '''未传入token'''
        params = 'topicId=80'
        r = self.myhttp1('POST',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_topicdpost_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'topicId':'16'}
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
        # params = 'topicId=80'
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
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


    def test_topicdpost_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'topicId':'16'}
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
        # params = 'topicId=80'
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
