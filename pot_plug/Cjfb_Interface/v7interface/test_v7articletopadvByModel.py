#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 13:58
# @Author  : fengguifang
# @File    : test_v7articletopadvByModel.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class articletopadvByModelTest(CJMyTest):
    '''获取首页Banner'''
    url_path = '/v7/article/topadvByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_articletopadvByModel_success(self):
        '''传必填参数'''
        r = self.cjmyhttpjs('GET',
                        self.url_path,
                        {'model':self.model_name,'language': self.language}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        for i in range(len(js['result'])):

            print js['result'][i]['id']
        # if len(js['result']) == 0:
        #     print "失败"
        # else:
        #     print "成功"
        # self.assertNotEqual(len(js['result']),0)


