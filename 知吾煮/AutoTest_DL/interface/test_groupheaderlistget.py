#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
import requests
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class showdetailTest(MyTest):
    '''筛选条件---食谱类型'''
    url_path =  '/group/header/list/get'

    @classmethod
    def setUpClass(cls):
        pass


    def test_showdetail_success(self):
        '''获取成功'''
        r = self.nosign('GET',
                         self.url_path,
                         {'': ''},
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('米饭', js['result'][0]['title'])
        self.assertIn('汤粥', js['result'][1]['title'])
        self.assertIn('菜品', js['result'][2]['title'])
        self.assertIn('点心', js['result'][3]['title'])




# class showdetail1Test(unittest.TestCase):
#     '''筛选条件---食谱类型'''
#
#     def setUp(self):
#
#         self.base_url = 'https://testapi2.coo-k.com'
#         self.url = self.base_url + '/group/header/list/get'
#         self.nonce = generateNonce()
#         self.signature = generateSignature(self.nonce, 'GET', self.url)
#         self.key = getSessionSecurity(self.nonce)
#         self.headers = {'User-Agent': 'chunmiapp'
#                         }
#
#
#     def tearDown(self):
#         pass
#
#
#     def test_showdetail_success(self):
#
#         request = urllib2.Request(self.url,  headers=self.headers)
#         response = urllib2.urlopen(request)
#         result = response.read()
#         print result
#         js=json.loads(result)
#         self.assertEqual(js['state'], 1)
#         self.assertIn('米饭', js['result'][0]['title'])
#         self.assertIn('汤粥', js['result'][1]['title'])
#         self.assertIn('菜品', js['result'][2]['title'])
#         self.assertIn('点心', js['result'][3]['title'])