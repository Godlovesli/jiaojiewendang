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


class ricecookscriptfindTest(MyTest):
    '''查找米烹饪程序'''
    url_path = '/ricecookscript/find'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecookscriptfind_success(self):
        '''传必填参数'''
        # # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        # db = MyDB().getCon()
        # cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        # sql = "select A.riceId,A.cookstyle,B.deviceId from mipot_rice_cookscript A ,mipot_device B where  \
        #       A.deviceModelId=B.deviceModelId"
        # data_count = cursor.execute(sql)
        # print data_count
        # if data_count > 0:
        #     rows = cursor.fetchone()
        #     print rows
        #     riceid = rows['1']
        #     cookstyleid = rows['1100']
        #     deviceid = rows['1082455']
        params = 'riceid=1&cookstyleid=1100&deviceid=1082455'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'riceid': 1, 'cookstyleid': 1100, 'deviceid':1082455},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], 1)
        self.assertIn('成功', js['message'])



    def test_ricecookscriptfind_rilose(self):
        '''测试参数不完整，必填参数(riceid)未传'''
        params = 'cookstyleid=1100&deviceid=1082455'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'cookstyleid': '1100', 'deviceid': '81251112'},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'riceid' is not present", js['message'])



    def test_ricecookscriptfind_colose(self):
        '''测试参数不完整，必填参数(cookstyleid)未传'''
        params = 'riceid=2&deviceid=1082455'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'riceid': '2', 'deviceid': '81251112'},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'cookstyleid' is not present", js['message'])

    def test_ricecookscriptfind_delose(self):
        '''测试参数不完整，必填参数(deviceid)未传'''
        params = 'riceid=2&cookstyleid=1100'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'riceid': '2', 'cookstyleid': '1100'},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'deviceid' is not present", js['message'])


    def test_ricecookscriptfind_rinull(self):
        '''必填参数(riceid)的值为空'''
        params = 'riceid=&cookstyleid=1100&deviceid=81251112'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'riceid': '', 'cookstyleid': '1100', 'deviceid': '81251112'},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'riceid' is not present", js['message'])


    def test_ricecookscriptfind_conull(self):
        '''必填参数(cookstyleid)的值为空'''
        params = 'riceid=2&cookstyleid=&deviceid=81251112'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'riceid': '2', 'cookstyleid': '', 'deviceid': '81251112'},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'cookstyleid' is not present", js['message'])


    def test_ricecookscriptfind_denull(self):
        '''必填参数(deviceid)的值为空'''
        params = 'riceid=2&cookstyleid=1100&deviceid='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'riceid': '2', 'cookstyleid': '1100', 'deviceid': ''},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'deviceid' is not present", js['message'])


    def test_ricecookscriptfind_ripanull(self):
        '''必填参数(riceid)为空'''
        params = '=2&cookstyleid=1100&deviceid=81251112'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'': '2', 'cookstyleid': '1100', 'deviceid': '81251112'},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'riceid' is not present", js['message'])


    def test_ricecookscriptfind_copanull(self):
        '''必填参数(cookstyleid)为空'''
        params = 'riceid=2&=1100&deviceid=81251112'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'riceid': '2', '': '1100', 'deviceid': '81251112'},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'cookstyleid' is not present", js['message'])


    def test_ricecookscriptfind_depanull(self):
        '''必填参数(deviceid)为空'''
        params = 'riceid=2&cookstyleid=1100&=81251112'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'riceid': '2', 'cookstyleid': '1100', '': '81251112'},

                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'deviceid' is not present", js['message'])


    def test_ricecookscriptfind_signerror(self):
        '''sign不正确'''
        params ={'riceid':'2','cookstyleid':'1100','deviceid':'81251112'}
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
        # params = urllib.urlencode({'riceid':'2','cookstyleid':'1100','deviceid':'81251112'})
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # URL = self.url + '?' + payload
        # request = urllib2.Request(URL)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature +'e')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


    def test_ricecookscriptfind_noncerror(self):
        '''nonce不正确'''
        params ={'riceid':'2','cookstyleid':'1100','deviceid':'81251112'}
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
        # params = urllib.urlencode({'riceid':'2','cookstyleid':'1100','deviceid':'81251112'})
        # print '传入的参数:'+ params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # URL = self.url + '?' + payload
        # request = urllib2.Request(URL)
        # request.add_header('nonce', self.nonce+'e')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature )
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])


if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_success'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_rilose'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_colose'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_delose'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_rinull'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_conull'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_denull'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_ripanull'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_copanull'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_depanull'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_signerror'))
    testunit.addTest(ricecookscriptfindTest('test_ricecookscriptfind_noncerror'))


    fp = open('./ricecookscriptfind_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'查找米烹饪程序接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()









