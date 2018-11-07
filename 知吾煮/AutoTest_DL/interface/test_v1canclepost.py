#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
import requests
import unittest
import json
import time
import urllib, urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class canclepostTest(MyTest):
    '''删除收藏的食谱'''
    url_path = '/v1/recipe/collect/cancle/post'


    @classmethod
    def setUpClass(cls):
        pass

    def test_canclepost_success(self):
        '''删除成功'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                        self.url_path,
                         {
                             "recipeIds": ["275", "283"],
                             "deviceId": "994706",
                         },
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( '操作成功',js['message'])


    def test_canclepost_ridlose(self):
        '''必填字段recipeId未传'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                        self.url_path,
                         {

                             "deviceId": "994706",
                         },
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '需要选择一个食谱',js['message'])

    def test_canclepost_ridnull(self):
        '''必填字段recipeId的值为空'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                        self.url_path,
                         {
                             "recipeIds": '',
                             "deviceId": "994706",
                         },
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '需要选择一个食谱',js['message'])

    def test_canclepost_ridpanull(self):
        '''必填字段recipeId为空'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                        self.url_path,
                         {
                             "":  ["275", "283"],
                             "deviceId": "994706",
                         },
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '需要选择一个食谱',js['message'])


    def test_canclepost_didlose(self):
        '''必填字段deviceId未传'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                        self.url_path,
                         {
                             "recipeIds":  ["275", "283"],

                         },
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '需要选择一个设备',js['message'])

    def test_canclepost_didnull(self):
        '''必填字段deviceId的值为空'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                        self.url_path,
                         {
                             "recipeIds":  ["275", "283"],
                             "deviceId": ""
                         },
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '需要选择一个设备',js['message'])

    def test_canclepost_didpanull(self):
        '''必填字段deviceId为空'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                         self.url_path,
                         {
                             "recipeIds": ["275", "283"],
                             "": "994706"
                         },
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('需要选择一个设备', js['message'])

    def test_canclepost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                        self.url_path,
                        {
                            "recipeIds": ["275", "283"],
                            "": "994706"
                        },
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_canclepost_tokenull(self):
        '''未传入token'''
        r = self.publish('POST',
                        self.url_path,
                        {
                            "recipeIds": ["275", "283"],
                            "": "994706"
                        },

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_canclepost_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={
            "recipeIds": ["275","283"],
            "deviceId": "994706",
            }
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
        # register_openers()
        # post_data = {
        #     "recipeIds": ["275","283"],
        #     "deviceId": "994706",
        #     }
        # data, headers = multipart_encode(post_data)
        # request = urllib2.Request(self.url, data=data, headers=headers)
        # request.add_header('nonce', self.nonce)
        # request.add_header('signature', self.signature+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('token',self.token)
        # result =urllib2.urlopen(request).read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_canclepost_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={
            "recipeIds": ["275","283"],
            "deviceId": "994706",
            }
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
        # register_openers()
        # post_data = {
        #     "recipeIds": ["275", "283"],
        #     "deviceId": "994706",
        # }
        # data, headers = multipart_encode(post_data)
        # request = urllib2.Request(self.url, data=data, headers=headers)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('signature', self.signature)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('token', self.token)
        # result = urllib2.urlopen(request).read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
