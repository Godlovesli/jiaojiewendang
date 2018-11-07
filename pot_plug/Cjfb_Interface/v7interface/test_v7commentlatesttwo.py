#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 11:25
# @Author  : fengguifang
# @File    : test_v7commentlatesttwo.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7commentlatesttwoTest(CJMyTest):
    '''食谱详情页获取最新两条评论'''
    url_path = '/v7/recipe/comment/latesttwo'

    @classmethod
    def setUpClass(cls):
        pass
    def test_v7commentadd_success(self):
        '''所有参数都传'''
        r = self.cjmyhttpjs('GET',
                        self.url_path,
                        {'recipeId':3474}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])