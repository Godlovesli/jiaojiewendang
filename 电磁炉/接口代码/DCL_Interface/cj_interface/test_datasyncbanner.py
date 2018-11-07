#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 15:31
# @Author  : fengguifang
# @File    : test_devicefactory.py
# @Software: PyCharm
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class datasynbannerTest(MyTest):
    '''同步banner图片'''
    url_path = '/v1/data/sync/banner'

    @classmethod
    def setUpClass(cls):
        pass

    def test_datasyncbanner_success(self):
        '''所有参数都传'''
        payload = {'': ''}
        # r = self.cry_myhttp('POST',
        #                  self.url_path,
        #                 payload,
        #                  )
        # print r
        # js = json.loads(r)
        # self.assertEqual(js['code'], 1)
        # self.assertEqual(js['message'], 'success')
