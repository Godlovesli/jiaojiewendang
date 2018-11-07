#coding=utf-8
import json
import requests
import unittest
from cryp import *
from api_testdata import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MyTest(unittest.TestCase):

    def setUp(self):
        # self.base_url = 'http://10.0.10.100:17011'                  # 电磁炉插件测试环境
        # self.base_url='https://induction-hm-api.joyami.com'
        # self.base_url = 'https://inapi.coo-k.com'
        # self.base_url = 'https://inductionplugapi.joyami.com'       #电磁炉正式环境
        # self.base_url = 'https://pre-inductionplugapi.joyami.com'
        # self.base_url='https://inductionplugapi.joyami.com'
        self.base_url = 'https://sginductionplugapi.joyami.com'
        # self.base_url = 'https://ruinductionplugapi.joyami.com'
        # self.base_url = 'https://frainductionplugapi.joyami.com'
        # self.base_url = 'http://222.73.246.23:17023'  # 预法兰克服生产环境
        # self.base_url='http://222.73.246.25:8080'
        self.deviceId=deviceid
        self.model=model_name
        self.language=language_name




    def myhttp(self,method,url_path=None,params=None,token=None):
        url = self.base_url+url_path
        print url
        headers = {
        "Accept": "application/json;charset=UTF-8",
                   "token": token}
        try:
            if method == 'GET':
                r = requests.get(url, params=params, headers=headers,verify=False)
            if method == 'POST':
                r = requests.post(url, data=params, headers=headers,verify=False)
            result = r.text.encode()
            return result
        except Exception as e:
            print('%s' % e)
            return {}

    def cry_myhttp(self, method, url_path=None, params=None, token=None):
        # base_url = 'http://10.0.10.100:17011'
        # base_url = 'http://222.73.246.23:17023'  # 预法兰克服生产环境
        # base_url = 'https://inductionplugapi.joyami.com'
        base_url = 'https://sginductionplugapi.joyami.com'
        # base_url = 'https://frainductionplugapi.joyami.com'
        # base_url = 'https://ruinductionplugapi.joyami.com'
        url = base_url + url_path
        print url
        appid = "com.chunmi.ihcooker"
        signature = generateSignature(appid,method,url_path)
        print("sign",signature)
        headers = {"Accept": "application/json;charset=UTF-8",
                    "token": token,
                   "signature": signature}
        try:
            if method == 'GET':
                r = requests.get(url, params=params, headers=headers, verify=False)
            if method == 'POST':
                r = requests.post(url, data=params, headers=headers, verify=False)
            result = r.text.encode()
            return result
        except Exception as e:
            print('%s' % e)
            return {}




    def tearDown(self):
        pass