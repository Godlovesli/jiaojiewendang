#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 9:53
# @Author  : fengguifang
# @File    : test_v7ricedel.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ricecollectdelTest(CJMyTest):
    '''删除用户添加的米种'''
    url_path = '/v7/rice/del'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecollectdel_success(self):
        '''所有参数都传'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {
                                # 'deviceId': 57387733,'rices':[{'id':'56853'}]
                                'deviceId': self.deviceId, 'rices': [{'id': '24641'}]


                         }
                         )
        print r
        js = json.loads(r)
        print type(js)
        self.assertEqual(js['state'], 1)
        self.assertIn("删除成功", js['message'])