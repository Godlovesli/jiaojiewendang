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

class V1searchappdatagetTest(MyTest):
    '''搜索/筛选接口'''
    url_path = '/v1/community/search/app/data/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_searchappdataget_success(self):
        '''传入所有参数'''
        params = 'content=藕&pageno=1&perpage=20'
        r = self.myhttp('GET',
                        self.url_path,
                         params
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']

    def test_searchappdataget_btsuccess(self):
        '''传入必填参数'''
        params = 'pageno=1&perpage=20'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_searchappdataget_nolose(self):
        '''必填参数pageno未传，默认显示第1页的数据'''
        params = 'perpage=20'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_searchappdataget_nonull(self):
        '''必填参数pageno的值为空，默认显示第1页的数据'''
        params = 'pageno=&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_searchappdataget_nopanull(self):
        '''必填参数pageno的参数为空，默认显示第1页的数据'''
        params = '=1&perpage=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_searchappdataget_gelose(self):
        '''必填参数perpage未传'''
        params = 'pageno=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 2)


    def test_searchappdataget_genull(self):
        '''必填参数perpage的值为空'''
        params = 'pageno=1&perpage='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 2)

    def test_searchappdataget_gepanull(self):
        '''必填参数perpage的参数为空'''
        params = 'pageno=1&=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 2)



    def test_searchappdataget_signerror(self):
        '''sign不正确'''
        params = {'pageno': '1','perpage':'5'}
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
        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = 'pageno=1&perpage=5'
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
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])

    def test_searchappdataget_noncerror(self):
        '''nonce不正确'''
        params = {'pageno': '1','perpage':'5'}
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
        # params = 'pageno=1&perpage=5'
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # self.headers = {'nonce': self.nonce + 'e',
        #                 'User-Agent': 'chunmiapp',
        #                 'signature': self.signature
        #                 }
        # request = urllib2.Request(url2, headers=self.headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


