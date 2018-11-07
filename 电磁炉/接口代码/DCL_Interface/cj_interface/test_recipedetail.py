#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipedetailTest(MyTest):
    '''获取某个模式的详情'''
    url_path = '/v1/recipe/detail'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeapiinfo_success(self):
        '''所有参数都传'''
        payload = {'recipeid': '1', 'deviceid': '53256503'}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        # self.assertIn('success',js['message'])

