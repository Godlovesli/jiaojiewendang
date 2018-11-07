#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipedetailTest(CJMyTest):
    '''食谱详情'''
    url_path = '/v6/recipe/detailByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecookscriptfind_success(self):
        '''传必填参数'''

        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'model': self.model_name, 'recipeId': 256,'language': self.language},
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('成功', js['message'])



#   'model': 'chunmi.cooker.naeg1', 'recipeId': 256,'language': 'english'