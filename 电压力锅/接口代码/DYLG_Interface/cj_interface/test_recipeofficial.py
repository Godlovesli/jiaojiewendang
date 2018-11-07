#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipeofficialTest(MyTest):
    '''获取官方模式'''
    url_path = '/v1/recipe/official'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipelist_success(self):
        '''传所有参数'''
        payload = {'deviceid': '57379662', 'pageno': 1, 'perpage': '50'}
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

    def test_recipelist_success1(self):
        '''非必填参数不传'''
        payload = {'': ''}
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


    def test_recipelist_success2(self):
        '''非第一页'''
        payload = { 'pageno': 2, 'perpage': '5'}
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