#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import unittest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class recipehintTest(CJMyTest):
    '''食谱关键字匹配'''
    url_path = '/v6/recipe/hint/getByModel'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipehint_success(self):
        '''所有字段都传'''
        r = self.cjbujiami('GET',
                        self.url_path,
                           {'model': self.model_name, 'perpage': 500, 'pageno': 1, 'language':self.language,
                            'content': 'Tom'},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            if js['result'][i]['name'] != None:
                print js['result'][i]['id']
                print js['result'][i]['name']

