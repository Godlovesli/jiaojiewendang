#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
requests.packages.urllib3.disable_warnings()
class articletopadv1Test(MyTest):
    '''获取头部Banner'''
    url_path = '/v1/article/topadv'

    @classmethod
    def setUpClass(cls):
        pass

    def test_articletopadv_sysuccess111(self):
        '''所有参数都传'''
        r = self.myhttp('GET',
                         self.url_path,
                        {'deviceid': '57357285', 'type': 6100,'language':''}     #'language': 'simplified'
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        for i in range(len(js['result'])):
            print js['result'][i]['id']
            print js['result'][i]['title']


