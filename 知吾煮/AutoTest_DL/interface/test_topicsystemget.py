#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import random
import requests
import MySQLdb
import MultipartPostHandler
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class topicsystemgetTest(MyTest):
    '''系统默认的举报用语'''
    url_path = '/topic/report/system/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_topicsystemget_success(self):
        '''获取内容成功'''
        r = self.nosign('GET',
                        self.url_path,
                        {'':''},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取内容成功',js['message'])

