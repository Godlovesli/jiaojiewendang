#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 09:20
# @Author  : fengguifang
# @File    : base.py
# @Software: PyCharm

import requests
from base.cry import *
from cryptutil import md5
import unittest
import json
import sys


class MyTest(unittest.TestCase):

    def setUp(self):
        self.base_url ='http://120.92.219.37:8704'
        self.base_url='http://120.92.219.37:8715'
        # self.base_url = 'http://10.0.30.239:8704'
        self.app_id = 'com.chunmi.tokit'



    def myhttp(self,method, selfurl,payload=None,sign=None,token=None):
        url = self.base_url + selfurl
        print(url)
        signature = generateSignature(self.app_id,method, selfurl)
        print (signature)

        if sign:
            headers = {'Content-Type': 'application/json',
                       'token':token,
                       'signature': signature}
        else:
            headers = {'Content-Type': 'application/json',
                       'token':token}
        if method == 'GET':
            r = requests.get(url, data=payload, headers=headers)
        if method == 'POST':
            r = requests.post(url, data=payload, headers=headers)
        result = r.text
        return result

    def tearDown(self):
        pass

