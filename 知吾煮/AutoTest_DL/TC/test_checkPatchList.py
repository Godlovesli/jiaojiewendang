
# coding:utf-8
# __author__ = 'feng'
from base.V1base import MyTest
from base.mydb import MyDB
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


class checkPatchListTest(MyTest):
    '''IOS取得APP patch包列表'''
    url_path =  '/app/checkPatchList'

    @classmethod
    def setUpClass(cls):
        pass


    def test_checkPatchList_success(self):
        '''release_code传入正确，获取新版成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_app_release where state='2200' and platform='2' ORDER BY id  "
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        release_code = rows['id']
        print release_code
        params= 'release_code='+ str(release_code)+'&platform=2'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        if data_count >1:
            self.assertEqual(js['state'], 1)
            self.assertIn('patches获取成功', js['message'])

        else:
            self.assertEqual(js['state'], -4)
            self.assertIn('未有新版本', js['message'])



    def test_checkPatchList_success2(self):
        '''release_code传入非最新的版本代码时，获取新版成功'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_app_release where state='2200' and platform='1' ORDER BY id  "
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        release_code = rows['id']
        print release_code
        params= 'release_code='+ str(release_code)+'&platform=1'
        print params
        r = self.myhttp('GET',
                        self.url_path,
                        params,

                        )
        print r
        js = json.loads(r)
        if data_count > 1:
            self.assertEqual(js['state'], 1)
            self.assertIn('patches获取成功', js['message'])

        else:
            self.assertEqual(js['state'], -4)
            self.assertIn('未有新版本', js['message'])


#
#     def test_checkPatchList_reno(self):
#         '''必填参数(release_code)的值输入不存在的信息'''
#         params = 'release_code=21238'
#         print params
#         r = self.myhttp('GET',
#                          self.url_path,
#                         params,
#
#                          )
#         print r
#         js = json.loads(r)
#         self.assertEqual(js['state'],-4)
#         self.assertIn("未有新版本",js['message'])
#
#
#     def test_checkPatchList_relose(self):
#         '''测试参数不完整，必填参数(release_code)未传'''
#         params = ''
#         print params
#         r = self.myhttp('GET',
#                         self.url_path,
#                         params,
#
#                         )
#         print r
#         js = json.loads(r)
#         self.assertEqual(js['state'], -4)
#         self.assertIn("'release_code' is not present", js['message'])
#
#
#     def test_checkPatchList_renull(self):
#         '''必填字段(release_code)的值为空'''
#         params= 'release_code='
#         print params
#         r = self.myhttp('GET',
#                          self.url_path,
#                         params,
#
#                          )
#         print r
#         js = json.loads(r)
#         self.assertEqual(js['state'],-4)
#         self.assertIn("parameter 'release_code' is not present",js['message'])
#
#
#
#     def test_checkPatchList_repanull(self):
#         '''必填参数(release_code)为空'''
#         params = 'release_code='
#         print params
#         r = self.myhttp('GET',
#                          self.url_path,
#                         params,
#
#                          )
#         print r
#         js = json.loads(r)
#         self.assertEqual(js['state'],-4)
#         self.assertIn("'release_code' is not present",js['message'])
#
#
#     def test_checkPatchList_signerror(self):
#         '''sign不正确'''
#         self.url=self.base_url+self.url_path
#         self.signature = generateSignature(self.nonce, "GET", self.url)
#         params = urllib.urlencode({'release_code': '256'})
#         print '输入参数：'+params
#         request = urllib2.Request(self.url + '?' + params)
#         request.add_header('nonce',self.nonce)
#         request.add_header('User-Agent','chunmiapp')
#         request.add_header('signature',self.signature+'1')
#         response = urllib2.urlopen(request)
#         result = response.read()
#         print result
#         js = json.loads(result)
#         self.assertEqual(js['state'],-2)
#         self.assertIn('拦截请求授权出错',js['message'])
#
#
#     def test_checkPatchList_noncerror(self):
#         '''nonce不正确'''
#         self.url=self.base_url+self.url_path
#         self.signature = generateSignature(self.nonce, "GET", self.url)
#         params = urllib.urlencode({'release_code': '256'})
#         print '输入参数：'+params
#         request = urllib2.Request(self.url + '?' + params)
#         request.add_header('nonce',self.nonce+'1')
#         request.add_header('User-Agent','chunmiapp')
#         request.add_header('signature',self.signature)
#         response = urllib2.urlopen(request)
#         result = response.read()
#         print result
#         js = json.loads(result)
#         self.assertEqual(js['state'],-2)
#         self.assertIn('拦截请求授权出错',js['message'])
#
#
# if __name__ == '__main__':
#     # unittest.main()
#
#     testunit = unittest.TestSuite()
#     testunit.addTest(checknewTest('test_checknew_success'))
#     testunit.addTest(checknewTest('test_checknew_renew'))
#     testunit.addTest(checknewTest('test_checknew_reno'))
#     testunit.addTest(checknewTest('test_checknew_relose'))
#     testunit.addTest(checknewTest('test_checknew_renull'))
#     testunit.addTest(checknewTest('test_checknew_repanull'))
#     # testunit.addTest(checknewTest('test_checknew_reerror'))
#     # testunit.addTest(checknewTest('test_checknew_rec'))
#     # testunit.addTest(checknewTest('test_checknew_ree'))
#     testunit.addTest(checknewTest('test_checknew_signerror'))
#     testunit.addTest(checknewTest('test_checknew_noncerror'))
#
#     fp = open('./checknew.html', 'wb')
#     runner = HTMLTestRunner(stream=fp,
#                             title=u'检查更新接口测试报告',
#                             description=u'用例执行情况：')
#     runner.run(testunit)
#     fp.close()
