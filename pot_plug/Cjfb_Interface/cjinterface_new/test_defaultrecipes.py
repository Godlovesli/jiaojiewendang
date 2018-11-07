#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 17:01
# @Author  : fengguifang
# @File    : test_defaultrecipes.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class defaultRecipesTest(CJMyTest):
    '''获取用户收藏菜谱'''
    url_path =  '/v6/literecipe/defaultRecipes'


    @classmethod
    def setUpClass(cls):
        pass


    def test_defaultRecipes_success(self):
        '''获取默认食谱'''
        r = self.cjmyhttp('GET',
                         self.url_path,
                         {'model': self.model_name,'language': self.language},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取菜谱列表成功', js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipeId'],js['result'][i]['name']