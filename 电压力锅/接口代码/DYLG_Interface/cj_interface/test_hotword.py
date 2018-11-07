#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipehotwordTest(MyTest):
    '''热搜'''
    url_path = '/v1/recipe/hotword/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_hotword_success(self):
        '''所有参数都传'''
        payload = {'': ''}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )

        js = json.loads(r)
        self.assertEqual(js['code'],1)
        for i in range(len(js['result'])):
            print js['result'][i]['content']

        # self.assertIn('success',js['message'])


