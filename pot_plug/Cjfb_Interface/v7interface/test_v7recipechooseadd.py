#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 10:02
# @Author  : fengguifang
# @File    : test_v7recipechooseadd.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipechooseaddTest(CJMyTest):
    '''添加收藏'''
    url_path = '/v7/recipe/choose/add'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipechooseadd_success(self):
        '''传必填参数'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {'deviceId':self.deviceId,
                        'recipeId':'2732'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("收藏成功", js['message'])

    def test_recipechooseadd_success1(self):
        '''已收藏的食谱'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {'deviceId':self.deviceId,'recipeId':'2732'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn("已收藏，无需再收藏", js['message'])