#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 13:54
# @Author  : fengguifang
# @File    : test_v7deviceupdatecity.py
# @Software: PyCharm
from base.cjbase import  CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class deviceupdateCityTest(CJMyTest):
    '''注册设备'''
    url_path = '/v7/device/global/regdeviceNew'

    @classmethod
    def setUpClass(cls):
        pass

    def test_deviceupdateCity_success(self):
        '''必传参数'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {
                                "deviceId": '123400', 'serverArea':'广州',
                                'model':self.model_name,
                                'longitude':23.05,
                                 'latitude':113.11,
                         }
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
