#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 15:31
# @Author  : fengguifang
# @File    : test_devicefactory.py
# @Software: PyCharm
from base.base import MyTest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class datasyncageTest(MyTest):
    '''同步多语言图片'''
    url_path = '/v1/data/sync/recipeImg/multilanguage'

    @classmethod
    def setUpClass(cls):
        pass

    def test_datasyncage_success(self):
        '''所有参数都传'''
        payload = {'': ''}
        print(payload)
        # r = self.cry_myhttp('POST',
        #                  self.url_path,
        #                 payload,
        #                  )
        # print r
        # js = json.loads(r)
        # self.assertEqual(js['code'], 1)
        # self.assertEqual(js['message'], 'success')
