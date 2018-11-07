#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class editglobalnewTest(MyTest):
    '''编辑自定义'''
    url_path = '/v1/recipe/collect/editglobalnew'

    @classmethod
    def setUpClass(cls):
        pass

    def test_editglobalnew_success(self):
        '''编辑自定义'''
        payload = {'id': 16487, 'name': 'good', 'firePower': 26, 'duration': 60, 'temperature': 0, 'deviceid': 65707813,
                   'language': 'zh_HK'}
        r = self.cry_myhttp('POST',
                         self.url_path,
                        json.dumps(payload),
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)





