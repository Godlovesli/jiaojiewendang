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


class showallTest(MyTest):
    '''作品照片墙'''
    url_path = '/show/all'

    @classmethod
    def setUpClass(cls):
        pass


    def test_showall_success(self):
        '''获取成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            recipeId = rows['recipe_id']
            params = 'curPage=1&limit=5&recipeId='+str(recipeId)
            r = self.myhttp('GET',
                            self.url_path,
                            params,
                            # {'recipeId': recipeId, 'curPage': '1', 'limit': '5'},

                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
        else:
            print "未找到作品"



    def test_showall_btsuccess(self):
        '''必填字段传入正确，获取成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            recipeId = rows['recipe_id']
            params = 'curPage=1&recipeId=' + str(recipeId)
            r = self.myhttp('GET',
                            self.url_path,
                            params,
                            # {'recipeId': recipeId, 'curPage': '1'},

                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('获取成功', js['message'])
        else:
            print "未找到作品"


    def test_showall_relose(self):
        '''测试参数不完整，必填参数(recipeId)未传'''
        params = 'curPage=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'curPage': '1'},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'recipeId' is not present", js['message'])



    def test_showall_renull(self):
        '''必填参数(recipeId)的值为空'''
        params = 'recipeId=&curPage=1'
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         # {'recipeId': '', 'curPage': '1'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'recipeId' is not present", js['message'])


    def test_showall_repanull(self):
        '''必填参数(recipeId)为空'''
        params = '=256&curPage=1'
        r = self.myhttp('GET',
                         self.url_path,
                         params,
                         # {'': '256', 'curPage': '1'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'recipeId' is not present", js['message'])

    def test_showall_culose(self):
        '''测试参数不完整，必填参数(curPage)未传'''
        params = 'recipeId=256&curPage=1'
        r = self.myhttp('GET',
                         self.url_path,
                         params,
                         # {'recipeId': '256','curPage': '1'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])


    def test_showall_cunull(self):
        '''必填参数(curPage)的值为空'''
        params = 'recipeId=256&curPage=1'
        r = self.myhttp('GET',
                         self.url_path,
                         params,
                         # {'recipeId': '256', 'curPage': ''},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])


    def test_showall_cupanull(self):
        '''必填参数(curPage)为空'''
        params = 'recipeId=256&=1'
        r = self.myhttp('GET',
                         self.url_path,
                         params,
                         # {'recipeId': '256', '': '1'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功', js['message'])


    def test_showall_signerror(self):
        '''sign不正确'''
        params = {'recipeId':'256','curPage':'1','limit':'2'}
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
        # params = urllib.urlencode({'recipeId':'256','curPage':'1','limit':'2'})
        # print '传入的参数:'+ params
        # URL = self.url + '?' + params
        # request = urllib2.Request(URL)
        # request.add_header('nonce',self.nonce)
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature+'e')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_showall_noncerror(self):
        '''nonce不正确'''
        params = {'recipeId':'256','curPage':'1','limit':'2'}
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
        # params = urllib.urlencode({'recipeId':'256','curPage':'1','limit':'2'})
        # print '传入的参数:'+ params
        # URL = self.url + '?' + params
        # request = urllib2.Request(URL)
        # request.add_header('nonce',self.nonce+'e')
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])







