#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 10:41
# @Author  : fengguifang
# @File    : test_v7recipechooseminelist.py
# @Software: PyCharm


from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class v7recipechoosemineTest(CJMyTest):
    '''我的收藏'''
    url_path = '/v7/recipe/choose/mine/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipechoosemine_success(self):
        '''传必填参数'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                          {'deviceId': self.deviceId, 'model': self.model_name,'language':self.language}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['id'],js['result'][i]['name']