#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import unittest
import json
import urllib, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class recipequerygetTest(CJMyTest):
    '''大家都在搜接口'''
    url_path = '/v6/recipe/people/query/getByModel'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipequeryget_success(self):
        '''所有字段都传'''
        r = self.cjbujiami('GET',
                        self.url_path,
                           {'model': self.model_name, 'language':self.language},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( 'success',js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['content']

