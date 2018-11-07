#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class manageropTest(MyTest):
    '''设置收藏'''
    url_path = '/v1/recipe/manager/op'

    @classmethod
    def setUpClass(cls):
        pass

    def test_managerop_success(self):
        '''所有参数都传'''
        payload = {'deviceid': '57357285', 'recipeid': 1888, 'flag': 1}
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)


    def test_managerop_success1(self):
        '''所有参数都传'''
        payload = {'deviceid': '57381615', 'recipeid': 1888, 'flag': 0}
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)

