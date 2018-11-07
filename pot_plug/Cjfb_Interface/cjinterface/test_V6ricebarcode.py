#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase1 import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ricebarcodeTest(CJMyTest):
    '''扫码获取米详情'''
    url_path = '/v6/rice/barcode'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricebarcode_success(self):
        '''所有参数都传'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'deviceid':'','barCode':self.barcode}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取米详情成功", js['message'])



    def test_ricebarcode_FTsuccess(self):
        '''海外版扫码添加米种不需要传deviceid，所有参数都传'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'deviceid': '','barCode':self.barcode,'language':self.language}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取米详情成功", js['message'])