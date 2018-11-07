#coding=utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 13:15
# @Author  : fengguifang
# @File    : test_v7recipequery.py
# @Software: PyCharm


# from base.cjbase import CJMyTest
from base.cjbase1 import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7recipequeryTest(CJMyTest):
    '''更多食谱，根据食谱类别和关键字进行查询'''
    url_path = '/v7/recipe/people/query'

    @classmethod
    def setUpClass(cls):
        pass
    def recipelist(self):
        '''获取食谱列表'''
        params='language=&model=chunmi.cooker.eh1'  #model=chunmi.cooker.k1pro1
        r = self.cjmyhttpjs('GET',
                            self.url_path,
                            params
                            )

        print r
        js = json.loads(r)
        print  js
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']

    def test_recipequery_success(self):
        '''传必填参数'''
        params = 'params=大酱汤&deviceId=57384129&pageno=1&perpage=10&categoryId=&model=chunmi.cooker.eh1&language='


        r = self.cjmyhttpjs('GET',
                        self.url_path,
                        params


                         )

        print r
        js = json.loads(r)

        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['name'],js['result'][i]['collectFlag']