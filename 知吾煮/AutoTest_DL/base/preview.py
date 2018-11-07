#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
import unittest
import json
from login import Login
import urllib, urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Preview:
    '''预览'''

    def preview(self):
        '''所有参数都传入，预览成功'''
        self.token = Login().login()     #引用登录
        # self.base_url = 'https://testapi2.coo-k.com'
        # self.base_url = 'http://10.0.10.64:18080'
        self.base_url = 'http://10.0.10.100:17001'
        self.url = self.base_url + '/recipe/preview'
        self.nonce = generateNonce()
        self.signature = generateSignature(self.nonce, 'POST', self.url)
        self.headers = {'nonce': self.nonce,
                        'User-Agent': 'chunmiapp',
                        'signature': self.signature,
                        'token': self.token}
        self.key = getSessionSecurity(self.nonce)
        register_openers()
        post_data = {"name": "牛肉饭",
                     "tagList": [1, 2],
                     "ingredientList": [{"name": "牛肉", "quality": "一斤"}, {"name": "五花肉", "quality": "二斤"}],
                     "steps": [{"stepPic": "pic1", "description": "step1"},
                               {"stepPic": "pic2", "description": "step2"}],
                     "content": "content",
                     "iconPath": "recipe/9e07d2d3-f568-46c4-b4b1-333d4ead53fa.png",
                     "peopleNum": 5,
                     "duration": 10,
                     "description": "description",
                     # "state": 2101,
                     "categoryId": 3}
        data_json = json.dumps(post_data)
        A = "json=" + data_json
        encoded = encryptAES(A, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        request = urllib2.Request(self.url, data=payload)
        request.add_header('nonce', self.nonce)
        request.add_header('signature', self.signature)
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('token', self.token)
        result = urllib2.urlopen(request).read()
        s = decryptAES(result, self.key)
        print s
        js = json.loads(s)
        recipeid = js['result'][0]
        return recipeid

