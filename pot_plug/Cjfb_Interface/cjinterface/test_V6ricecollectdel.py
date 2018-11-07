#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ricecollectdelTest(CJMyTest):
    '''删除用户的收藏米谱'''
    url_path = '/v6/ricecollect/del'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecollectdel_success(self):
        '''所有参数都传'''
        r = self.cjmyhttp('POST',
                        self.url_path,
                        {'deviceid': '5182018','riceid':57143}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("删除收藏记录成功", js['message'])