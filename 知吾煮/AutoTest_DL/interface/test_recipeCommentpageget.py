#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
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

class recipeCommentpagegetTest(MyTest):
    '''食谱评论'''
    url_path = '/v1/recipeComment/page/get'


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeCommentpageget_dc(self):
        '''操作成功'''
        # token = Login().login()  # 引用登录
        # print token
        params = 'recipeId=256&pageno=1&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'recipeId': 2561, 'pageno': 1, 'perpage': 5},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)




    def test_recipeCommentpageget_bt(self):
        '''只传必填参数'''
        params = 'recipeId=2561'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_recipeCommentpageget_idno(self):
        '''传入不存在的recipeId，message（评论数）为0'''
        params = 'recipeId=2561'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertEqual('0', js['message'])

    def test_recipeCommentpageget_idlose(self):
        '''测试参数不完整，必填参数(recipeId)未传'''
        params = 'pageno=2&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('请选择食谱', js['message'])

    def test_recipeCommentpageget_idnull(self):
        '''必填字段(recipeId)的值为空'''
        params = 'recipeId=&pageno=2&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'recipeId': '', 'pageno': 2, 'perpage': 5},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('请选择食谱', js['message'])

    def test_recipeCommentpageget_idpanull(self):
        '''必填字段(recipeId)为空'''
        params = '=1661&pageno=2&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'': '1661', 'pageno': 2, 'perpage': 5},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('请选择食谱', js['message'])


    def test_recipeCommentpageget_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'recipeId': 1661,'pageno':2,'perpage':5}
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


        #
        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'recipeId': 1661,'pageno':2,'perpage':5})
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
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_recipeCommentpageget_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'recipeId': 1661,'pageno':2,'perpage':5}
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


        #
        # self.url=self.base_url+self.url_path
        # print self.url
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'recipeId': 1775,'pageno':2,'perpage':5})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce ,
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
