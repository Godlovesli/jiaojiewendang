#coding:utf-8
#__author__ = 'feng'
from base.base import MyTest
import requests
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class feedbacksubmitTest(MyTest):
    '''提交反馈'''
    url_path='/feedback/submit'

    @classmethod
    def setUpClass(cls):
        pass


    def test_feedbacksubmit_success(self):
        params = 'description=用起来不错哟&contact=13126196610&pics=/fcdb247fbfe3424792d0a7abf9eaceac.jpg'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('反馈提交成功', js['message'])


    def test_feedbacksubmit_btsuccess(self):
        '''只传入必填参数，反馈提交成功'''
        params = 'description=用起来不错哟'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('反馈提交成功', js['message'])



    def test_feedbacksubmit_delose(self):
        '''测试参数不完整，必填参数(desctiprion)未传'''
        params = ''
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],-4)
        self.assertIn(u'description 字段不能为null',js['message'])


    def test_feedbacksubmit_denull(self):
        '''必填字段(desctiprion)的值为空'''
        params = 'description='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],-4)
        self.assertIn(u'description 字段不能为null',js['message'])


    def test_feedbacksubmit_depanull(self):
        '''必填参数(desctiprion)为空'''
        params = '=1234'
        r = self.myhttp('POST',
                        self.url_path,
                         params,
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],-4)
        self.assertIn(u'description 字段不能为null',js['message'])



    def test_feedbacksubmit_signerror(self):
        '''sign不正确'''
        params = {'description': '1234'}
        print params
        r = self.signerror('POST',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'desctiprion': '1234'})
        # request = urllib2.Request(self.url,data=params)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


    def test_feedbacksubmit_noncerror(self):
        '''nonce不正确'''
        params = {'description': '1234'}
        print params
        r = self.noncerror('POST',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'desctiprion': '1234'})
        # request = urllib2.Request(self.url,data=params)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])
        #



if __name__ == '__main__':
    # unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(feedbacksubmitTest('test_feedbacksubmit_success'))
    testunit.addTest(feedbacksubmitTest('test_feedbacksubmit_btsuccess'))
    testunit.addTest(feedbacksubmitTest('test_feedbacksubmit_delose'))
    testunit.addTest(feedbacksubmitTest('test_feedbacksubmit_denull'))
    testunit.addTest(feedbacksubmitTest('test_feedbacksubmit_depanull'))
    testunit.addTest(feedbacksubmitTest('test_feedbacksubmit_deerror'))
    testunit.addTest(feedbacksubmitTest('test_feedbacksubmit_signerror'))
    testunit.addTest(feedbacksubmitTest('test_feedbacksubmit_noncerror'))


    fp = open('./feedbacksubmit.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'提交反馈接口测试报告',
                            description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()
