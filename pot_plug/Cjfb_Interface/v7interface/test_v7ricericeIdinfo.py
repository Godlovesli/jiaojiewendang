#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 10:5
# @Author  : zhouli
# @File    : test_v7ricelist.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7ricelistTest(CJMyTest):
    '''米种详情'''
    url_path = '/v7/rice/1/info'

    @classmethod
    def setUpClass(cls):
        pass

    def test_riceinfo_success(self):
        '''查看米详情，传必填参数'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'riceId': 1,'language': self.language}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
