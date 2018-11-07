#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
from base.mydb import MyDB
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

class V3removepostTest(MyTest):
    '''取消收藏'''
    url_path = '/v3/recipe/collect/remove/post'


    @classmethod
    def setUpClass(cls):
        pass

    def test_v3removepost_success(self):
        '''操作成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe A where A.state='2200'"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        recipeId = rows['id']
        print recipeId
        params = 'recipeId='+str(recipeId)
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                         # {'recipeId': recipeId},
                         token
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( '操作成功',js['message'])


    def test_v3removepost_relose(self):
        '''测试参数不完整，必填参数(recipeId)未传'''
        token = Login().login()  # 引用登录
        print token
        params = ''
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)



    def test_v3removepost_renull(self):
        '''必填字段(recipeId)的值为空'''
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)


    def test_v3removepost_repanull(self):
        '''必填字段(recipeId)为空'''
        token = Login().login()  # 引用登录
        print token
        params = '431'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)



    def test_v3removepost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'recipeId=431'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token+'1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_v3removepost_tokenull(self):
        '''未传入token'''
        params = 'recipeId=431'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_removepost_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'recipeId': '431'}
        print params
        r = self.signerror('POST',
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
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])



    def test_removepost_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params = {'recipeId': '431'}
        print params
        r = self.noncerror('POST',
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
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])



if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(V3removepostTest('test_removepost_success'))
    testunit.addTest(V3removepostTest('test_removepost_reno'))
    testunit.addTest(V3removepostTest('test_removepost_relose'))
    testunit.addTest(V3removepostTest('test_removepost_renull'))
    testunit.addTest(V3removepostTest('test_removepost_repanull'))
    testunit.addTest(V3removepostTest('test_removepost_reerror'))
    testunit.addTest(V3removepostTest('test_removepost_rec'))
    testunit.addTest(V3removepostTest('test_removepost_ree'))
    testunit.addTest(V3removepostTest('test_removepost_tokenerror'))
    testunit.addTest(V3removepostTest('test_removepost_tokenull'))
    testunit.addTest(V3removepostTest('test_removepost_signerror'))
    testunit.addTest(V3removepostTest('test_removepost_noncerror'))


    fp = open('./v3removepost_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'取消收藏接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()
