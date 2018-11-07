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

class sortpostTest(MyTest):
    '''排序（点击置顶时调用接口）'''
    url_path = '/v3/recipe/collect/sort/post'


    @classmethod
    def setUpClass(cls):
        pass

    def test_sortpost_success(self):
        '''操作成功'''
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


    def test_sortpost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        r = self.publish('POST',
                        self.url_path,
                        {
                            "recipeIds": ["275", "283"],
                            "deviceId": "994706",
                        },
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_sortpost_tokenull(self):
        '''未传入token'''
        r = self.publish('POST',
                        self.url_path,
                        {
                            "recipeIds": ["275", "283"],
                            "deviceId": "994706",
                        },

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_sortpost_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "POST", self.url)
        register_openers()
        post_data = {
            "recipeIds": ["275","283"],
            "deviceId": "994706",
            }
        data, headers = multipart_encode(post_data)
        request = urllib2.Request(self.url, data=data, headers=headers)
        request.add_header('nonce', self.nonce)
        request.add_header('signature', self.signature+'1')
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('token',self.token)
        result =urllib2.urlopen(request).read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


    def test_sortpost_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "POST", self.url)
        register_openers()
        post_data = {
            "recipeIds": ["275", "283"],
            "deviceId": "994706",
        }
        data, headers = multipart_encode(post_data)
        request = urllib2.Request(self.url, data=data, headers=headers)
        request.add_header('nonce', self.nonce+ '1')
        request.add_header('signature', self.signature )
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('token', self.token)
        result = urllib2.urlopen(request).read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])