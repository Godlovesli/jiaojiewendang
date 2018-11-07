#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class officialByModelTest(MyTest):
    '''获取官方模式'''
    url_path = '/v1/recipe/officialByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_officialByModel_success(self):
        '''所有参数都传'''
        payload = {'model': 'chunmi.ihcooker.hk1', 'pageno': 1, 'perpage': '20', 'language': 'zh_hk'}
        r = self.cry_myhttp('GET',
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



