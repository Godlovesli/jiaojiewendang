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


class deleteDraftTest(MyTest):
    '''草稿箱删除某个草稿'''
    url_path =  '/v1/recipe/deleteDraft'

    @classmethod
    def setUpClass(cls):
        pass

    def test_deleteDraft_success1(self):
        '''删除成功'''
        recipeid = V1Preview().V1preview()
        print recipeid
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId='+str(recipeid)
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'recipeId': recipeid},
                        token)
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'删除成功', js['message'])

    def test_deleteDraft_success(self):
        '''删除成功'''
        recipeid = Preview().preview()
        print recipeid
        token = Login().login()     #引用登录
        print token
        params = 'recipeId=' + str(recipeid)
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                         # {'recipeId':recipeid},
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn(u'删除成功',js['message'])


    def test_deleteDraft_relose(self):
        '''测试参数不完整，必填参数(recipeId)未传'''
        token = Login().login()     #引用登录
        print token
        params = ''
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        # self.assertIn("parameter 'recipeId' is not present", js['message'])


    def test_deleteDraft_renull(self):
        '''必填字段(recipeId)的值为空'''
        token = Login().login()     #引用登录
        print token
        params = 'recipeId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                         # {'recipeId':''},
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        # self.assertIn("parameter 'recipeId' is not present", js['message'])


    def test_deleteDraft_repanull(self):
        '''必填参数(recipeId)为空'''
        token = Login().login()     #引用登录
        print token
        params = '=648'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        # self.assertIn("parameter 'recipeId' is not present", js['message'])

    def test_deleteDraft_tokenerror(self):
        '''token错误'''
        token = Login().login()     #引用登录
        print token
        params = 'recipeId=2500'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token+'ee' )
        print r
        js = json.loads(r)

        self.assertEqual(js['state'], -3)
        self.assertIn( u'token无效',js['message'])


    def test_deleteDraft_tokennull(self):
        '''未传入token'''
        params = 'recipeId=2500'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn( u'token无效',js['message'])


    def test_deleteDraft_signerror(self):
        '''sign不正确'''
        params = {'recipeId': '649'}
        print params
        r = self.signerror('POST',
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
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'recipeId': '649'})
        # request = urllib2.Request(self.url, data=params)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'ee')
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_deleteDraft_noncerror(self):
        '''nonce不正确'''
        params = {'recipeId': '649'}
        print params
        r = self.noncerror('POST',
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
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'recipeId': '649'})
        # request = urllib2.Request(self.url, data=params)
        # request.add_header('nonce', self.nonce+'ee')
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
    testunit.addTest(deleteDraftTest('test_deleteDraft_success'))
    testunit.addTest(deleteDraftTest('test_deleteDraft_relose'))
    testunit.addTest(deleteDraftTest('test_deleteDraft_renull'))
    testunit.addTest(deleteDraftTest('test_deleteDraft_repanull'))
    testunit.addTest(deleteDraftTest('test_deleteDraft_tokenerror'))
    testunit.addTest(deleteDraftTest('test_deleteDraft_tokennull'))
    testunit.addTest(deleteDraftTest('test_deleteDraft_signerror'))
    testunit.addTest(deleteDraftTest('test_deleteDraft_noncerror'))


    fp = open('./deleteDraft_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'草稿箱删除某个草稿接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


