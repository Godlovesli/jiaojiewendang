#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 17:05
# @Author  : fengguifang
# @File    : test_v7recipechooselist.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class v7recipechooseTest(CJMyTest):
    '''自选精选列表'''
    url_path = '/v7/recipe/choose/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipechoose_success1(self):
        '''精选列表'''
        r = self.cjmyhttp('GET',
                        self.url_path,

                         {'deviceId': self.deviceId, 'model': self.model_name,'language':self.language,'pageno':1,'perpage':50,

                        }
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        for i in range(len(js['result']['jxRecipes'])):
            print js['result']['jxRecipes'][i]['name'],js['result']['jxRecipes'][i]['topRecipe']
            #"topRecipe":false

    def test_recipechoose_success2(self):
        '''自选列表'''
        r = self.cjmyhttp('GET',
                          self.url_path,
                          {'deviceId': self.deviceId, 'model': self.model_name,'language':self.language,'pageno':1,'perpage':10,'zxFlag':'true'}

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        for i in range(len(js['result']['zxRecipes'])):
            print js['result']['zxRecipes'][i]['name'],js['result']['zxRecipes'][i]['topRecipe'],\
                js['result']['zxRecipes'][i]['recipeOptionFlag']

        #返回值多了一个 "topRecipe":true，"topRecipe":false
