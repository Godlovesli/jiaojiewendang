#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 18:00
# @Author  : fengguifang
# @File    : test_dataclear.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from base.cjbase import CJMyTest

class dataclearTest(CJMyTest):
    # '''清除数据
    # 1、清除用户收藏的米
    # 2、清除用户加的米
    # 3、清除用户收藏的食谱
    #  4、清除用户评论 '''  #---能删除自己的评论
    url_path =  '/user/data/clear'


    @classmethod
    def setUpClass(cls):
        pass

    def test_dataclear_success1(self):
        r = self.cjmyhttp('POST',
                          self.url_path,
                          {'deviceId': 9382018}
                          )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('清除成功', js['message'])


