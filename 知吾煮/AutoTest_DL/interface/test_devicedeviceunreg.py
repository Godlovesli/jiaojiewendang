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

class devicedeviceunregTest(MyTest):
    '''解绑饭煲'''
    url_path = '/device/un/mydevice/reg'

    @classmethod
    def setUpClass(cls):
        pass

    def test_unreg_success(self):
        '''解绑饭煲（主动解除分享给别人的设备）'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_device_useinfo where userId != '54644930'"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            deviceId = rows['deviceId']
            toUserId = rows['userId']
            print deviceId
            print toUserId
            params = 'deviceId='+str(deviceId)+'&toUserId='+str(toUserId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'deviceId':deviceId,'toUserId':toUserId},
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('操作成功', js['message'])
        else:
            print "不存在分享设备"


    def test_deviceunreg_delose(self):
        '''测试参数不完整，必填参数(deviceId)未传'''
        token = Login().login()  # 引用登录
        params =  'toUserId=1092928237'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("操作失败", js['message'])


    def test_deviceunreg_denull(self):
        '''必填字段(deviceId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'deviceId=&toUserId=1092928237'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'deviceId': '', 'toUserId': 1092928237},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("操作失败", js['message'])


    def test_deviceunreg_depanull(self):
        '''必填字段(deviceId)为空'''
        params = '=81251114&toUserId=1092928237'
        token = Login().login()  # 引用登录
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("操作失败", js['message'])


    def test_deviceunreg_uslose(self):
        '''测试参数不完整，必填参数(toUserId)未传'''
        token = Login().login()  # 引用登录
        params = 'deviceId=81251114'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("操作失败", js['message'])


    def test_deviceunreg_usnull(self):
        '''必填字段(toUserId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'deviceId=81251114&toUserId='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("操作失败", js['message'])


    def test_deviceunreg_uspanull(self):
        '''必填字段(toUserId)为空'''
        token = Login().login()  # 引用登录
        params = 'deviceId=81251114&=1092928237'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("操作失败", js['message'])


    def test_deviceunreg_tokenull(self):
        '''未传入token'''
        params = 'deviceId=81251114&toUserId=1092928237'
        r = self.myhttp1('POST',
                        self.url_path,
                         params
                        # {'deviceId': '81251114','toUserId': 1092928237},

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_deviceunreg_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'deviceId=81251114&toUserId=1092928237'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_deviceunreg_signerror(self):
        '''sign不正确'''
        token = Login().login()  # 引用登录
        params = {'deviceId':'994706','toUserId':'54644930'}
        print params
        r = self.signerror('GET',
                        self.url_path,
                        params,
                        token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])



        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'deviceId':'994706','toUserId':'54644930'})
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + 'e')
        # request.add_header('token', self.token)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'],-2)
        # self.assertIn('拦截请求授权出错',js['message'])

    def test_deviceunreg_noncerror(self):
        '''nonce不正确'''
        token = Login().login()  # 引用登录
        params = {'deviceId':'994706','toUserId':'54644930'}
        print params
        r = self.noncerror('GET',
                        self.url_path,
                        params,
                        token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'deviceId':'994706','toUserId':'54644930'})
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # data = {'data': encoded}
        # payload = urllib.urlencode(data)
        # request = urllib2.Request(self.url, data=payload)
        # request.add_header('nonce', self.nonce + 'e')
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
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_success'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_delose'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_denull'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_depanull'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_uslose'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_usnull'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_uspanull'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_tokenerror'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_tokenull'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_signerror'))
    testunit.addTest(devicedeviceunregTest('test_deviceunreg_noncerror'))



    fp = open('./devicedeviceunreg_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'解绑饭煲（主动解除分享给别人的设备）接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()



