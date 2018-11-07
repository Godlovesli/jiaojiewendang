# coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.mydb import MyDB
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


class checknewTest(MyTest):
    '''检查更新'''
    url_path =  '/qiniu/getUpToken'

    @classmethod
    def setUpClass(cls):
        pass


    def test_getUpToken_success(self):
        '''获取成功'''
        params=''
        r = self.myhttp('GET',
                        self.url_path,
                        params

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取token成功', js['message'])


    def test_getUpToken_signerror(self):
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


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({})
        # print '输入参数：'+params
        # request = urllib2.Request(self.url + '?' + params)
        # request.add_header('nonce',self.nonce)
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature+'1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_getUpToken_noncerror(self):
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


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({})
        # print '输入参数：'+params
        # request = urllib2.Request(self.url + '?' + params)
        # request.add_header('nonce',self.nonce+'1')
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
