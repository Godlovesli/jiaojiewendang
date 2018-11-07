#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class managermylistTest(MyTest):
    '''获取我的模式最近使用的集合'''
    url_path = '/v1/recipe/manager/mylist'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipesmylist_success(self):
        '''所有参数都传'''
        payload = {'deviceid': '57381615', 'pageno': 1, 'perpage': 10}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']


