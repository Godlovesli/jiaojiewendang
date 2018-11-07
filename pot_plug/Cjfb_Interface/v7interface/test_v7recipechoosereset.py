#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 10:54
# @Author  : fengguifang
# @File    : test_v7recipechoosesort.py
# @Software: PyCharm
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipechooseresetTest(CJMyTest):
    '''排序'''
    url_path = '/v7/recipe/choose/reset'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipechoosereset_success(self):
        '''重置成功'''
        r = self.cjmyhttp(
                        'POST',
                        self.url_path,
                        {'deviceId': self.deviceId, 'model': self.model_name
                         }
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("重置成功", js['message'])
