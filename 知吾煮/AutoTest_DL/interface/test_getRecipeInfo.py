#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
from base.preview import Preview
from base.V1preview import V1Preview
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class getRecipeInfoTest(MyTest):
    '''获取某个食谱的所有信息'''
    url_path =  '/v1/recipe/getRecipeInfo'

    @classmethod
    def setUpClass(cls):
        pass


    def test_getRecipeInfo_success(self):
        '''获取食谱信息成功'''
        recipeid = Preview().preview()
        print recipeid
        token = Login().login()     #引用登录
        print token
        params = 'recipeId='+str(recipeid)
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn(u'获取食谱信息成功',js['message'])


    def test_getRecipeInfo_relose(self):
        '''测试参数不完整，必填参数(recipeId)未传'''
        token = Login().login()     #引用登录
        print token
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'recipeId' is not present", js['message'])


    def test_getRecipeInfo_renull(self):
        '''必填字段(recipeId)的值为空'''
        token = Login().login()     #引用登录
        print token
        params = 'recipeId='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'recipeId' is not present", js['message'])


    def test_getRecipeInfo_repanull(self):
        '''必填参数(recipeId)为空'''
        token = Login().login()     #引用登录
        print token
        params = '=2500'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'recipeId' is not present", js['message'])



    def test_getRecipeInfo_tokenerror(self):
        '''token错误'''
        token = Login().login()     #引用登录
        print token
        params = 'recipeId=2500'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+'1' )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn(u'token无效',js['message'])


    def test_getRecipeInfo_tokennull(self):
        '''未传入token'''
        params = 'recipeId=2500'
        r = self.myhttp1('GET',
                        self.url_path,
                         params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn(u'token无效',js['message'])


    def test_getRecipeInfo_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'recipeId': '652'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params,
                        self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])

        #
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'recipeId': '652'})
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


    def test_getRecipeInfo_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'recipeId': '652'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        self.token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'recipeId': '652'})
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
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_success'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_reIDno'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_relose'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_renull'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_repanull'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_reerror'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_IDc'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_IDe'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_tokenerror'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_tokennull'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_signerror'))
    testunit.addTest(getRecipeInfoTest('test_getRecipeInfo_noncerror'))


    fp = open('./getRecipeInfo_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'获取某个食谱的所有信息接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


