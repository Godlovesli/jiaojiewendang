#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 11:38
# @Author  : fengguifang
# @File    : v7recipecategory.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import unittest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7recipecategoryTest(CJMyTest):
    '''获取菜谱的类别'''
    url_path = '/v7/recipe/category/get'

    @classmethod
    def setUpClass(cls):
        pass

    @unittest.skip(u"强制跳过示例")

    def test_recipecategory_success(self):
        '''所有参数都传'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'language':self.language}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']
