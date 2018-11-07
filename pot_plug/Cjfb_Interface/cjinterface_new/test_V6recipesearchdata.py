#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import unittest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class recipesearchdataByModelTest(CJMyTest):
    '''食谱列表'''
    url_path = '/v6/recipe/searchdataByModel'


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipesearchdata_success(self):
        '''所有字段都传'''
        r = self.cjbujiami('GET',
                        self.url_path,
                           {'model': self.model_name, 'perpage': 500, 'pageno': 1, 'language': self.language, 'name': '',
                            'type': ''},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 0)
        print "食谱数量：%d"%len(js['result'])
        for i in range(len(js['result'])):
            if js['result'][i]['name'] != None:
                print js['result'][i]['recipeId']
                print js['result'][i]['name']