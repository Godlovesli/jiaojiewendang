#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipepracticeTest(MyTest):
    '''选取口感'''
    url_path = '/v1/recipe/texture/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipetexture_success(self):
        '''所有参数都传'''
        payload = {'ingredientid':1,'practiceid':6}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        # self.assertIn('success',js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']
            print js['result'][i]['id']
        return js['result'][i]['id']


