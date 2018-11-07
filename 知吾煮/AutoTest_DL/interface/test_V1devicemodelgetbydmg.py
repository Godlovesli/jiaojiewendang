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


class devicemodelgetbydmgTest(MyTest):
    '''根据设备分组ID获取设备分组所有设备model'''
    url_path = '/v1/devicemodel/list/getbydmg'

    @classmethod
    def setUpClass(cls):
        pass

    def test_getbydmg_sysuccess(self):
        '''所有参数都填'''
        params = {'dmgid':1}
        print params
        r = self.nosign('GET',
                         self.url_path,
                         params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn("根据分组ID获取所有设备型号信息成功",js['message'])

    def test_getbydmg_didnull(self):
        '''deviceid的值为空'''
        params = {'dmgid': ''}
        # params = 'deviceid='
        print params
        r = self.nosign('GET',
                         self.url_path,
                         params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn("根据分组ID获取所有设备型号信息成功",js['message'])



