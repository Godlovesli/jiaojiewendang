#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class stepinfogetTest(MyTest):
    '''获取食谱所有步骤信息接口'''
    url_path = '/v1/recipe/resume/stepinfo/get'

    @classmethod
    def setUpClass(cls):
        pass


    def test_stepinfoget_success(self):
        '''获取食谱步骤成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT A.* from mipot_recipe A,mipot_recipe_step B where A.id = B.recipeId \
              and A.state='2200' and B.resumeIndex is NOT NULL"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        recipeid = rows['id']
        print recipeid
        if data_count>0:
            params = 'recipeid='+str(recipeid)
            r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'recipeid': recipeid}
                        )
            print r
            print '返回结果：'+ r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取食谱步骤成功',js['message'])
        else:
            print '不存在食谱'

    def test_stepinfoget_ideerror(self):
        '''recipeid的值格式不正确，为英文'''
        params = 'recipeid=one'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'recipeid': 'one'},
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('食谱id必须是纯数字', js['message'])

    def test_stepinfoget_idcerror(self):
        '''recipeid的值格式不正确，为中文'''
        params = 'recipeid=一'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'recipeid': '一'},
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('食谱id必须是纯数字', js['message'])

    def test_stepinfoget_idlose(self):
        '''测试参数不完整，必填参数(recipeid)未传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'': ''},
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('请填写食谱id', js['message'])


    def test_stepinfoget_idnull(self):
        '''必填字段(recipeid)的值为空'''
        params = 'recipeid='
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'recipeid': ''},
                        )
        print "返回结果："+r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('请填写食谱id', js['message'])


    def test_stepinfoget_idpanull(self):
        '''必填字段(recipeid)为空'''
        params = '=356'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'': '356'},
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn('请填写食谱id', js['message'])


    def test_stepinfoget_signerror(self):
        '''sign不正确'''
        params ={'recipeId': '668'}
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
        # params = urllib.urlencode({'recipeId': '668'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + 'ee')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_stepinfoget_noncerror(self):
        '''nonce错误'''
        params ={'recipeId': '668'}
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
        # params = urllib.urlencode({'recipeId': '668'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + 'EE')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    # def test_stepinfoget_sysuccess(self):
    #     '''传所有参数'''
    #     self.url = self.base_url + self.url_path
    #     self.signature = generateSignature(self.nonce, "GET", self.url)
    #     params = urllib.urlencode({'recipeId': 668})
    #     print '传入的参数:' + params
    #     encoded = encryptAES(params, self.key)
    #     datas = {'data': encoded}
    #     payload = urllib.urlencode(datas)
    #     url2 = self.url + '?' + payload
    #     request = urllib2.Request(url2)
    #     request.add_header('nonce', self.nonce)
    #     request.add_header('User-Agent', 'chunmiapp')
    #     request.add_header('signature', self.signature)
    #     response = urllib2.urlopen(request)
    #     result = response.read()
    #     print result
    #     r = decryptAES(result, self.key)
    #     print 'r:'+ r
    #     js = json.loads(r)
    #     print 'js:'+ js
    #     self.assertEqual(js['state'], 1)
    #     self.assertIn('获取食谱步骤成功', js['message'])
