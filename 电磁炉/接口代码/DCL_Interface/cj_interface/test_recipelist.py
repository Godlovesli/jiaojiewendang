#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipelistTest(MyTest):
    '''获取更多食谱'''
    url_path = '/v1/recipe/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipelist_success(self):
        '''非必填参数不传'''
        # payload = {'deviceid': self.deviceId, 'pageno':1,'perpage': 100, 'keyword': '懒人', 'categoryid': '', 'language': '' }
        payload = {'deviceid': self.deviceId, 'pageno': 1, 'perpage': 500,
                   'language': ''}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']
            self.assertIsNot(js['result'][i]['cookCode'],None)

    def test_recipelist_success1(self):
        '''非必填参数不传'''
        payload = {'deviceid': '53256503', 'pageno': 1, 'perpage': 100, 'keyword': '松饼', 'categoryid': '3',
                       'language': ''}
        r = self.myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']



