#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
from base.mydb import MyDB
import requests
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class showReviewTest(MyTest):
    '''发表作品评论或回复评论'''
    url_path = '/v1/show/review'

    @classmethod
    def setUpClass(cls):
        pass


    def test_review_success(self):
        '''所有参数都传，发表作品评论或回复评论'''
        token = Login().login()  # 引用登录
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show_comment"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['recipe_show_id']
            parentId = rows['id']
            print showId
            params = 'content=test&showId='+str(showId)+'&parentId='+str(parentId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'showId': showId, 'content': 'test', 'parentId':parentId},
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('回复成功', js['message'])
        else:
            print "请先发表作品评论"


    def test_review_pa(self):
        '''只传必填参数都传，发表作品评论或回复评论'''
        token = Login().login()  # 引用登录
        # token = 'YTk2OGZjODJkYTNhMzA1ZGNjODhiMzJjMDhkOGQwMzI='
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_recipe_show_comment"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            rows = cursor.fetchone()
            print rows
            showId = rows['recipe_show_id']
            print showId
            params = 'content=test&showId=' + str(showId)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                            # {'showId': 695, 'content': '好'},
                            token
                            )
            print r
            js = json.loads(r)
            print js
            self.assertEqual(js['state'], 1)
            self.assertIn('回复成功', js['message'])
        else:
            print "请先发表作品评论"


    def test_review_shlose(self):
        '''测试参数不完整，某个必填参数(showId)未传'''
        token = Login().login()  # 引用登录
        params = 'content=test'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # { 'content': 'test'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'recipe_show_id' cannot be null", js['message'])

    def test_review_colose(self):
        '''测试参数不完整，某个必填参数(content)未传'''
        token = Login().login()  # 引用登录
        params = 'showId=784'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': 784},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'content' cannot be null", js['message'])


    def test_review_shnull(self):
        '''某个必填字段(showId)的值为空'''
        token = Login().login()  # 引用登录
        params = 'showId=&content=test'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId':'','content': 'test'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'recipe_show_id' cannot be null", js['message'])


    def test_review_conull(self):
        '''某个必填字段(content)的值为空'''
        token = Login().login()  # 引用登录
        params = 'showId=784&content='
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': 784,'content':''},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'content' cannot be null", js['message'])


    def test_review_shpanull(self):
        '''某个必填字段(showId)为空'''
        token = Login().login()  # 引用登录
        params = '=784&content=test'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'': '784', 'content': 'test'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'recipe_show_id' cannot be null", js['message'])


    def test_review_copanull(self):
        '''某个必填字段(content)为空'''
        token = Login().login()  # 引用登录
        params = 'showId=784&=test'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': 784, '': 'test'},
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("'content' cannot be null", js['message'])


    def test_review_tokennull(self):
        '''未传入token'''
        params = 'showId=784&content=test'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,
                        # {'showId': '818', 'content': 'test123'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_review_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'showId=784&content=test'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        # {'showId': '818', 'content': 'test123'},
                        token+ '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_review_signerror(self):
        '''签名不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId': '818', 'content': 'test123'}
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
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'showId': '818', 'content': 'test123'})
        # encoded = encryptAES(params, self.key)
        # data = {"data": encoded}
        # payload = urllib.urlencode(data)
        # headers = {'nonce': self.nonce,
        #            'User-Agent': 'chunmiapp',
        #            'signature': self.signature + 'e'}  # 签名不正确
        # request = urllib2.Request(self.url, data=payload, headers=headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_review_noncerror(self):
        '''nonce不正确'''
        self.token = Login().login()  # 引用登录
        print self.token
        params ={'showId': '818', 'content': 'test123'}
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
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'showId': '818', 'content': 'test123'})
        # encoded = encryptAES(params, self.key)
        # data = {"data": encoded}
        # payload = urllib.urlencode(data)
        # headers = {'nonce': self.nonce + 'e',  # nonce不正确
        #            'User-Agent': 'chunmiapp',
        #            'signature': self.signature}
        # request = urllib2.Request(self.url, data=payload, headers=headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])


#
# if __name__ == '__main__':
#     #unittest.main()
#
#     testunit = unittest.TestSuite()
#     testunit.addTest(showReviewTest('test_review_success'))
#     testunit.addTest(showReviewTest('test_review_pa'))
#     testunit.addTest(showReviewTest('test_review_shlose'))
#     testunit.addTest(showReviewTest('test_review_colose'))
#     testunit.addTest(showReviewTest('test_review_shnull'))
#     testunit.addTest(showReviewTest('test_review_conull'))
#     testunit.addTest(showReviewTest('test_review_shpanull'))
#     testunit.addTest(showReviewTest('test_review_copanull'))
#     testunit.addTest(showReviewTest('test_review_tokenerror'))
#     testunit.addTest(showReviewTest('test_review_tokennull'))
#     testunit.addTest(showReviewTest('test_review_signerror'))
#     testunit.addTest(showReviewTest('test_review_noncerror'))
#
#
#     fp = open('./showReview_result.html', 'wb')
#     runner = HTMLTestRunner(stream = fp,
#                             title = u'发表作品评论或回复评论接口测试报告',
#                             description = u'用例执行情况：')
#     runner.run(testunit)
#     fp.close()





