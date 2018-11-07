#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 10:23
# @Author  : fengguifang
# @File    : test_v7recipechoosecancel.py
# @Software: PyCharm
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipechoosecancelTest(CJMyTest):
    '''取消收藏'''
    url_path = '/v7/recipe/choose/cancel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipechoosecancel_success(self):
        '''传必填参数'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {'recipeChooses': [{'recipeId': 3473, 'deviceId': 85465933}]}
                         ) #白菜炖粉条
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("取消成功", js['message'])