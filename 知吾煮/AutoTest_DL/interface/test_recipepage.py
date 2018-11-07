#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
import time
import requests
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipepageTest(MyTest):
    '''分页获取食谱'''
    url_path =  '/recipe/page'

    @classmethod
    def setUpClass(cls):
        pass

    def test_portalindex_success11(self):
        '''获取成功'''
        params = {'curPage': '2', 'limit':20}
        url = self.base_url + self.url_path
        signature = generateSignature(self.nonce, 'GET', url)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': signature
                   }
        payload = urllib.urlencode(params)
        r = requests.get(url, headers=headers,verify=False)
        print r
        result = r.text.encode()
        print result



    def test_recipepage_success(self):
        '''所有参数都传'''
        # params = 'curPage=2&limit=2'
        params = {'curPage': '3', 'limit':20}
        # params = {'': ''}
        r = self.nocryp('GET',
                        self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn(u'获取成功',js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']
            # print js['result'][i]['title']


    def test_recipepage_btsuccess(self):
        '''只传入必填参数'''
        params = {'curPage': '2'}
        r = self.nocryp('GET',
                        self.url_path,
                         params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn(u'获取成功',js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']



    def test_recipepage_culose(self):
        '''测试参数不完整，必填参数(curPage)未传'''
        params = {'': ''}
        r = self.nocryp('GET',
                         self.url_path,
                         params,
                         # {'': ''},
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取成功', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']



    def test_recipepage_cunull(self):
        '''必填字段(curPage)的值为空'''
        params = {'curPage': ''}
        r = self.nocryp('GET',
                         self.url_path,
                         params,
                         # {'curPage': ''},
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取成功', js['message'])


    def test_recipepage_cupanull(self):
        '''必填参数(curPage)为空'''

        params = {'': '2'}
        r = self.nocryp('GET',
                         self.url_path,
                         params,
                         # {'': '2'},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取成功', js['message'])


    def test_recipepage_signerror(self):
        '''sign不正确'''
        params =  {'curPage': '2', 'limit': 2}
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
        # params = urllib.urlencode({'curPage': '1'})
        # print '输入参数：'+params
        # request = urllib2.Request(self.url + '?' + params)
        # request.add_header('nonce',self.nonce)
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature+'1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_recipepage_noncerro(self):
        '''nonce不正确'''
        params =  {'curPage': '2', 'limit': 2}
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
        # params = urllib.urlencode({'curPage': '2'})
        # print '输入参数：'+params
        # request = urllib2.Request(self.url + '?' + params)
        # request.add_header('nonce',self.nonce+'1')
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
    testunit.addTest(recipepageTest('test_recipepage_success'))
    testunit.addTest(recipepageTest('test_recipepage_btsuccess'))
    testunit.addTest(recipepageTest('test_recipepage_culose'))
    testunit.addTest(recipepageTest('test_recipepage_cunull'))
    testunit.addTest(recipepageTest('test_recipepage_cupanull'))
    testunit.addTest(recipepageTest('test_recipepage_signerror'))
    testunit.addTest(recipepageTest('test_recipepage_noncerror'))


    fp = open('./recipepage.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'分页获取食谱接口测试报告',
                            description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()
