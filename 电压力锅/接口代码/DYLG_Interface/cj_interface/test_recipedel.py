#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecollectdelTest(MyTest):
    '''批量删除自定义'''
    url_path = '/v1/recipe/collect/del'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecollectdel_success(self):
        '''单个删除'''
        payload = {'deviceid': '57381615',
                   'recipeids': 1945

                   }
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)


    def test_recipecollectdel_success1(self):
        '''批量删除'''
        payload = {'deviceid': '57357285',
                   'recipeids': [1405,1406]

                   }
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)


