#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ricecollectaddTest(CJMyTest):
    '''添加米信息到设备的收藏列表'''
    url_path = '/v6/ricecollect/add'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecollectdel_success(self):
        '''所有参数都传'''
        r = self.cjmyhttp('POST',
                        self.url_path,
                        {'deviceid': self.deviceId,'riceid':57143}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("加入用户收藏列表成功", js['message'])