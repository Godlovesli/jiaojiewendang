#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
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


class reciperesumepointTest(MyTest):
    '''获取开盖步谱详情'''
    url_path =  '/recipe/resume/point'

    @classmethod
    def setUpClass(cls):
        pass


    def test_reciperesumepoint_success(self):
        '''获取开盖步骤详情'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from mipot_recipe A,mipot_recipe_step B where A.id = B.recipeId \
              and A.state='2200' and B.resumeIndex is NOT NULL"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        recipeId = rows['recipeId']
        resumeIndex = rows['resumeIndex']
        print recipeId
        params = 'recipeid='+str(recipeId)+'&stepIndex='+str(resumeIndex)
        r = self.myhttp('GET',
                        self.url_path,
                        params
                         # {'recipeid':recipeId, 'stepIndex':resumeIndex},

                        )
        print r
        js = json.loads(r)
        if data_count >0:
            self.assertEqual(js['state'], 1)
            self.assertIn('获取步骤信息成功', js['message'])

        else:
            print "不存在断点食谱"



    def test_reciperesumepoint_reIDno(self):
        '''食谱Id不存在'''
        params = 'recipeid=8497684976&stepIndex=1'
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         # {'recipeid': 8497684976, 'stepIndex': 1},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],0)
        self.assertIn('没有相关信息', js['message'])



    def test_reciperesumepoint_relose(self):
        '''测试参数不完整，必填参数(recipeId)未传'''
        params = 'stepIndex=1'
        r = self.myhttp('GET',
                         self.url_path,
                         params,
                         # {'stepIndex': 1},
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required long parameter 'recipeid' is not present", js['message'])


    def test_reciperesumepoint_renull(self):
        '''必填字段(recipeId)的值为空'''
        params = 'recipeid=&stepIndex=2'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'recipeid': '', 'stepIndex': '2'},
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required long parameter 'recipeid' is not present", js['message'])


    def test_reciperesumepoint_repanull(self):
        '''必填参数(recipeId)为空'''
        params = '=1497&stepIndex=2'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'': '1497', 'stepIndex': '2'},
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required long parameter 'recipeid' is not present", js['message'])



    def test_reciperesumepoint_stno(self):
        '''食谱stepIndex不存在'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from mipot_recipe A,mipot_recipe_step B where A.id = B.recipeId \
              and A.state='2200' and B.resumeIndex is NOT NULL"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        recipeId = rows['recipeId']
        print recipeId
        params = 'stepIndex=20&recipeid='+str(recipeId)
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         # {'recipeid':recipeId, 'stepIndex':20},

                        )
        print r
        js = json.loads(r)
        if data_count >0:
            self.assertEqual(js['state'], 0)
            self.assertIn('没有相关信息', js['message'])

        else:
            print "不存在断点食谱"



    def test_reciperesumepoint_stlose(self):
        '''测试参数不完整，必填参数(stepIndex)未传'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from mipot_recipe A,mipot_recipe_step B where A.id = B.recipeId \
              and A.state='2200' and B.resumeIndex is NOT NULL"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        recipeId = rows['recipeId']
        resumeIndex = rows['resumeIndex']
        print recipeId
        params = 'recipeid=' + str(recipeId)
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         # {'recipeid':recipeId},

                        )
        print r
        js = json.loads(r)
        if data_count >0:
            self.assertEqual(js['state'], 1)
            self.assertIn('获取步骤信息成功', js['message'])

        else:
            print "不存在断点食谱"


    def test_reciperesumepoint_stnull(self):
        '''必填字段(stepIndex)的值为空'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from mipot_recipe A,mipot_recipe_step B where A.id = B.recipeId \
              and A.state='2200' and B.resumeIndex is NOT NULL"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        recipeId = rows['recipeId']
        resumeIndex = rows['resumeIndex']
        print recipeId
        params = 'stepIndex=&recipeid=' + str(recipeId)
        r = self.myhttp('GET',
                        self.url_path,
                        params
                         # {'recipeid':recipeId, 'stepIndex':''},

                        )
        print r
        js = json.loads(r)
        if data_count >0:
            self.assertEqual(js['state'], 1)
            self.assertIn('获取步骤信息成功', js['message'])

        else:
            print "不存在断点食谱"


    def test_reciperesumepoint_stpanull(self):
        '''必填参数(stepIndex)为空'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT B.* from mipot_recipe A,mipot_recipe_step B where A.id = B.recipeId \
              and A.state='2200' and B.resumeIndex is NOT NULL"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        recipeId = rows['recipeId']
        resumeIndex = rows['resumeIndex']
        print recipeId
        params = 'recipeid=' + str(recipeId)+'&'+str(resumeIndex)
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         # {'recipeid':recipeId, '':resumeIndex},

                        )
        print r
        js = json.loads(r)
        if data_count >0:
            self.assertEqual(js['state'], 1)
            self.assertIn('获取步骤信息成功', js['message'])

        else:
            print "不存在断点食谱"



    def test_reciperesumepoint_signerror(self):
        '''sign不正确'''
        params = {'recipeid':356, 'stepIndex':1}
        r = self.signerror('GET',
                           self.url_path,
                           params,
                           # {'deviceid':'1128170','':'1558'}
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'recipeid':356, 'stepIndex':1})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature + 'e'
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn(u'拦截请求授权出错', js['message'])

    def test_reciperesumepoint_noncerror(self):
        '''nonce不正确'''
        params = {'recipeid':356, 'stepIndex':1}
        r = self.noncerror('GET',
                           self.url_path,
                           params,
                           # {'deviceid':'1128170','':'1558'}
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'recipeid':356, 'stepIndex':1})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce + 'e',
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn(u'拦截请求授权出错', js['message'])









