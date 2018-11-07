#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
from poster.streaminghttp import register_openers
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class previewTest(MyTest):
    '''预览'''
    url_path =  '/recipe/preview'

    @classmethod
    def setUpClass(cls):
        pass


    def test_preview_success(self):
        '''所有参数都传入，预览成功'''
        self.url = self.base_url + '/recipe/preview'
        self.signature = generateSignature(self.nonce, 'POST', self.url)
        self.token = Login().login()     #引用登录
        # register_openers()
        post_data = {"name": "测试预览11",
                     "tagList": [317, 318],
                     "DeviceModelGroup":[1,3],
                     "ingredientList": [{"name": "牛肉", "quality": "一斤"}, {"name": "五花肉", "quality": "二斤"}],
                     "steps": [{"stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg", "description": "step1"},
                               {"stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg", "description": "step2"}],
                     "content": "content",
                     "iconPath": "/7b56873b8081406dbfe4da027c2c175c.jpg",
                     "peopleNum": 5,
                     "duration": 10,
                     "description": "description",
                     # "state": 2101,
                     "categoryId": 3}
        data_json = json.dumps(post_data)
        print data_json
        A = "json=" + data_json
        print A
        # A='json={"content": "content", "peopleNum": 5, "ingredientList": [{"quality": "\u4e00\u65a4", "name": "\u725b\u8089"}, {"quality": "\u4e8c\u65a4", "name": "\u4e94\u82b1\u8089"}], "steps": [{"stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg", "description": "step1"}, {"stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg", "description": "step2"}], "name": "\u6d4b\u8bd5\u9884\u89c8", "iconPath": "/7b56873b8081406dbfe4da027c2c175c.jpg", "duration": 10, "description": "description", "categoryId": 3, "tagList": [8225, 8226]}'
        encoded = encryptAES(A, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        print payload
        request = urllib2.Request(self.url, data=payload)
        request.add_header('nonce', self.nonce)
        request.add_header('signature', self.signature)
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('token', self.token)
        result = urllib2.urlopen(request).read()
        print result
        s = decryptAES(result, self.key)
        print s
        js = json.loads(s)
        self.assertEqual(js['state'], 1)
        self.assertEqual(js['message'], '预览成功')
        recipeid = js['result']
        return recipeid

    #
    # def test_preview_success1(self):
    #     r=self.test_preview_success()
    #     print r
