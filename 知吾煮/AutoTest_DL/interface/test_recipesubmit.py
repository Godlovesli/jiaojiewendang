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


class recipesubmitTest(MyTest):
    '''提交'''
    url_path =  '/recipe/submit'

    @classmethod
    def setUpClass(cls):
        pass


    def test_recipesubmit_success(self):
        '''所有参数都传入，提交成功'''
        self.url = self.base_url +self.url_path
        self.signature = generateSignature(self.nonce, 'POST', self.url)
        self.token = Login().login()     #引用登录
        print self.token
        register_openers()
        post_data ={"name": "测试发布食谱",
                     "tagList": [317, 318],
                     "DeviceModelGroup":[1,3],
                     "ingredientList": [{"name": "牛肉", "quality": "一斤"}, {"name": "五花肉", "quality": "二斤"}],
                     "steps": [{"stepPic": "pic1", "description": "step1"}, {"stepPic": "pic2", "description": "step2"}],
                     "content": "content",
                     "iconPath": "iconPath",
                     "peopleNum": 5,
                     "duration": 10,
                     "description": "description",
                     "state": 2100,
                     "categoryId": 3}
        print post_data
        data_json = json.dumps(post_data)
        print data_json
        A = "json="+data_json
        print A
        encoded = encryptAES(A, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        print data
        print payload
        request = urllib2.Request(self.url, data=payload)
        request.add_header('nonce', self.nonce)
        request.add_header('signature', self.signature)
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('token',self.token)
        result =urllib2.urlopen(request).read()
        print result
        s = decryptAES(result, self.key)
        print s
        js = json.loads(s)
        self.assertEqual(js['state'] , 1)
        self.assertEqual(js['message'] , '提交成功，正在审核')
        recipeid=js['result']
        print recipeid




    # def test_preview_ss(self):
    #     '''所有参数都传入，预览成功'''
    #     data1 = urllib.urlencode({"name": "牛肉饭",
    #                  "tagList": [1, 2],
    #                  "ingredientList": [{"name": "牛肉", "quality": "一斤"}, {"name": "五花肉", "quality": "二斤"}],
    #                  "steps": [{"stepPic": "pic1", "description": "step1"}, {"stepPic": "pic2", "description": "step2"}],
    #                  "content": "content", "iconPath": "iconPath", "peopleNum": 5, "duration": 10, "description": "description",
    #                  "state": 2101,
    #                  "categoryId": 3})
    #
    #     print data1
    #     A = "json=" + str(data1)
    #     print A
    #     encoded = encryptAES(A, self.key)
    #     data = {'data': encoded}
    #     payload = urllib.urlencode(data)
    #     print data
    #     print payload
    #     request = urllib2.Request(self.url, data=payload)
    #     request.add_header('nonce', self.nonce)
    #     request.add_header('User-Agent', 'chunmiapp')
    #     request.add_header('signature', self.signature)
    #     request.add_header('Content-Type', 'application/json')
    #     request.add_header('token', self.token)
    #     response = urllib2.urlopen(request)
    #     result = response.read()
    #     print result
    #     s = decryptAES(result, self.key)
    #     print s
    #
    #
    #
    #
    # def test_preview_success(self):
    #     '''所有参数都传入，预览成功'''
    #     data = urllib.urlencode( {'name':u'牛肉饭',
    #             'tagList':'[1, 2]',
    #             'ingredientList':[{'name': u'牛肉', 'quality': u'一斤'}, {'name': u'米', 'quality':u'二斤'}],
    #             'steps': [{'stepPic': 'pic1', 'description': 'step1'}, {'stepPic': 'pic2', 'description': 'step2'}],
    #             'content':'content',
    #             'iconPath':'iconPath',
    #             'peopleNum':'5',
    #             'duration':'10',
    #             'description':'description',
    #             'state':'2101',
    #             'categoryId':'3'})
    #     print data
    #     datas = urllib.urlencode({'json': data})
    #     data_json = json.dumps(data)
    #     encoded = encryptAES(data_json, self.key)
    #     data = {'data': encoded}
    #     payload = urllib.urlencode(data)
    #     print datas
    #     print data_json
    #     request = urllib2.Request(self.url, data=payload)
    #     request.add_header('nonce', self.nonce)
    #     request.add_header('User-Agent', 'chunmiapp')
    #     request.add_header('signature', self.signature)
    #     request.add_header('Content-Type', 'application/json')
    #     request.add_header('token', self.token)
    #     response = urllib2.urlopen(request)
    #     result = response.read()
    #     print result
    #     s = decryptAES(result, self.key)
    #     print s
    #
    #     params = urllib.urlencode({'json': '256'})
    #     encoded = encryptAES(params, self.key)
    #     data = {'data': encoded}
    #     payload = urllib.urlencode(data)
    #
    #     {"name": "牛肉饭", "tagList": [1, 2],
    #      "ingredientList": [{"name": "牛肉", "quality": "一斤"}, {"name": "五花肉", "quality": "二斤"}],
    #      "steps": [{"stepPic": "pic1", "description": "step1"}, {"stepPic": "pic2", "description": "step2"}],
    #      "content": "content", "iconPath": "iconPath", "peopleNum": 5, "duration": 10, "description": "description",
    #      "state": 2101, "categoryId": 3}
    #
    # def test_preview_success1(self):
    #     '''所有参数都传入，预览成功'''
    #     payload1 = {'name': u'牛肉饭',
    #                         'tagList': '[1, 2]',
    #                         'ingredientList': [{'name': u'牛肉', 'quality': u'一斤'}, {'name': u'米', 'quality': u'二斤'}],
    #                         'steps': [{'stepPic': 'pic1', 'description': 'step1'},
    #                                   {'stepPic': 'pic2', 'description': 'step2'}],
    #                         'content': 'content',
    #                         'iconPath': 'iconPath',
    #                         'peopleNum': '5',
    #                         'duration': '10',
    #                         'description': 'description',
    #                         'state': '2101',
    #                         'categoryId': '3'}
    #     payload ={'json':payload1}
    #     jdata = json.dumps(payload)
    #     print '传的参数：' + jdata
    #     self.headers = {'nonce': self.nonce,
    #                     'User-Agent': 'chunmiapp',
    #                     'signature': self.signature,
    #                     'token': self.token,
    #                     'Content-Type': 'application/json'}
    #     r = requests.post(self.url, data=jdata, headers=self.headers)
    #     result = r.text
    #     code = r.status_code
    #     print result
    #     print code
    #     js = decryptAES(str(result),self.key)
    #     print js
    #     self.assertEqual(code, 200)
