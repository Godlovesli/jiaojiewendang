#coding:utf-8
# -*- __author__ = 'feng' -*-

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class riceaddTest(CJMyTest):
    '''添加米'''
    url_path = '/v7/rice/addNew'

    @classmethod
    def setUpClass(cls):
        pass

    def test_riceadd_success(self):
        '''所有参数都传'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {

                         'deviceId': self.deviceId,
                         'name':'wjy88',
                         'id': '',
                         'brand':'brand788',
                         'ppties':'testsx0787',
                         'barCode':'2018080260000',
                         'language':self.language,
                         'pic':'/b2197884207041d7b24f1c73db4cde68.jpg'


                         }
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        print js['result']['name'] #打印米名称