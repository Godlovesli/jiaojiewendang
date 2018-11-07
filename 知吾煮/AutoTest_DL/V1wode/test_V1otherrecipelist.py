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


class v1otherrecipelistTest(MyTest):
    '''查看用户(非本人)发布的食谱列表'''
    url_path = '/v1/mine/other/people/recipe/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_otherrecipelist_success(self):
        '''所有参数都传'''
        token = Login().login()  # 引用登录
        params = 'customerid=1117&pageno=1&perpage=6'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取我发布的成功', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['contentId']
            print js['result'][i]['csrecipe']['recipeName']
            print js['result'][i]['csrecipe']['status']

    def test_otherrecipelist_success1(self):
        '''所有参数都不传'''
        token = Login().login()  # 引用登录
        params = 'customerid=1117'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取我发布的成功', js['message'])


    # def test_otherrecipelist_tokenull(self):
    #     '''未传入token'''
    #     token = Login().login()  # 引用登录
    #     params = 'customerid=1117'
    #     print params
    #     r = self.myhttp('GET',
    #                     self.url_path,
    #                     params
    #                     )
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['state'], -3)
    #     self.assertIn('token无效', js['message'])
    #
    #
    # def test_otherrecipelist_tokenerror(self):
    #     '''token错误'''
    #     token = Login().login()  # 引用登录
    #     params = 'customerid=1117'
    #     print params
    #     r = self.myhttp('GET',
    #                     self.url_path,
    #                     params,
    #                     token+'ert'
    #                     )
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['state'], -3)
    #     self.assertIn('token无效', js['message'])


    def test_otherrecipelist_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'customerid': '1117'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r


        # token = Login().login()
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = ''
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # request.add_header('token', token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_otherrecipelist_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'customerid': '1117'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r


        #
        # token = Login().login()
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = ''
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # request.add_header('token', token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
