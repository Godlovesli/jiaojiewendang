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

class messagegetTest(MyTest):
    '''获取社区消息列表'''
    url_path = '/message/get'


    @classmethod
    def setUpClass(cls):
        pass

    def test_mget_success(self):
        '''获取成功'''
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


    def test_mget_btbcsuccess(self):
        '''获取成功'''
        params = ''
        token = Login().login()  # 引用登录
        print token
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)


    def test_mget_tokenerror(self):
        '''token错误'''
        params = ''
        token = Login().login()  # 引用登录
        print token
        r = self.myhttp('GET',
                            self.url_path,
                            params,
                            token+'1'
                             )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])



    def test_mget_tokenull(self):
        '''未传入token'''
        params = ''
        r = self.myhttp1('GET',
                            self.url_path,
                            params,

                             )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])


    def test_mget_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'': ''}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])

        #
        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # request = urllib2.Request(self.url )
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


    def test_mget_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'': ''}
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
        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # request = urllib2.Request(self.url)
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
    testunit.addTest(messagegetTest('test_mget_success'))
    testunit.addTest(messagegetTest('test_mget_btbcsuccess'))
    testunit.addTest(messagegetTest('test_mget_tokenerror'))
    testunit.addTest(messagegetTest('test_mget_tokenull'))
    testunit.addTest(messagegetTest('test_mget_signerror'))
    testunit.addTest(messagegetTest('test_mget_noncerror'))


    fp = open('./messageget_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'获取社区消息列表接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


