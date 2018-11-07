#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class managermyTest(MyTest):
    '''获取我的模式'''
    url_path = '/v1/recipe/manager/my'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeslist_success(self):
        '''所有参数都传'''
        #53256503
        payload = {'deviceid': self.deviceId, 'language': ''} #zh_TW
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']


