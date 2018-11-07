#coding:utf-8
# __author__ = 'feng'
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

class myallShowTest(MyTest):
    '''我的所有作品'''
    url_path = '/show/myallShow'

    @classmethod
    def setUpClass(cls):
        pass


    def test_myshow_success(self):
        '''所有参数都传，获取到我的作品'''
        token = Login().login()  # 引用登录
        r = self.nocryp('GET',
                         self.url_path,
                         {'curPage': '3', 'limit': '5'},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取成功", js['message'])


    def test_myshow_btsuccess(self):
        '''只传必填参数，获取到对应作品'''
        token = Login().login()  # 引用登录
        r = self.nocryp('GET',
                         self.url_path,
                         {'curPage': '3'},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取成功", js['message'])

    def test_myshow_cplose(self):
        '''测试参数不完整，必填参数(curPage)未传'''
        token = Login().login()  # 引用登录
        r = self.nocryp('GET',
                         self.url_path,
                         {'': ''},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取成功", js['message'])

    def test_myshow_cpnull(self):
        '''必填参数(curPage)的值为空'''
        token = Login().login()  # 引用登录
        r = self.nocryp('GET',
                         self.url_path,
                         {'curPage': ''},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取成功", js['message'])


    def test_myshow_cppanull(self):
        '''必填字段(curPage)为空'''
        token = Login().login()  # 引用登录
        r = self.nocryp('GET',
                         self.url_path,
                         {'': '2'},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取成功", js['message'])


    def test_myshow_tokennull(self):
        '''未传入token'''
        r = self.bujiami('GET',
                        self.url_path,
                         {'curPage': '2'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_myshow_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        r = self.nocryp('GET',
                        self.url_path,
                         {'curPage': '2'},
                        token+ '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_myshow_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'curPage':'2'}
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
        # params = urllib.urlencode({'curPage':'2'})
        # request = urllib2.Request(self.url+'?'+params)
        # request.add_header('nonce',self.nonce)
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature + 'e')
        # request.add_header('token', self.token )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_myshow_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'curPage':'2'}
        print params
        r = self.noncerror('GET',
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
        # params = urllib.urlencode({'curPage':'2'})
        # request = urllib2.Request(self.url+'?'+params)
        # request.add_header('nonce',self.nonce + 'e')
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature )
        # request.add_header('token', self.token )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])
        #


if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(myallShowTest('test_myshow_success'))
    testunit.addTest(myallShowTest('test_myshow_btsuccess'))
    testunit.addTest(myallShowTest('test_myshow_cplose'))
    testunit.addTest(myallShowTest('test_myshow_cpnull'))
    testunit.addTest(myallShowTest('test_myshow_cppanull'))
    testunit.addTest(myallShowTest('test_myshow_tokennull'))
    testunit.addTest(myallShowTest('test_myshow_tokenerror'))
    testunit.addTest(myallShowTest('test_myshow_signerror'))
    testunit.addTest(myallShowTest('test_myshow_noncerror'))

    fp = open('./myshow_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'我的所有作品接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()





