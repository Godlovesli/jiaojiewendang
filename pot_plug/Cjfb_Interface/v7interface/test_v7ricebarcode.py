#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 13:48
# @Author  : fengguifang
# @File    : test_v7ricebarcode.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7ricebarcodeTest(CJMyTest):
    '''扫描条形码添加米种'''
    url_path = '/v7/rice/barcode'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricebarcode_success(self):
        '''传必填参数'''
        r = self.cjmyhttpjs('GET',
                        self.url_path,
                        {
                        'barCode':self.barcode,
                        'deviceId': self.deviceId,
                        'barCode':self.barcode,

                        'language':self.language,

                        }
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
