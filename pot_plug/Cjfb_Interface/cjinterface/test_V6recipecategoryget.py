#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import unittest
import json
import urllib, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecategorygetTest(CJMyTest):
    '''食谱类别'''
    url_path = '/v6/recipe/category/get'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipecollectadd_success(self):
        '''所有字段都传'''
        r = self.cjbujiami('GET',
                        self.url_path,
                         {'language':'en_US'},

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']



