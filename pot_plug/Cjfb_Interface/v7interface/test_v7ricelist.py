#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 13:38
# @Author  : fengguifang
# @File    : test_v7ricelist.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7ricelistTest(CJMyTest):
    '''米种列表'''
    url_path = '/v7/rice/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricelist_success(self):
        '''传必填参数'''
        r = self.cjmyhttpjs('GET',
                        self.url_path,
                        {'deviceid': self.deviceId,'language': self.language,'pageno':1,'perpage':100}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['id'],js['result'][i]['name']