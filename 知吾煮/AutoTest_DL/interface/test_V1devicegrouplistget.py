#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
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

class V1devicegrouplistTest(MyTest):
    '''筛选条件---支持的设备类型'''
    # url_path =  '/v1/devicegroup/list/get'
    url_path = '/v1/devicegroup/list/getpotandinduction'

    @classmethod
    def setUpClass(cls):
        pass


    def test_devicegroup_success(self):
        '''获取食谱信息成功'''
        token = Login().login()  # 引用登录
        params = ''
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                        token
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('米家压力IH电饭煲', js['result'][0]['description'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']


