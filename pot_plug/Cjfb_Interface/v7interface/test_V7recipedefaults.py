#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 17:01
# @Author  : zhouli
# @File    : test_defaultrecipes.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipesDefaults(CJMyTest):
    '''获取默认模式'''
    url_path =  '/v7/recipe/defaults'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipesDefaults_success(self):
        '''获取默认模式'''
        r = self.cjmyhttp('GET',
                         self.url_path,
                         {'model': self.model_name,'language': self.language},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        # self.assertIn(u'操作成功',js['message'] )
        self.assertTrue(u'操作成功'==js['message'])
        print "打印默认模式的个数：%s"%js['result']
        for i in range(len(js['result'])):
            print js['result'][i]['recipeId'],js['result'][i]['name']