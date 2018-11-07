#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 15:32
# @Author  : fengguifang
# @File    : test_articletopadvtopadvByModel.py
# @Software: PyCharm
from base.base import MyTest
import requests
requests.packages.urllib3.disable_warnings()
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class articletopadv1Test(MyTest):
    '''获取头部Banner'''
    url_path = '/v1/article/topadvByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_articletopadv_sysuccess111(self):
        '''所有参数都传'''
        payload = {'model': self.model, 'type': 6100, 'language': self.language}# ru_RU en_US es_ES
        r = self.cry_myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        for i in range(len(js['result'])):

            print ("头部banner id ：%d" % js['result'][i]['id'])
            print("头部banner title ：%d"%js['result'][i]['title'])


