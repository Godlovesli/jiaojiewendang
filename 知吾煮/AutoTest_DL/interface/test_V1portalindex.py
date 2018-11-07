#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
import requests
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class portalindexTest(MyTest):
    '''APP首页'''
    # url_path = '/v1/portal/index'
    url_path = '/v1/portal/potandinduction/index'

    @classmethod
    def setUpClass(cls):
        pass

    def test_searchappdataget_success134(self):
        '''传入所有参数'''
        self.base_url = 'https://cinapi.joyami.com'
        url = self.base_url + self.url_path
        print url
        signature = generateSignature(self.nonce, 'GET', url)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': signature
                   }
        # params = {'param': 'value', 'param': 'value'}
        # payload1 = urllib.urlencode(params)
        params = ''
        encoded = encryptAES(params, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        r = requests.get(url, params=params, headers=headers, verify=False)
        result = r.text.encode()
        print result
        s = decryptAES(result, self.key)
        print s

    def test_portalindex_success(self):
        '''获取成功'''
        params = ''
        r = self.bujiami('GET',
                        self.url_path,
                         params
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn(u'获取成功',js['message'])
        # print js['result'][0]['hot_search_recipe']



    def test_portalindex_signerror(self):
        '''sign不正确'''
        params = {'': ''}
        print params
        r = self.signerror('GET',
                           self.url_path,
                           params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # request = urllib2.Request(self.url)
        # request.add_header('nonce',self.nonce)
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature+'2')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_portalindex_noncerror(self):
        '''nonce不正确'''
        # params = {'': ''}
        # print params
        # r = self.noncerror('GET',
        #                    self.url_path,
        #                    params
        #                    )
        # print r
        # js = json.loads(r)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # request = urllib2.Request(self.url)
        # request.add_header('nonce',self.nonce)
        # request.add_header('User-Agent','chunmiapp')
        # request.add_header('signature',self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


if __name__ == '__main__':
    # unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(portalindexTest('test_portalindex_success'))
    testunit.addTest(portalindexTest('test_portalindex_signerror'))
    testunit.addTest(portalindexTest('test_portalindex_noncerror'))


    fp = open('./portalindex.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'App首页接口测试报告',
                            description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()




