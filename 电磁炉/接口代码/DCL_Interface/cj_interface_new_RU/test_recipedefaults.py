#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 15:43
# @Author  : fengguifang
# @File    : test_recipedefaults.py
# @Software: PyCharm
from base.base import MyTest
import json
import requests
requests.packages.urllib3.disable_warnings()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipedefaultsTest(MyTest):
    '''获取默认模式'''
    url_path = '/v1/recipe/defaults'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipelist_success(self):
        '''非必填参数不传'''
        payload = {'model':self.model,'language': self.language} ## ru_RU en_US es_ES
        r = self.cry_myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']
            self.assertIsNot(js['result'][i]['cookCode'], None)