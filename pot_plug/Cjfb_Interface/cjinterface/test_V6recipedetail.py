#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipedetailTest(CJMyTest):
    '''按ID查询菜谱详情'''
    url_path = '/v6/recipe/detail'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipedetail_success(self):
        '''所有字段都传'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                         {'deviceid': self.deviceId,'recipeid':'256','language':self.language},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( '获取菜谱详情成功',js['message'])

