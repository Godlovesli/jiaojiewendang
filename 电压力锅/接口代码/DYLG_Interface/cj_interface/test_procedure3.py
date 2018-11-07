#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class procedure3Test(MyTest):
    '''流程3'''
    # 恢复默认设置-最近使用的集合为空


    @classmethod
    def setUpClass(cls):
        pass

    def test_procedure3_success(self):
        '''所有参数都传'''
        url_path1 = '/v1/recipe/manager/reset'
        payload = {'deviceid': '57357285'}   #57357235
        r = self.myhttp('POST',
                        url_path1,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']


        url_path = '/v1/recipe/manager/mylist'
        payload = {'deviceid': '57357285', 'pageno': 1, 'perpage': 10}
        r = self.myhttp('GET',
                        url_path,
                        payload,
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        print js['result']
        self.assertEqual(js['result'], [])


