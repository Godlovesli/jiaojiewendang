#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class draftListTest(MyTest):
    '''获取用户上传食谱草稿列表'''
    url_path =  '/v1/recipe/draftList'

    @classmethod
    def setUpClass(cls):
        pass


    def test_draftlist_success(self):
        '''获取用户上传食谱草稿列表'''
        token = Login().login()     #引用登录
        # token = 'ZDI5ZTcyNjUyZTFhMzdhNjVhZWQ0ODhlN2M5MjJhNDk='
        print token

        r = self.nocryp('GET',
                        self.url_path,
                        {'':''},
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn(u'获取用户草稿成功',js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']
            print js['result'][i]['id']



    def test_draftlist_tokennull(self):
        '''未传入token'''

        r = self.bujiami('GET',
                         self.url_path,
                         {'': ''},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn(u'token无效',js['message'])


    def test_draftlist_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        r = self.nocryp('GET',
                         self.url_path,
                         {'': ''},
                         token+'1')
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn(u'token无效',js['message'])




    def test_feedbacksubmit_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'': ''}
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


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'': ''})
        # request = urllib2.Request(self.url,data=params)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_feedbacksubmit_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'': ''}
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


        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'': ''})
        # request = urllib2.Request(self.url,data=params)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])