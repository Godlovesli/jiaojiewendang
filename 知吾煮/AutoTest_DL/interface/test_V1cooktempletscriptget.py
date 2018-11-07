#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.base import MyTest
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


class cooktempletgetTest(MyTest):
    '''获取模板烹饪程序'''
    # url_path = '/v4/article/topadv'
    url_path = '/v1/recipe/cook/templet/script/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_cooktempletget_success11(self):
        self.base_url = 'http://10.0.10.100:17002'
        self.url = self.base_url + '/v1/recipe/cook/templet/script/get'
        self.nonce = generateNonce()
        self.key = getSessionSecurity(self.nonce)
        self.signature = generateSignature(self.nonce, 'GET', self.url)
        self.headers = {'nonce': self.nonce,
                        'User-Agent': 'chunmiapp',
                        'signature': self.signature

                        }
        params = {'templetid': 10, 'deviceid': 45423531}
        payload1 = urllib.urlencode(params)
        print payload1
        encoded = encryptAES(payload1, self.key)
        data = {'data': encoded}
        print data
        payload = urllib.urlencode(data)
        print payload
        r = requests.get(self.url, params=payload,  headers=self.headers)
        print r
        code =r.status_code
        print code
        result = r.text.encode()
        print result
        s = decryptAES(result, self.key)
        print s
        js = json.loads(s)
        self.assertEqual(js['state'], 1)
        self.assertIn('get recipecooktempletscript success', js['message'])

    def test_cookscriptget_sysuccess(self):
        '''所有参数都传'''
        # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
        db = MyDB().getCon()
        cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "SELECT recipe_cooktemplet_id,dmg_id  FROM mipot_recipe_cook_templet_script " \
              "WHERE recipe_cooktemplet_id IN (SELECT id FROM mipot_recipe_cook_templet WHERE state = 2200) "
        data_count = cursor.execute(sql)
        print data_count
        rows = cursor.fetchone()
        print rows
        templetid = rows['recipe_cooktemplet_id']
        dmgid=rows['dmg_id']
        # params={'templetid':templetid,'deviceid':dmgid}
        params = 'templetid='+str(10)+'&deviceid='+str(45423531)
        print params
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],1)
        self.assertIn("get recipecooktempletscript success",js['message'])

    def test_cookscriptget_tpidnull(self):
        '''templetid的值为空'''
        params={'templetid':'','deviceid':1083258}
        print params
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],-4)
        self.assertIn("parameter 'templetid' is not present",js['message'])


    def test_cookscriptget_tpidno(self):
        '''templetid未传'''
        params='deviceid=1083258'
        print params
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],-4)
        self.assertIn("parameter 'templetid' is not present",js['message'])


    def test_cookscriptget_dmidnull(self):
        '''dmgid的值为空'''
        params = 'templetid=15&deviceid='
        # params={'templetid':'15','deviceid':''}
        print params
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],-4)
        self.assertIn("parameter 'deviceid' is not present",js['message'])


    def test_cookscriptget_dmidno(self):
        '''dmgid未传'''
        params = 'templetid=15'
        # params={'templetid':'15'}
        print params
        r = self.myhttp('GET',
                         self.url_path,
                        params,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'],-4)
        self.assertIn("parameter 'deviceid' is not present",js['message'])


    def test_cookscriptget_signerror(self):
        '''sign不正确'''
        params = {'templetid': '15','deviceid':1083258}
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
        # params = {'templetid':15,'deviceid':1083258}
        # params = urllib.urlencode(params)
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce)
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature + '1')
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])

    def test_cookscriptget_noncerror(self):
        '''nonce不正确'''
        params = {'templetid': '15','deviceid':1083258}
        print params
        r = self.noncerror('GET',
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
        # params = {'templetid':15,'deviceid':1083258}
        # params = urllib.urlencode(params)
        # print '传入的参数:' + params
        # encoded = encryptAES(params, self.key)
        # datas = {'data': encoded}
        # payload = urllib.urlencode(datas)
        # url2 = self.url + '?' + payload
        # request = urllib2.Request(url2)
        # request.add_header('nonce', self.nonce + '1')
        # request.add_header('User-Agent', 'chunmiapp')
        # request.add_header('signature', self.signature)
        # response = urllib2.urlopen(request)
        # result = response.read()
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['state'], -2)
        # self.assertIn('拦截请求授权出错', js['message'])