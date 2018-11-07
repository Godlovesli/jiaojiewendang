#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import unittest
import json
import urllib, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ricecookscriptfindTest(CJMyTest):
    '''查找米烹饪程序'''
    url_path = '/v6/ricecookscript/findByModel'

    @classmethod
    def setUpClass(cls):
        pass


    @unittest.skip(u"强制跳过示例")



    def test_ricecookscriptfind_success(self):
        '''传必填参数'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'model': self.model_name,'cookstyleid':1200,'tasteid':4101}   #快煮是1200,
                            )
        print r
        js = json.loads(r)
            # print js
        self.assertEqual(js['state'],0)
#俄罗斯服务器没有添加米的功能，扫码添加米和查找米烹饪程序(所以注释此功能）
