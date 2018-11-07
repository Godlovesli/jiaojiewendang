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

class grouprecipedataTest(MyTest):
    '''食谱分组接口'''
    # url_path = '/v1/group/recipedata/get'
    url_path = '/v1/group/recipedata/potandinduction/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_grouprecipedata_success(self):
        '''传入所有参数'''
        params = 'groupId=2&pageno=1&perpage=200'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name'],js['result'][i]['source']

    def test_grouprecipedata_success1(self):
        '''传入所有参数'''
        params = 'groupId=1&pageno=1&perpage=200'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print  js['result'][i]['name']


    def test_grouprecipedata_Idlose(self):
        '''必填参数groupId未传'''
        params = 'pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('请选择一个分组',js['message'])

    def test_grouprecipedata_Idnull(self):
        '''必填参数groupId的值为空'''
        params = 'groupId=&pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('请选择一个分组',js['message'])

    def test_grouprecipedata_Idpanull(self):
        '''必填参数groupId的参数为空'''
        params = '=1&pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('请选择一个分组',js['message'])


    def test_grouprecipedata_nolose(self):
        '''必填参数pageno未传'''
        params = 'groupId=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_grouprecipedata_nonull(self):
        '''必填参数pageno的值为空'''
        params = 'groupId=1&pageno=&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

    def test_grouprecipedata_nopanull(self):
        '''必填参数pageno的参数为空'''
        params = 'groupId=1&=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_grouprecipedata_gelose(self):
        '''必填参数perpage未传'''
        params = 'groupId=1&pageno=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 3)

    def test_grouprecipedata_genull(self):
        '''必填参数perpage的值为空'''
        params = 'groupId=1&pageno=1&perpage='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 3)

    def test_grouprecipedata_gepanull(self):
        '''必填参数perpage的参数为空'''
        params = 'groupId=1&pageno=1&=5'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 3)


    def test_grouprecipedata_signerror(self):
        '''sign不正确'''
        params ={'groupId': '1', 'pageno': '1', 'perpage': '10'}
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
        # params = urllib.urlencode({'groupId': '1', 'pageno': '1', 'perpage': '10'})
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


    def test_grouprecipedata_noncerror(self):
        '''nonce不正确'''
        params ={'groupId': '1', 'pageno': '1', 'perpage': '10'}
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
        # params = urllib.urlencode({'groupId': '1', 'pageno': '1', 'perpage': '10'})
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



