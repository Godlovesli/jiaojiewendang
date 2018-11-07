#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import requests
import unittest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class manageropTest(MyTest):
    '''我的模式,管理;分页获取[列表] 编辑'''
    url_path = '/v1/recipe/manager/sort'

    @classmethod
    def setUpClass(cls):
        pass

    def test_managerop_success(self):
        '''所有参数都传'''
        url = self.url_path + '?deviceid=53312514'
        payload = [{"recipeid":5,"top":1,"type":0},
                        {"recipeid":3532,"top":0,"type":1},
                        {"recipeid": 3526, "top": 1, "type": 0},
                        {"recipeid":2,"top":1,"type":0},
                        {"recipeid":1,"top":1,"type":0},
                        {"recipeid":4,"top":1,"type":0},
                        {"recipeid":3,"top":0,"type":1}]
        r = self.myhttp('POST',
                        url,
                        json.dumps(payload),
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)






