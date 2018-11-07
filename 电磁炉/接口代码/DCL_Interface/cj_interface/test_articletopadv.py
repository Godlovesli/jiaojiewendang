#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class articletopadvTest(MyTest):
    '''获取头部Banner'''
    url_path = '/v1/article/topadv'

    @classmethod
    def setUpClass(cls):
        pass

    def test_articletopadv_sysuccess111(self):
        '''所有参数都传'''
        # 53256503
        r = self.myhttp('GET',
                         self.url_path,
                        {'deviceid': self.deviceId, 'type': 6100}     #'language': 'simplified'
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        for i in range(len(js['result'])):
            print js['result'][i]['id']
            print js['result'][i]['title']


