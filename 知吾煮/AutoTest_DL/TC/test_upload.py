#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.V1base import MyTest
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class uploadTest(MyTest):
    '''上传图片'''
    url_path = '/file/upload'

    @classmethod
    def setUpClass(cls):
        pass

    def test_upload_success(self):
        '''上传图片成功'''
        r = self.publish('POST',
                        self.url_path,
                         {'filename': open(r'D:\test.jpg', 'rb')},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertEqual(js['message'], u'上传成功')

    def test_upload_null(self):
        '''必填参数的值为空'''
        r = self.publish('POST',
                         self.url_path,
                         {'filename': ''},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],-4)
        self.assertIn("'filename' is not present",js['message'])


    def test_upload_panull(self):
        '''必填参数为空'''
        r = self.publish('POST',
                         self.url_path,
                         {'': open(r'D:\test.jpg', 'rb')},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("'filename' is not present", js['message'])


    def test_upload_signerror(self):
        '''sign不正确'''
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "POST", self.url)
        register_openers()
        data, headers = multipart_encode({'filename': open(r'D:\test.jpg', 'rb')})
        request = urllib2.Request(self.url, data=data, headers=headers)
        request.add_header('nonce', self.nonce)
        request.add_header('signature', self.signature+'e')
        request.add_header('User-Agent', 'chunmiapp')
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'],-2)
        self.assertIn('拦截请求授权出错',js['message'])


    def test_upload_noncerror(self):
        '''nonce不正确'''
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "POST", self.url)
        register_openers()
        data, headers = multipart_encode({'filename': open(r'D:\test.jpg', 'rb')})
        request = urllib2.Request(self.url, data=data, headers=headers)
        request.add_header('nonce', self.nonce+'e')
        request.add_header('signature', self.signature)
        request.add_header('User-Agent', 'chunmiapp')
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'],-2)
        self.assertIn('拦截请求授权出错',js['message'])