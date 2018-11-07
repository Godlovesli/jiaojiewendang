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


class literecipegetTest(MyTest):
    '''获自选页默认的六个食谱的烹饪程序'''
    url_path = '/literecipe/defalse/recipe/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_literecipeget_success(self):
        ''' 所有参数都填，操作成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select B.deviceId from mipot_device B ,mipot_device_model_recipe A where A.devicemodelid=B.deviceModelId"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            deviceid = rows['deviceId']
            params = 'pageNo=1&perpage=5&deviceid='+str(deviceid)
            r = self.myhttp('GET',
                            self.url_path,
                            params,

                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('获取食谱列表成功', js['message'])
        else:
            print "未找到默认食谱"


    def test_literecipeget_btsuccess(self):
        '''只传必填参数，操作成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select B.deviceId from mipot_device B ,mipot_device_model_recipe A where  \
              A.devicemodelid=B.deviceModelId and B.deviceModelId = '1'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            deviceid = rows['deviceId']
            params = 'deviceid=' + str(deviceid)
            r = self.myhttp('GET',
                            self.url_path,
                            params,

                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('获取食谱列表成功', js['message'])
        else:
            print "未找到默认食谱"


    def test_literecipeget_delose(self):
        '''测试参数不完整，必填参数(deviceId)未传'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'deviceid' is not present", js['message'])


    def test_literecipeget_denull(self):
        '''必填字段(deviceId)的值为空'''
        params = 'deviceId='
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'deviceid' is not present", js['message'])


    def test_literecipeget_depanull(self):
        '''必填字段(deviceId)为空'''
        params = '=81251114'
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'deviceid' is not present", js['message'])


    def test_literecipeget_signerror(self):
        '''sign不正确'''
        params ={'deviceId': '81251114'}
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
        # params = urllib.urlencode({'deviceId': '81251114'})
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2=self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature +'e')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_literecipeget_noncerror(self):
        '''nonce不正确'''
        params ={'deviceId': '81251114'}
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
        # params = urllib.urlencode({'deviceId': '81251114'})
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # url2=self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce +'e')
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
    testunit.addTest(literecipegetTest('test_literecipeget_success'))
    testunit.addTest(literecipegetTest('test_literecipeget_btsuccess'))
    testunit.addTest(literecipegetTest('test_literecipeget_delose'))
    testunit.addTest(literecipegetTest('test_literecipeget_denull'))
    testunit.addTest(literecipegetTest('test_literecipeget_depanull'))
    testunit.addTest(literecipegetTest('test_literecipeget_signerror'))
    testunit.addTest(literecipegetTest('test_literecipeget_noncerror'))


    fp = open('./literecipeget_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'获自选页默认的六个食谱的烹饪程序接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


