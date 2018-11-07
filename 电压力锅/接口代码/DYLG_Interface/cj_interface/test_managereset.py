#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class manageresetTest(MyTest):
    '''恢复默认设置'''
    url_path = '/v1/recipe/manager/reset'

    @classmethod
    def setUpClass(cls):
        pass

    def test_managereset_success(self):
        '''所有参数都传'''
        payload = {'deviceid': '57357285'}   #57357235
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']





