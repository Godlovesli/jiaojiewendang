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

class collectdevicegetTest(MyTest):
    '''设备收藏的食谱(替换原/literecipe/recipebydevice接口)'''
    url_path = '/v1/recipe/collect/device/get'


    @classmethod
    def setUpClass(cls):
        pass

    def test_collectdeviceget_success(self):
        '''获取成功'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_device_useinfo where userId='54644930'"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        deviceId = rows['deviceId']
        print deviceId
        params = 'pageno=1&deviceId='+str(deviceId)
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'pageNo': 1, 'deviceId':deviceId},
                         token
                         )
        print r
        if data_count>0:
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn( '获取菜谱列表成功',js['message'])
            print len(js['result'])
            for i in range(len(js['result'])):
                print js['result'][i]['name']
        else:
            print "不存在收藏食谱"

    def test_collectdeviceget_plose(self):
        '''pageNo未传'''
        token = Login().login()  # 引用登录
        print token
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT * from mipot_device_useinfo where userId='54644930'"
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        deviceId = rows['deviceId']
        print deviceId
        params = 'deviceId=' + str(deviceId)
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # { 'deviceId':deviceId},
                         token
                         )
        print r
        if data_count>0:
            js = json.loads(r)
            self.assertEqual(js['state'], 1)
            self.assertIn( '获取菜谱列表成功',js['message'])
        else:
            print "不存在收藏食谱"


    def test_collectdeviceget_delose(self):
        '''deviceId未传，获取失败'''
        token = Login().login()  # 引用登录
        print token
        params = 'pageNo=2'
        r = self.myhttp('GET',
                        self.url_path,
                        params,
                        # {'pageNo': 2},
                        token
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -4)
        self.assertIn("Required Long parameter 'deviceId' is not present", js['message'])

