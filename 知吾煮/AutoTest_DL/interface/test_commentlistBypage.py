#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import random
import requests
import MySQLdb
import MultipartPostHandler
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class commentlistBypageTest(MyTest):
    '''查询话题的评论列表'''
    url_path = '/v1/topic/comment/listBypage'

    @classmethod
    def setUpClass(cls):
        pass

    def test_commentlistBypage_success(self):
        '''获取成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from  mipot_topic where commentCount > 0 and is_deleted != 1 order by publish_time DESC "
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'pageno=1&perpage=10&topicId='+str(id)
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'topicId': id, 'pageno': '1', 'perpage': '10'},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])

    def test_commentlistBypage_palose(self):
        '''pageno未传，获取失败'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from  mipot_topic where commentCount > 0 and is_deleted != 1 order by publish_time DESC"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'perpage=10&topicId=' + str(id)
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])

    def test_commentlistBypage_pelose(self):
        '''perpage未传，获取失败'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from  mipot_topic where commentCount > 0 and is_deleted != 1 order by publish_time DESC"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'pageno=1&topicId=' + str(id)
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])


    def test_commentlistBypage_idlose(self):
        '''topicId未传，获取失败'''
        params = 'pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])


    def test_commentlistBypage_idpanull(self):
        '''topicId的参数为空，获取失败'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from  mipot_topic where is_deleted != '1' and praiseCount > '0' "
        data_count = cursor.execute(sql)
        print data_count

        rows = cursor.fetchone()
        print rows
        id = rows['id']
        print id
        params = 'pageno=1&perpage=10&='+str(id)
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])


    def test_commentlistBypage_idnull(self):
        '''topicId的值为空，获取失败'''
        params = 'pageno=1&perpage=10&topicId='
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'topicId' is not present", js['message'])


    def test_commentlistBypage_signerror(self):
        '''sign不正确'''

        params = {'topicId':'23','pageno': '1', 'perpage': '6'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params

                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'topicId':'23','pageno': '1', 'perpage': '6'})
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_commentlistBypage_noncerror(self):
        '''nonce不正确'''
        params = {'topicId':'23','pageno': '1', 'perpage': '6'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params

                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'topicId':'23','pageno': '2', 'perpage': '6'})
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
        #
        #
        #
        #





