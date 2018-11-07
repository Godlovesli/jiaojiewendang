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
from cjcryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ricecollectallTest(MyTest):
    '''获取专题'''
    url_path = '/v1/article/special/list'

    @classmethod
    def setUpClass(cls):
        pass


    def test_allfavricebydid_success(self):
        '''所有参数都传，获取成功'''
        params = 'pageno=1&perpage=10'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        # {'deviceid': '1128170','pageno ':'2','perpage':'2'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("专题数据获取成功", js['message'])
        print(len(js['result']))
        for i in range(len(js['result'])):
            print(js['result'][i]['id'])

