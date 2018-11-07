#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class articletopadv1Test(MyTest):
    '''获取头部Banner'''
    url_path = '/v1/article/topadvByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_articletopadv_sysuccess111(self):
        '''所有参数都传'''
        payload = {'model': self.model, 'type': 6100, 'language': self.language}
        r = self.cry_myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        print type(js)
        self.assertEqual(js['code'],1)
        for i in range(len(js['result'])):
            print js['result'][i]['id']
            print js['result'][i]['title']


