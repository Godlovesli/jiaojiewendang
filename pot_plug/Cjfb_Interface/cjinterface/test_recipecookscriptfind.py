#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecookscriptfindTest(CJMyTest):
    '''获取食谱烹饪程序'''
    url_path =  '/v6/recipecookscript/find'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecookscriptfind_success(self):
        '''获取食谱烹饪程序'''
        r = self.cjmyhttp('GET',
                         self.url_path,
                          {'deviceid': 9382018, 'recipeid': 256},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取菜谱烹饪程序成功', js['message'])

