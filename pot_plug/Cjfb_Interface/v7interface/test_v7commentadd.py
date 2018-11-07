#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 11:06
# @Author  : fengguifang
# @File    : test_v7commentadd.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import unittest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class v7commentaddTest(CJMyTest):
    '''添加评论'''
    url_path = '/v7/recipe/comment/addNew'


    @classmethod
    def setUpClass(cls):
        pass

    @unittest.skip(u"强制跳过示例")
    def test_v7commentadd_success(self):
        '''必传参数'''
        r = self.cjmyhttpjs('POST',
                        self.url_path,
                        {'device': self.deviceId,'contents':'这个食谱不错','recipeId':2793}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("添加评论成功", js['message'])



