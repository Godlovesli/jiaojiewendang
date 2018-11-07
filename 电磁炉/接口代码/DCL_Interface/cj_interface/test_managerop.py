#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json,unittest
import requests
requests.packages.urllib3.disable_warnings()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class manageropTest(MyTest):
    '''设置收藏'''
    # 现在没有这个接口了   8.30注释
    # 根据设备ID, 模式ID进行设置, flag =
    # 1为设置收藏,
    # 0为取消收藏,
    # 3为删除该模式
    url_path = '/v1/recipe/manager/op'


    @classmethod
    def setUpClass(cls):
        pass



    def test_managerop_success(self):
        '''所有参数都传'''
        # payload = {'deviceid': '65707813', 'pageno': 1, 'perpage': 10, 'language': 'hongkong', 'recipeid': 3523, 'flag': 1}
        payload = {'deviceid': self.deviceId, 'recipeid': 23242, 'flag': 1}
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)


    def test_managerop_success1(self):
        '''所有参数都传'''
        payload = {'deviceid': '53256503', 'recipeid': 1, 'flag': 0}
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)


    def test_managerop_success2(self):
        '''所有参数都传'''
        payload = {'deviceid': '53256503', 'recipeid': 868, 'flag': 3}
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)

