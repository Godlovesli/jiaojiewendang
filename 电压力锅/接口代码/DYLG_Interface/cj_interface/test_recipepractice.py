#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipepracticeTest(MyTest):
    '''选取做法'''
    url_path = '/v1/recipe/practice/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipepractice_success(self):
        '''所有参数都传'''
        payload = {'ingredientid': '1'}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        # self.assertIn('success',js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']
            print js['result'][i]['id']


