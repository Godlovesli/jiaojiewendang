#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import requests
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipetaggetTest(MyTest):
    '''获取标签'''
    url_path =  '/v1/recipe/tag/get'

    @classmethod
    def setUpClass(cls):
        pass


    def test_recipetagget_success(self):
        '''获取食谱信息成功'''
        params={'recipeId':3336}
        url = self.base_url + self.url_path
        signature = generateSignature(self.nonce, "GET", url)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': signature
                   }
        payload1 = urllib.urlencode(params)
        # encoded = encryptAES(payload1, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        r = requests.get(url, params=payload1, headers=headers, verify=False)
        result = r.text.encode()
        print result
        js = json.loads(result)
        # self.assertEqual(js['state'], 1)
        # self.assertIn(u'获取成功', js['message'])
        for i in range(len(js)):
            print js[i]['state']['name']




