#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class tagListTest(MyTest):
    '''获取食谱标签'''
    url_path = '/recipe/tagList'

    @classmethod
    def setUpClass(cls):
        pass

    def test_taglist_success(self):
        '''获取食谱标签列表成功'''
        r = self.nocryp('GET',
                        self.url_path,
                         {'':''},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn(u'获取食谱标签列表成功',js['message'])

    def test_taglist_signerror(self):
        '''sign不正确'''
        params ={'':''}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # request = urllib2.Request(self.url)
        # request.add_header('nonce',self.nonce)
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature+'2')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_taglist_noncerror(self):
        '''nonce不正确'''
        params ={'':''}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # request = urllib2.Request(self.url)
        # request.add_header('nonce',self.nonce+'2')
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


if __name__ == '__main__':
    # unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(tagListTest('test_taglist_success'))
    testunit.addTest(tagListTest('test_taglist_signerror'))
    testunit.addTest(tagListTest('test_taglist_noncerror'))


    fp = open('./tagList.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'获取食谱标签接口测试报告',
                            description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()


