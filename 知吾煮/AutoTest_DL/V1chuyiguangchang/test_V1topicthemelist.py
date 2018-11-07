#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v1topicthemelistTest(MyTest):
    '''获取话题中的主题列表'''
    url_path = '/v1/topic/theme/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_topicthemelist_success(self):
        '''所有参数都传'''
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_theme where deleted!='1'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            cursor.scroll(0)
            rows = cursor.fetchone()
            print rows
            themeid = rows['id']
            params = 'pageno=1&perpage=20&themeid='+str(95)
            # params = 'pageno=1&perpage=10&themeid=175'
            print params
            r = self.myhttp('GET',
                            self.url_path,
                             params
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取话题相关主题列表成功', js['message'])
            print "话题下的主题数量："+str(len(js['result']))
            print "话题参与人数：" + str(js['result'][0]["themes"][0]["participants"])
            for i in range(len(js['result'])):
                print js['result'][i]['content']

        else:
            print "不存在话题"



    def test_topicthemelist_btsuccess(self):
        '''只传必填参数'''

        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_theme where deleted!='1'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            cursor.scroll(0)
            rows = cursor.fetchone()
            print rows
            themeid = rows['id']
            params = 'themeid='+str(themeid)
            print params
            r = self.myhttp('GET',
                            self.url_path,
                             params
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取话题相关主题列表成功', js['message'])
            print len(js['result'])
            for i in range(len(js['result'])):
                print js['result'][i]['content']
        else:
            print "不存在话题"

    def test_topicthemelist_idlose(self):
        '''themeid未传，获取失败'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required long parameter 'themeid' is not present", js['message'])


    def test_topicthemelist_idnull(self):
        '''themeid的值为空，获取失败'''
        params = 'themeid='
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required long parameter 'themeid' is not present", js['message'])

    def test_topicthemelist_idpanull(self):
        '''themeid参数为空，获取失败'''
        params = '=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required long parameter 'themeid' is not present", js['message'])

    def test_topicthemelist_signerror(self):
        '''sign不正确'''
        params = {'themeid':'6'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params
                        )
        print r


    def test_topicthemelist_noncerror(self):
        '''nonce不正确'''
        params = {'themeid':'6'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                            params
                        )
        print r



