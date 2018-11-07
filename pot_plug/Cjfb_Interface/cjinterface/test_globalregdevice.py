#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 14:35
# @Author  : fengguifang
# @File    : test_globalregdevice.py
# @Software: PyCharm
#coding:utf-8
# __author__ = 'feng'

from base.cjbase import CJMyTest
import json
import urllib, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class globalregdeviceTest(CJMyTest):
    '''注册设备'''
    url_path =  '/v6/device/global/regdevice'

    @classmethod
    def setUpClass(cls):
        pass


    def test_globalregdevice_success(self):
        '''注册饭煲'''
        A={'deviceid': '71820180',
                           'mac': 'F0:B4:29:BE:94:5C',
                           'userId': '54644930',
                           'online': '1',
                           'cityName': 'shanghai',
                           'ownerId': '54644930',
                           'ownerName': 'ff',
                           'modelName': self.model_name
                           }
        r = self.cjmyhttp('POST',
                         self.url_path,
                          {'deviceid': '7182028',
                           'mac': 'F0:B4:29:BE:94:5C',
                           'userId': '54644930',
                           'online': '1',
                           'cityName': 'shanghai',
                           'ownerId': '54644930',
                           'ownerName': 'ff',
                           'modelName': self.model_name

                           },
                         )
        print r
        js = json.loads(r)
        # print type(js)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'注册设备成功', js['message'])
