#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipequerygetTest(CJMyTest):
    '''大家都在搜接口'''
    url_path = '/v6/recipe/people/query/get'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipequeryget_success(self):
        '''所有字段都传'''
        r = self.cjbujiami('GET',
                        self.url_path,
                        {'deviceid': self.deviceId, 'language': self.language},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( 'success',js['message'])



