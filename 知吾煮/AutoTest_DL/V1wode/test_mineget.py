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

class minegetTest(MyTest):
    '''关注'''
    url_path = '/recipe/collect/mine/get'


    @classmethod
    def setUpClass(cls):
        pass

    def test_mineget_success(self):
        '''操作成功'''
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
        self.assertEqual(js['state'], 1)
        self.assertIn('操作成功',js['message'])

    def test_mineget_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = ''
        r = self.myhttp('GET',
                            self.url_path,
                            params,
                            token+'1'
                             )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效',js['message'])

    def test_mineget_tokenull(self):
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


    def test_mineget_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno': '1'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r


    def test_mineget_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'pageno': '1'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                            params,
                           self.token
                           )
        print r




if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(minegetTest('test_mineget_success'))
    testunit.addTest(minegetTest('test_mineget_tokenerror'))
    testunit.addTest(minegetTest('test_mineget_tokenull'))
    testunit.addTest(minegetTest('test_mineget_signerror'))
    testunit.addTest(minegetTest('test_mineget_noncerror'))


    fp = open('./mineget_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'关注接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


