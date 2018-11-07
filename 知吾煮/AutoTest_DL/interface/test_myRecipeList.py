#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
from base.preview import Preview
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class myRecipeListTest(MyTest):
    '''我的食谱列表'''
    url_path =  '/recipe/myRecipeList'

    @classmethod
    def setUpClass(cls):
        pass

    def test_myRecipeList_success(self):
        '''获取成功'''
        token = Login().login()     #引用登录
        print token
        r = self.nocryp('GET',
                        self.url_path,
                         {'':''},
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn(u'获取我的食谱列表成功',js['message'])


    def test_myRecipeList_tokenerror(self):
        '''token错误'''
        token = Login().login()     #引用登录
        print token
        r = self.nocryp('GET',
                        self.url_path,
                         {'':''},
                        token+'1' )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn( u'token无效',js['message'])


    def test_myRecipeList_tokennull(self):
        '''未传入token'''
        r = self.bujiami('GET',
                        self.url_path,
                         {'':''},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn( u'token无效',js['message'])


    def test_myRecipeList_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'':''}
        print params
        r = self.signerror('GET',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'':''})
        # request = urllib2.Request(self.url + '?' + params)
        # print request
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
        #

    def test_myRecipeList_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'':''}
        print params
        r = self.noncerror('GET',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        #
        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'':''})
        # request = urllib2.Request(self.url + '?' + params)
        # print request
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(myRecipeListTest('test_myRecipeList_success'))
    testunit.addTest(myRecipeListTest('test_myRecipeList_tokenerror'))
    testunit.addTest(myRecipeListTest('test_myRecipeList_tokennull'))
    testunit.addTest(myRecipeListTest('test_myRecipeList_signerror'))
    testunit.addTest(myRecipeListTest('test_myRecipeList_noncerror'))


    fp = open('./myRecipeList_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'我的食谱列表接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


