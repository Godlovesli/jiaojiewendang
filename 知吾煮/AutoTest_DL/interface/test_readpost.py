#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
from base.mydb import MyDB
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class readpostTest(MyTest):
    '''阅读社区消息'''
    url_path = '/message/read/post'


    @classmethod
    def setUpClass(cls):
        pass

    def test_readpost_success(self):
        '''所有参数都传，阅读成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_message where username='1081'"
        data_count = cursor.execute(sql)
        print data_count
        cursor.scroll(0)
        rows = cursor.fetchone()
        print rows
        mid = rows['id']
        print mid
        if data_count > 0:
            params = 'mid='+str(mid)
            r = self.myhttp('POST',
                            self.url_path,
                            params,
                             token
                             )
            print r
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn( '操作成功',js['message'])
        else:
            print "不存在消息"

    def test_readpost_idbc(self):
        '''不传非必填参数，阅读成功'''
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
        self.assertEqual(js['state'], 1)
        self.assertIn( '操作成功',js['message'])

    def test_readpost_iderror(self):
        '''id格式不正确'''
        token = Login().login()  # 引用登录
        print token
        params = 'mid=one'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token
                             )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn( '操作失败',js['message'])


    def test_readpost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        params = 'mid=2'
        r = self.myhttp('POST',
                        self.url_path,
                        params,
                        token + '1'
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])

    def test_readpost_tokenull(self):
        '''未传入token'''
        params = 'mid=2'
        r = self.myhttp1('POST',
                        self.url_path,
                         params,

                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_readpost_signerror(self):
        '''sign不正确'''
        params ={'mid': '2'}
        print params
        r = self.signerror('POST',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        #
        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'mid': '2'})
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



    def test_readpost_noncerror(self):
        '''nonce不正确'''
        params ={'mid': '2'}
        print params
        r = self.noncerror('POST',
                        self.url_path,
                        params
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -2)
        self.assertIn('拦截请求授权出错', js['message'])


        # self.token = Login().login()  # 引用登录
        # print self.token
        # self.url=self.base_url+self.url_path
        # self.signature = generateSignature(self.nonce, "POST", self.url)
        # params = urllib.urlencode({'mid': '2'})
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
        #

if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(readpostTest('test_readpost_success'))
    testunit.addTest(readpostTest('test_readpost_tokenerror'))
    testunit.addTest(readpostTest('test_readpost_tokenull'))
    testunit.addTest(readpostTest('test_readpost_signerror'))
    testunit.addTest(readpostTest('test_readpost_noncerror'))


    fp = open('./readpostTest_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'阅读社区消息接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()


