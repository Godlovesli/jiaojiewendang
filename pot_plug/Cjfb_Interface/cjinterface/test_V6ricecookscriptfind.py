#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 14:03
# @Author  : fengguifang
# @File    : test_V6ricecookscriptfind.py
# @Software: PyCharm
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ricecookscriptfindTest(CJMyTest):
    '''查找米烹饪程序'''
    url_path = '/v6/ricecookscript/find'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecookscriptfind_success(self):
        '''传必填参数'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'riceid': 1, 'cookstyleid':'1100' , 'tasteid':'4111','deviceid':'91903314','language': 'ja_JP'},
                        )
        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['state'], 1)
        self.assertIn('成功', js['message'])
