#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecollectaddTest(CJMyTest):
    '''添加收藏'''
    url_path = '/v6/recipe/collect/add'


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecollectadd_success(self):
        '''收藏成功'''
        r = self.cjmyhttp('POST',
                        self.url_path,
                         {'deviceid': self.deviceId,'recipeid':'535','language':'en_US'},   #1676是冬阴功
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( '收藏成功',js['message'])

