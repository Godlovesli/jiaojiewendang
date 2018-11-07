#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class collecteditTest(MyTest):
    '''编辑自定义模式'''
    url_path = '/v1/recipe/collect/edit'

    @classmethod
    def setUpClass(cls):
        pass

    def test_collectedit_success(self):
        '''所有必填字段都传'''
        payload = {'deviceid': '53256503', 'id': 430, 'name': '编辑自定义', 'duration': 10}
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertEqual(js['message'], 'success')



