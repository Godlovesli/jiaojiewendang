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

class cancelPraiseTest(MyTest):
    '''取消点赞'''
    url_path = '/show/cancelPraise'

    @classmethod
    def setUpClass(cls):
        pass

    def test_cpraise_success(self):
        '''已点赞过的作品进行取消点赞，取消成功'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_recipe_show where id in(select A.id from mipot_recipe_show A,mipot_recipe_show_praise B  \
              where a.id =b.recipe_show_id and b.user_id='1081')"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            print showId
            params = 'showId='+str(showId)
            r = self.myhttp('GET',
                            self.url_path,
                            params,
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('取消点赞成功', js['message'])
        else:
            print "不存在点赞记录"

    def test_cpraise_nozan(self):
        '''未点赞过的作品进行点赞'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_recipe_show where id not in(select A.id from mipot_recipe_show A,mipot_recipe_show_praise B  \
               where a.id =b.recipe_show_id and b.user_id='1081')"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['id']
            print showId
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                             self.url_path,
                             params,
                             token
                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('取消点赞成功', js['message'])
        else:
            print "不存在未点赞记录"


    def test_cpraise_shlose(self):
        '''测试参数不完整，必填参数(showId)未传'''
        token = Login().login()  # 引用登录
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'showId' is not present", js['message'])


    def test_cpraise_shnull(self):
        '''某个必填字段(showId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'showId='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'showId' is not present", js['message'])



    def test_cpraise_shpanull(self):
        '''某个必填参数(showId)为空'''
        token = Login().login()  # 引用登录
        params = '=784'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'showId' is not present", js['message'])

    def test_cpraise_tokennull(self):
        '''未传入token'''
        params = 'showId=784'
        r = self.myhttp1('GET',
                        self.url_path,
                         params

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_cpraise_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'showId=784'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        token+ 'ee'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_cpraise_signerror(self):
        '''sign不正确'''
        token = Login().login()  # 引用登录
        params = {'showId': '784'}
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



        #
        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'showId': '717'})
        # request = urllib2.Request(self.url + '?' + params)
        # print request
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


    def test_cpraise_noncerror(self):
        '''nonce不正确'''
        token = Login().login()  # 引用登录
        params = {'showId': '784'}
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
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'showId': '717'})
        # request = urllib2.Request(self.url + '?' + params)
        # print request
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
    testunit.addTest(cancelPraiseTest('test_cpraise_success'))
    testunit.addTest(cancelPraiseTest('test_cpraise_nozan'))
    testunit.addTest(cancelPraiseTest('test_cpraise_shlose'))
    testunit.addTest(cancelPraiseTest('test_cpraise_shnull'))
    testunit.addTest(cancelPraiseTest('test_cpraise_shpanull'))
    testunit.addTest(cancelPraiseTest('test_cpraise_tokenerror'))
    testunit.addTest(cancelPraiseTest('test_cpraise_tokennull'))
    testunit.addTest(cancelPraiseTest('test_cpraise_signerror'))
    testunit.addTest(cancelPraiseTest('test_cpraise_noncerror'))


    fp = open('./cancelPraise_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'取消点赞接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


