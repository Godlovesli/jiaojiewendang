#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.mydb import MyDB
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class showdetailTest(MyTest):
    '''用户作品详情'''
    url_path = '/show/detail/'

    @classmethod
    def setUpClass(cls):
        pass

    def test_showdetail_success1(self):
        '''显示用户作品详情成功'''
        token = Login().login()  # 引用登录
        r = self.nosign('GET',
                         self.url_path,
                         {'': ''},
                         token
                         )
        print r

    def test_showdetail_success(self):
        '''所有参数都传'''

        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from mipot_recipe_show"
        data_count = cursor.execute(sql)
        print data_count
        if data_count > 0:
            cursor.scroll(0)
            rows = cursor.fetchone()
            print rows
            id = rows['id']
            print id
            self.url_path = self.url_path + str(id)
            params = ''
            r = self.nosign('GET',
                             self.url_path,
                             params
                             )
            print r



    def test_showdetail_tokennull(self):
        '''未传入token'''
        params = ''
        self.url_path = self.url_path + str(750)
        token = Login().login()  # 引用登录
        r = self.nosign('GET',
                        self.url_path,
                        params,
                        token
                        )
        print r


    def test_showdetail_tokenerror(self):
        '''token错误'''
        params = ''
        self.url_path = self.url_path + str(750)
        token = Login().login()  # 引用登录
        r = self.nosign('GET',
                        self.url_path,
                        params,
                        token+'34e'
                        )
        print r



if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(showdetailTest('test_showdetail_success'))
    testunit.addTest(showdetailTest('test_showdetail_tokennull'))
    testunit.addTest(showdetailTest('test_showdetail_tokenerror'))


    fp = open('./showdetail_result.html', 'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'用户作品详情接口测试报告',
                            description = u'用例执行情况：')
    runner.run(testunit)
    fp.close()





