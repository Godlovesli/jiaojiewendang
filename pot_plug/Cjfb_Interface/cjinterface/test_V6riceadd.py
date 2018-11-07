#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class riceaddTest(CJMyTest):
    '''添加米'''
    url_path = '/v6/rice/add'

    @classmethod
    def setUpClass(cls):
        pass

    def test_riceadd_success(self):
        '''所有参数都传'''
        r = self.cjmyhttp('POST',
                        self.url_path,
                        {'deviceid': self.deviceId,'name':u'莉莉1','brand':'brand79','ppties':'testsx079','barCode':'71000047777'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("添加米详情成功", js['message'])