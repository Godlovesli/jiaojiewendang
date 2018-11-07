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

class devicefactoryTest(MyTest):
    '''恢复出厂'''
    url_path = '/v1/device/factory/reset/53312514'

    @classmethod
    def setUpClass(cls):
        pass

    def test_managereset_success(self):
        '''所有参数都传'''
        payload = {'': ''}
        r = self.cry_myhttp('POST',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        self.assertEqual(js['message'], '设备已恢复出厂')
