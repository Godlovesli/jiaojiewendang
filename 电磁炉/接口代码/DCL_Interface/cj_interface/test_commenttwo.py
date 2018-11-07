#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class commenttwoTest(MyTest):
    '''获取最新评论(2条)'''
    url_path = '/v1/recipecomment/toptwo'

    @classmethod
    def setUpClass(cls):
        pass

    def test_commenttwo_success(self):
        '''所有参数都传'''
        payload = {'recipeid': '3495'}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['id']


