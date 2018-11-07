#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 11:20
# @Author  : fengguifang
# @File    : test_v7globalregdeviceNew.py
# @Software: PyCharm

from base.cjbase import  CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7devicenewTest(CJMyTest):
    '''注册'''
    url_path = '/v7/device/global/regdeviceNew'

    @classmethod
    def setUpClass(cls):
        pass

    def test_v7regdeviceNew_success(self):
        '''必传参数'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {'deviceId': self.deviceId,
                        'mac': 'F0:B4:29:BE:94:5C',
                        'userId': '54644930',
                        'online': '1',
                        'cityName': 'shanghai',
                        'ownerId': '54644930',
                        'ownerName': '11',
                        'model':self.model_name,
                        'modelName': self.model_name}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])