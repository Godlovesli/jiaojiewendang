#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class publishTest(MyTest):
    '''发布作品'''
    url_path = '/show/publish'

    @classmethod
    def setUpClass(cls):
        pass

    def test_publish_success(self):
        '''所有必填参数都传，发布作品成功'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                        self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': u'确实很美味', 'recipeId': '258'},
                        token
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], 1)
        self.assertEqual(js['message'], u'发布作品成功')


    def test_publish_phlose(self):
        '''测试参数不完整，某个必填参数(photo)未传'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'experienceSharing': u'确实很美味', 'recipeId': '258'},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn( "parameter 'photo' is not present",js['message'])

    def test_publish_exlose(self):
        '''测试参数不完整，某个必填参数(experienceSharing)未传'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), 'recipeId': '258'},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'experienceSharing' is not present", js['message'])



    def test_publish_relose(self):
        '''测试参数不完整，某个必填参数(recipeId)未传'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': u'确实很美味'},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'recipeId' is not present", js['message'])


    def test_publish_phnull(self):
        '''必填参数(photo)的值为空'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'photo': '', 'experienceSharing': u'确实很美味', 'recipeId': '258'},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'photo' is not present", js['message'])


    def test_publish_exnull(self):
        '''必填参数(experienceSharing)的值为空'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': '', 'recipeId': '258'},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("experienceSharing 不能为空", js['message'])


    def test_publish_renull(self):
        '''必填参数(recipeId)的值为空'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': u'确实很美味', 'recipeId': ''},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("recipeId 不能为空", js['message'])


    def test_publish_phpanull(self):
        '''必填参数(photo)为空'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'': open(r'D:\test.jpg', 'rb'), 'experienceSharing': u'确实很美味', 'recipeId': '258'},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("parameter 'photo' is not present", js['message'])


    def test_publish_expanull(self):
        '''必填参数(experienceSharing)为空'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), '': u'确实很美味', 'recipeId': '258'},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required String parameter 'experienceSharing' is not present", js['message'])


    def test_publish_repanull(self):
        '''必填参数(recipeId)为空'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': u'确实很美味', '': '258'},
                         token
                         )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'recipeId' is not present", js['message'])


    def test_publish_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        r = self.publish('POST',
                         self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': u'确实很美味', 'recipeId': '258'},
                         token+'1'
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn(u'token无效',js['message'])


    def test_publish_tokennull(self):
        '''未传入token'''
        r = self.publish('POST',
                         self.url_path,
                         {'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': u'确实很美味', 'recipeId': '258'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn(u'token无效',js['message'])


    def test_publish_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "POST", self.url)
        register_openers()
        data, headers = multipart_encode({'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': '256', 'recipeId': '256'})
        request = urllib2.Request(self.url, data=data, headers=headers)
        request.add_header('nonce', self.nonce)
        request.add_header('signature', self.signature + '1')
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('token', self.token)
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'],-2)
        self.assertIn('拦截请求授权出错',js['message'])


    def test_publish_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        self.url = self.base_url + self.url_path
        self.signature = generateSignature(self.nonce, "POST", self.url)
        register_openers()
        data, headers = multipart_encode({'photo': open(r'D:\test.jpg', 'rb'), 'experienceSharing': '256', 'recipeId': '256'})
        request = urllib2.Request(self.url, data=data, headers=headers)
        request.add_header('nonce', self.nonce + '1')
        request.add_header('signature', self.signature)
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('token', self.token)
        response = urllib2.urlopen(request)
        result = response.read()
        print result
        js = json.loads(result)
        self.assertEqual(js['state'],-2)
        self.assertIn('拦截请求授权出错',js['message'])



if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(publishTest('test_publish_success'))
    testunit.addTest(publishTest('test_publish_phlose'))
    testunit.addTest(publishTest('test_publish_exlose'))
    testunit.addTest(publishTest('test_publish_relose'))
    testunit.addTest(publishTest('test_publish_phnull'))
    testunit.addTest(publishTest('test_publish_exnull'))
    testunit.addTest(publishTest('test_publish_renull'))
    testunit.addTest(publishTest('test_publish_phpanull'))
    testunit.addTest(publishTest('test_publish_expanull'))
    testunit.addTest(publishTest('test_publish_repanull'))
    testunit.addTest(publishTest('test_publish_tokenerror'))
    testunit.addTest(publishTest('test_publish_tokennull'))
    testunit.addTest(publishTest('test_publish_signerror'))
    testunit.addTest(publishTest('test_publish_noncerror'))


    fp = open('./publish_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'发布作品接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()



