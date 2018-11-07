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

class removepostTest(MyTest):
    '''取消收藏'''
    url_path = '/recipe/collect/remove/post'


    @classmethod
    def setUpClass(cls):
        pass

    def test_removepost_success(self):
        '''操作成功'''
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId=256'
        r = self.myhttp('POST',
                        self.url_path,
                         params,
                         # {'recipeId': '256'},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( '操作成功',js['message'])

    def test_removepost_reno(self):
        '''传入不存在的recipeId'''
        params = 'recipeId=23201608420'
        token = Login().login()  # 引用登录
        print token
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'recipeId': '23201608420'},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('食谱不存在', js['message'])

    def test_removepost_relose(self):
        '''测试参数不完整，必填参数(recipeId)未传'''
        token = Login().login()  # 引用登录
        print token
        params = ''
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': ''},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)

    def test_removepost_renull(self):
        '''必填字段(recipeId)的值为空'''
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'recipeId': ''},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)

    def test_removepost_repanull(self):
        '''必填字段(recipeId)为空'''
        token = Login().login()  # 引用登录
        print token
        params = '=431'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': '431'},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)


    def test_removepost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId=256'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'recipeId': '432'},
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_removepost_tokenull(self):
        '''未传入token'''
        params = 'recipeId=256'
        r = self.myhttp1('POST',
                        self.url_path,
                        params,
                        # {'recipeId': '432'},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_removepost_signerror(self):
        '''sign不正确'''
        params ={'recipeId': '431'}
        r = self.signerror('POST',
                           self.url_path,
                           params,
                           # {'deviceid':'1128170','':'1558'}
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'recipeId': '431'})
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
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



    def test_removepost_noncerror(self):
        '''nonce不正确'''
        params ={'recipeId': '431'}
        r = self.noncerror('POST',
                           self.url_path,
                           params,
                           # {'deviceid':'1128170','':'1558'}
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'recipeId': '431'})
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
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
    testunit.addTest(removepostTest('test_removepost_success'))
    testunit.addTest(removepostTest('test_removepost_reno'))
    testunit.addTest(removepostTest('test_removepost_relose'))
    testunit.addTest(removepostTest('test_removepost_renull'))
    testunit.addTest(removepostTest('test_removepost_repanull'))
    testunit.addTest(removepostTest('test_removepost_reerror'))
    testunit.addTest(removepostTest('test_removepost_rec'))
    testunit.addTest(removepostTest('test_removepost_ree'))
    testunit.addTest(removepostTest('test_removepost_tokenerror'))
    testunit.addTest(removepostTest('test_removepost_tokenull'))
    testunit.addTest(removepostTest('test_removepost_signerror'))
    testunit.addTest(removepostTest('test_removepost_noncerror'))


    fp = open('./removepost_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'取消收藏接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()
