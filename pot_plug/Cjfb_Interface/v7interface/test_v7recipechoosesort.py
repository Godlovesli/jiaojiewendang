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


class recipechoosesortTest(CJMyTest):
    '''排序'''
    url_path = '/v7/recipe/choose/sort'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipechoosesort_success(self):
        '''排序成功'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {'deviceId': self.deviceId,
                         'model':self.model_name,
                         # 'recipeOptions': [{'recipeId':''},{'recipeId':3353},{'recipeId':3454},{'recipeId':3455},{'recipeId':3456},{'recipeId':3457}],  #recipeChooses是收藏对象(我的精选)，recipeOptions设备所见
                         # 'recipeChooses': [{'recipeId': ''},{'recipeId':3353}]} #3473是白菜炖粉条，3353是照烧龙利鱼 这是测试环境的数据
                            'recipeOptions': [{'recipeId':''},{'recipeId':2732},{'recipeId':2718},{'recipeId':2719},{'recipeId':2720},{'recipeId':2721}],  #recipeChooses是收藏对象(我的精选)，recipeOptions设备所见
                            'recipeChooses': [{'recipeId': ''},{'recipeId':2732}]} #3473是白菜炖粉条，3353是照烧龙利鱼 这是预发布环境数据

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("排序成功", js['message'])