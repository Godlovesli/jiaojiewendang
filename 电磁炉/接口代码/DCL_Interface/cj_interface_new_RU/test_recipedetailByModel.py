#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 15:44
# @Author  : fengguifang
# @File    : test_recipedetailByModel.py
# @Software: PyCharm
from base.base import MyTest
import json
import requests
requests.packages.urllib3.disable_warnings()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class recipedetailTest(MyTest):
    '''获取某个模式的详情'''
    url_path = '/v1/recipe/detailByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeapiinfo_success(self):
        '''所有参数都传'''
        payload = {'recipeid': '4','model': self.model,'language':self.language}## ru_RU en_US es_ES
        r = self.cry_myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        self.assertIn('success',js['message'])