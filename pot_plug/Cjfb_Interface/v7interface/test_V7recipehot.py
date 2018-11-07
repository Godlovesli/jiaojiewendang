#coding=utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 13:15
# @Author  : zhouli
# @File    : test_v7recipequery.py
# @Software: PyCharm


# from base.cjbase import CJMyTest
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7recipehotTest(CJMyTest):
    '''更多食谱，热搜'''
    url_path = '/v7/recipe/hot'

    @classmethod
    def setUpClass(cls):
        pass
    def test_recipehot(self):
        '''获取食谱热词'''
        r = self.cjmyhttp('GET',
                            self.url_path,
                            {'language': self.language,
                             'model': self.model_name,

                             },
                            )

        print r
        js = json.loads(r)
        print  js

        print len(js['result'])
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        print "共有%d个热搜：" %len(js['result'])
        for i in js['result']:
            print "打印热搜名称：%s"%i



