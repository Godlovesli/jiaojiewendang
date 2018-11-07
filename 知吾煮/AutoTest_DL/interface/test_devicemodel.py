#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import random
import requests

from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class devicemodelTest(MyTest):
    '''获取所有设备型号'''
    url_path =  '/v1/devicemodel/list/get'

    @classmethod
    def setUpClass(cls):
        pass


    def test_devicemodellist_success(self):
        '''获取所有设备型号'''
        r = self.nosign('GET',
                         self.url_path,
                         {'': ''},
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)

# class devicemodel1Test(unittest.TestCase):
#     '''获取所有设备型号'''
#     def setUp(self):
#         self.base_url = 'http://10.0.10.64:18080'
#         #self.base_url='https://inapi.coo-k.com'
#         self.url = self.base_url+'/devicemodel/list/get'
#         self.nonce = generateNonce()
#         self.signature = generateSignature(self.nonce, 'GET', self.url)
#         self.key = getSessionSecurity(self.nonce)
#
#
#     def test_devicemodel_success(self):
#         '''获取成功'''
#         request = urllib2.Request(self.url )
#         #request.add_header('nonce',self.nonce)
#         request.add_header('User-Agent','chunmiapp')
#         #request.add_header('signature',self.signature)
#         response = urllib2.urlopen(request)
#         result = response.read()
#         print result
#         js = json.loads(result)
#         self.assertEqual(js['state'],1)
#
#
#
#

if __name__ == '__main__':
    # unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(devicemodelTest('test_devicemodel_success'))



    fp = open('./devicemodel.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'获取所有设备型号接口测试报告',
                            description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()




