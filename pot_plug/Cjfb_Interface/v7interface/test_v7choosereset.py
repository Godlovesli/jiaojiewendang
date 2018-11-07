#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 11:09
# @Author  : fengguifang
# @File    : test_v7choosereset.py
# @Software: PyCharm
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7resetTest(CJMyTest):
    '''重置'''
    url_path = '/v7/recipe/choose/reset'

    @classmethod
    def setUpClass(cls):
        pass

    def test_v7reset_success(self):
        '''必传参数'''
        r = self.cjmyhttp('POST',
                        self.url_path,
                        {'deviceId': self.deviceId,'model':self.model_name}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("重置成功", js['message'])
