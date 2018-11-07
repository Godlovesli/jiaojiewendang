#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
requests.packages.urllib3.disable_warnings()

class recipeapiinfoTest(MyTest):
    '''获取食谱详情'''
    url_path = '/v1/recipe/web/apiinfoByModel/16409'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeapiinfo_success(self):
        '''所有参数都传'''
        payload = {'model': 'chunmi.ihcooker.exp1', 'language': 'en_US'}
        r = self.cry_myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        # self.assertIn('success',js['message'])




