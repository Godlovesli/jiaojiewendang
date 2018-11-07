#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecreateTest(MyTest):
    '''创建一个自定义模式'''
    url_path = '/v1/recipe/collect/create'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecreate_success(self):
        '''创建一个自定义模式'''
        payload = {'deviceid': '53256503',
                   'name': 'testtest',
                   'firePower': 30,
                   'duration': 20
                   }
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)


    def test_recipecreate_success1(self):
        '''创建一个自定义模式'''
        payload= {'deviceid': '53256503', 'name': 'test','duration': 20,'temperature':120,'firePower': 0,}
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)

    def test_recipecreate_success2(self):
        '''创建一个自定义模式'''
        #name=%E5%8F%AF%E5%8A%B2%E5%8F%AF%E5%8A%B2&firePower=0&duration=60&temperature=135&deviceid=53256485&language=’
        payload= {'deviceid': '53256485', 'name': 'test','duration': 60,'firePower': 0,'temperature':120}
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)