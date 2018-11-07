#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
import requests
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class v2minegetTest(MyTest):
    '''关注'''
    url_path = '/v1/recipe/collect/mine/get'


    @classmethod
    def setUpClass(cls):
        pass

    def test_v2mineget_success(self):
        '''操作成功'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageNo=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('操作成功',js['message'])

    def test_v2mineget_nolose(self):
        '''pageNo未传'''
        token = Login().login()  # 引用登录
        print token
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)

    def test_v2mineget_nonull(self):
        '''pageNo的值为空'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageNo='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)

    def test_v2mineget_nopanull(self):
        '''pageNo参数为空'''
        token = Login().login()  # 引用登录
        print token
        params = '=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)


    def test_v2mineget_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageNo=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+'eee'
                             )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])

    def test_v2mineget_tokenull(self):
        '''未传入token'''
        params = 'pageNo=1'
        r = self.myhttp1('GET',
                            self.url_path,
                         params,

                             )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])


    def test_v2mineget_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = { 'pageNo': '1'}
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



        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode( {'pageNo': '1'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url+payload)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_v2mineget_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = { 'pageNo': '1'}
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
        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode( {'pageNo': '1'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url+payload)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])



if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(v2minegetTest('test_v2mineget_success'))
    testunit.addTest(v2minegetTest('test_v2mineget_tokenerror'))
    testunit.addTest(v2minegetTest('test_v2mineget_tokenull'))
    testunit.addTest(v2minegetTest('test_v2mineget_signerror'))
    testunit.addTest(v2minegetTest('test_v2mineget_noncerror'))


    fp = open('./mineget_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'关注接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


