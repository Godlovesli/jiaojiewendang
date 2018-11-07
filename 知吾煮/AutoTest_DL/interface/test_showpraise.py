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

class showPraiseTest(MyTest):
    '''对作品点赞'''
    url_path = '/show/praise'

    @classmethod
    def setUpClass(cls):
        pass

    def test_praise_success(self):
        '''未点赞过的作品进行点赞，点赞成功'''
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
            params = 'showId='+str(showId)
            r = self.myhttp('GET',
                            self.url_path,
                            params,
                            # {'showId':showId},
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn('点赞成功', js['message'])
        else:
            print "请先发表作品"



    def test_praise_yizan(self):
        '''已点赞过的作品进行点赞，提示已点赞'''
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
            params = 'showId=' + str(showId)
            r = self.myhttp('GET',
                            self.url_path,
                            params,
                            # {'showId': showId},
                            token
                            )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], -4)
            self.assertIn('曾经点赞过', js['message'])
        else:
            print "不存在已点赞作品"


    def test_praise_shlose(self):
        '''测试参数不完整，必填参数(showId)未传'''
        token = Login().login()  # 引用登录
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'': ''},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'showId' is not present", js['message'])

    def test_praise_shnull(self):
        '''某个必填字段(showId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'showId='
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'showId': ''},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'showId' is not present", js['message'])


    def test_praise_shpanull(self):
        '''某个必填参数(showId)为空'''
        token = Login().login()  # 引用登录
        params = '=784'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'': '784'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'showId' is not present", js['message'])

    def test_praise_tokennull(self):
        '''未传入token'''
        params = 'showId=784'
        r = self.myhttp1('GET',
                        self.url_path,
                        params,
                        # {'showId': '816'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_praise_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'showId=816'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'showId': '816'},
                        token+ '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_praise_signerror(self):
        '''sign不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId': '818'}
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
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'showId': '816'})
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


    def test_praise_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId': '818'}
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
        # self.url = self.base_url + self.url_path
        # self.signature = generateSignature(self.nonce, "GET", self.url)
        # params = urllib.urlencode({'showId': '816'})
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
    testunit.addTest(showPraiseTest('test_praise_success'))
    testunit.addTest(showPraiseTest('test_praise_yizan'))
    testunit.addTest(showPraiseTest('test_praise_shlose'))
    testunit.addTest(showPraiseTest('test_praise_shnull'))
    testunit.addTest(showPraiseTest('test_praise_shpanull'))
    testunit.addTest(showPraiseTest('test_praise_tokenerror'))
    testunit.addTest(showPraiseTest('test_praise_tokennull'))
    testunit.addTest(showPraiseTest('test_praise_signerror'))
    testunit.addTest(showPraiseTest('test_praise_noncerror'))


    fp = open('./showPraise_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'对作品点赞接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


