#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import unittest
import json
from HTMLTestRunner_cn import HTMLTestRunner
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ricecookscriptfindTest(CJMyTest):
    '''成功查找米烹饪程序'''



    url_path = '/v7/rice/cookscript/find'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecookscriptfind_success(self):
        '''传必填参数'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {
                            'riceId': 24642, 'cookstyleId':'1100' , 'tasteId':'4111',
                            # 'deviceId':'91903314',
                            'deviceId':self.deviceId




                          }
                        )
        # 'riceId': 1, 'cookstyleId':'1100', 'tasteId':'4111',
        print r
        js = json.loads(r)
        # print js
        print "打印烹饪程序：%s"%js['result']['cookscript']['cookcode']
        self.assertEqual(js['state'], 1)
        self.assertIn('成功', js['message'])

