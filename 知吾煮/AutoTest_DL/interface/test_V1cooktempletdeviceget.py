#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
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


class cooktempletgetTest(MyTest):
    '''获取设备对应住的烹饪模板'''
    # url_path = '/v4/article/topadv'
    url_path = '/v1/recipe/cook/templet/device/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_cooktempletget_sysuccess(self):
        '''正确发送请求'''
        params = ''
        print params
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn("get recipecooktemplet success",js['message'])

    def test_cooktempletget_signerror(self):
        '''sign不正确'''
        params = {'': ''}
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
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_cooktempletget_noncerror(self):
        '''nonce不正确'''
        params = {'': ''}
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
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])