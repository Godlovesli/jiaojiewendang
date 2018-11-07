#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 15:49
# @Author  : fengguifang
# @File    : test_recipeofficialByModel.py
# @Software: PyCharm
from base.base import MyTest
import json
import requests
requests.packages.urllib3.disable_warnings()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class officialByModelTest(MyTest):
    '''获取官方模式'''
    url_path = '/v1/recipe/officialByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_officialByModel_success(self):
        '''所有参数都传'''
        payload = {'model': self.model, 'pageno': 1, 'perpage': '20', 'language': self.language}## ru_RU en_US es_ES
        r = self.cry_myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        print "官方模式的数量：%d"%len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']
            self.assertIsNot(js['result'][i]['cookCode'],None)
