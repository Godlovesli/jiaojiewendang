#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class defalsegetTest(MyTest):
    '''查询饭煲类型的默认食谱'''
    url_path = '/recipe/device/defalse/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_defalseget_success(self):
        '''操作成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_device_model where volume='2200'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            devicemodelname = rows['name']
            params = 'devicemodelname='+str(devicemodelname)
            r = self.myhttp('GET',
                            self.url_path,
                            params,

                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('成功', js['message'])
        else:
            print "未找到默认食谱"


    def test_defalseget_dnlose(self):
        '''测试参数不完整，必填参数(devicemodelname)未传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn("获取失败", js['message'])


    def test_defalseget_dnnull(self):
        '''必填参数(devicemodelname)的值为空'''
        params = 'devicemodelname='
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn("获取失败", js['message'])


    def test_defalseget_dnpanull(self):
        '''必填参数(devicemodelname)为空'''
        params = '=chunmi.cooker.press1'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -1)
        self.assertIn("获取失败", js['message'])


    def test_defalseget_signerror(self):
        '''sign不正确'''

        params = {'devicemodelname': 'chunmi.cooker.press1'}
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
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'devicemodelname': 'chunmi.cooker.press1'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature+'1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])



    def test_defalseget_noncerror(self):
        '''nonce不正确'''
        params = {'devicemodelname': 'chunmi.cooker.press1'}
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
        # params = urllib.urlencode({'devicemodelname': 'chunmi.cooker.press1'})
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce+'1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])



if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(defalsegetTest('test_defalseget_success'))
    testunit.addTest(defalsegetTest('test_defalseget_dnlose'))
    testunit.addTest(defalsegetTest('test_defalseget_dnnull'))
    testunit.addTest(defalsegetTest('test_defalseget_dnpanull'))
    testunit.addTest(defalsegetTest('test_defalseget_signerror'))
    testunit.addTest(defalsegetTest('test_defalseget_noncerror'))


    fp = open('./defalseget_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'查询饭煲类型的默认食谱接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


