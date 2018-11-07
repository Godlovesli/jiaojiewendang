#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipeapiinfoTest(MyTest):
    '''获取食谱详情'''
    url_path = '/v1/recipe/web/apiinfo/1830'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeapiinfo_success(self):
        '''所有参数都传'''
        payload = {'deviceid': '57357285'}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        # self.assertIn('success',js['message'])


    def test_recipeapiinfo_success1(self):
        '''所有参数都传'''
        payload = {'': ''}
        r = self.myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertIn('success', js['message'])