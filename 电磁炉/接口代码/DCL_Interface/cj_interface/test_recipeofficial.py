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

    def test_officialrecipelist_success(self):
        '''非必填参数不传'''
        # 53256503
        payload = {'deviceid': self.deviceId, 'pageno': 1, 'perpage': '40', 'language': ''}  #en_US
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name'], js['result'][i]['recipe']['duration']
            print js['result'][i]['recipe']['id']

            # print js['result'][i]['cookCode']



    def test_recipelist_success1(self):
        '''非必填参数不传'''
        payload = {'deviceid': '53256503', 'pageno': 1, 'perpage': '50', 'language': 'english'}
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

