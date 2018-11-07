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


class Reviewandgenerate:
    '''运行烹饪程序'''

    def reviewandgenerate(self):
        '''所有参数都传入，预览成功'''
        self.token = Login().login()     #引用登录
        self.base_url = 'https://cinapi.joyami.com/'
        # self.base_url = 'http://10.0.10.100:17002'
        self.url = self.base_url + '/v1/recipe/reviewandgenerate'
        self.nonce = generateNonce()
        self.signature = generateSignature(self.nonce, 'POST', self.url)
        self.headers = {'nonce': self.nonce,
                        'User-Agent': 'chunmiapp',
                        'signature': self.signature,
                        'token': self.token}
        self.key = getSessionSecurity(self.nonce)
        register_openers()
        post_data = {"id":"",
	                "name":"运行烹饪程序",
	                "deviceid":"1083258",
	                "templetid":"19",
	                "tagList":[319,267,266,257,164],
	                "auxiliaryList":[{"name":"Q","quality":"1"},{"name":"W","quality":"2"}],
	                "ingredientList":[{"name":"E","quality":"2"},{"name":"R","quality":""},{"name":"","quality":"4"}],
	                "steps":[{"stepPic":"1498529207/4986F036-0F1E-4C62-8CE7-2DFD2B87FC28-960F91E6-0AC3-4B62-A750-5113C58DF9FD.jpg","description":"1","resumeIndex": 5,"resumeTime": 6,"resumeType": 18020},
	                        {"stepPic":"","description":"2"},{"stepPic":"","description":"3"},
	                        {"stepPic":"1498529232/4986F036-0F1E-4C62-8CE7-2DFD2B87FC28-44D5C93F-0652-481B-8A5E-B974D0AA4E87.jpg","description":"4"}],
	                "content":"",
	                "iconPath":"1498529157/4986F036-0F1E-4C62-8CE7-2DFD2B87FC28-8FABB4F3-FADA-4B62-82CA-DE409E0389B1.jpg",
	                "peopleNum":"2",
	                # "duration":"",
	                "description":"Hah ",
	                "deviceModelGroupList":[],
	                "riceId":"1",
	                "hardness":"50"}
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
        recipeid = js['result'][0]['id']
        return recipeid

