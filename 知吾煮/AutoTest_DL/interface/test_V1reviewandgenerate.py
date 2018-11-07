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


class reviewandgenerateTest(MyTest):
    '''运行烹饪程序'''
    url_path =  '/v1/recipe/reviewandgenerate'

    @classmethod
    def setUpClass(cls):
        pass


    def test_reviewandgenerate_success(self):
        '''所有参数都传入，预览成功'''
        self.url = self.base_url + '/v1/recipe/reviewandgenerate'
        print self.url
        self.signature = generateSignature(self.nonce, 'POST', self.url)
        self.token = Login().login()     #引用登录
        # register_openers()
        post_data = {"id":"",
	                "name":"运行烹饪程序",
	                "deviceid":"1083258",
	                "templetid":"19",
	                "tagList":[319,267,266,257,164],
	                "auxiliaryList":[{"name":"Q","quality":"1"},{"name":"W","quality":"2"}],
	                "ingredientList":[{"name":"E","quality":"2"},{"name":"R","quality":""},{"name":"","quality":"4"}],
	                "steps":[{"stepPic":"1498529207/4986F036-0F1E-4C62-8CE7-2DFD2B87FC28-960F91E6-0AC3-4B62-A750-5113C58DF9FD.jpg","description":"1","resumeIndex": 5,"resumeTime": 6,"resumeType": 18020},
	                        {"stepPic":"","description":"2"},{"stepPic":"","description":"3"},
	                        {"stepPic":"1498529232/4986F036-0F1E-4C62-8CE7-2DFD2B87FC28-44D5C93F-0652-481B-8A5E-B974D0AA4E87.jpg","description":"4","resumeIndex": 5,"resumeTime": 3,"resumeType": 18020}],
	                "content":"",
	                "iconPath":"1498529157/4986F036-0F1E-4C62-8CE7-2DFD2B87FC28-8FABB4F3-FADA-4B62-82CA-DE409E0389B1.jpg",
	                "peopleNum":"2",
	                # "duration":"",
	                "description":"Hah ",
	                "deviceModelGroupList":[],
	                "riceId":"1",
	                "hardness":"50"}
        print(type(post_data))
        data_json = json.dumps(post_data)
        print data_json
        A="json="+data_json
        print A
        A='json={"auxiliaryList":[{"name":"糙米","quality":"u舅舅家"}],"description":"良苦用心","deviceid":"45425163","hardness":60,"iconPath":"recipe/222e821c-bbbc-4e31-abac-9c014ccc30fa.jpg","id":"","ingredientList":[{"name":"吃饱*个","quality":"帮你拿"}],"name":"可口可乐了","peopleNum":5,"riceId":"40165","steps":[{"description":"u加班不","name":"步骤图片和描述","resumeIndex":0,"resumeTime":0,"resumeType":0,"stepPic":"recipe/d1af80ba-c9ea-426f-bdb0-93e47e980558.png"},{"description":"皇后娘娘VB","resumeIndex":2,"resumeTime":5,"resumeType":18020,"stepPic":"recipe/f6915877-6477-41d5-9204-4eb6cb316297.png"}],"tagList":[302,291,268],"templetid":"10"}'
        print(type(A))
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
        recipeid = js['result'][0]['id']
        print recipeid
        return recipeid

