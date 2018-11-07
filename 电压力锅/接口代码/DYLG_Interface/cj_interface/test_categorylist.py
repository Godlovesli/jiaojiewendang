#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class categorylistTest(MyTest):
    '''获取食谱分类列表'''
    url_path = '/v1/recipe/category/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_categorylist_success(self):
        '''所有必填字段都传'''
        payload = {'': ''}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['name']
            print js['result'][i]['id']


