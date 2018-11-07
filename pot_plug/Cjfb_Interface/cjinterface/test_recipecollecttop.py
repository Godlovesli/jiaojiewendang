#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecollecttopTest(CJMyTest):
    '''把食谱设置为置顶'''
    url_path = '/v6/recipe/collect/top'


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecollectadd_success(self):
        '''收藏成功'''
        r = self.cjmyhttp('POST',
                        self.url_path,
                         {'deviceid': self.deviceId,'recipeids':256,'language':'en_US'},   #1676是冬阴功
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( '操作成功',js['message'])

