#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 9:55
# @Author  : fengguifang
# @File    : test_feedbackadd.py
# @Software: PyCharm
import json
from base.base import MyTest

class feedbaceTest(MyTest):
    '''添加用户反馈'''
    selfurl = '/feedback/rpc/add'

    @classmethod
    def setUpClass(cls):
        pass


    def test_feedbace_success(self):
        '''添加用户反馈'''
        data = {
                "description": "用户反馈内容",
                "pictures": [{
                    "picUrl": "https://img.joyami.com/img/20180625/1529923550437_0.jpg"
                }, {
                    "picUrl": "https://img.joyami.com/img/20180625/1529923552221_1.jpg"
                }],
                "token": "YjdjNzE4YmMzMDY1YWUwZjhmNzQ2M2QwNjE1YWIzZDA="
            }
        result = self.myhttp('POST',self.selfurl,json.dumps(data),0)

        print (result)
        js = json.loads(result)
        self.assertEqual(200, js['code'])
        self.assertIn('操作成功', js['message'])