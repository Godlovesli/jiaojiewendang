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
            params = 'pageno=1&perpage=20&themeid='+str(themeid)
            # params = 'pageno=1&perpage=20&themeid=' + str(25)
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
        params = {'themeid':  '1'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        #
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'themeid=1'
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_topicthemelist_noncerror(self):
        '''nonce不正确'''
        params = {'themeid':  '1'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])

        #
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'themeid=1'
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
