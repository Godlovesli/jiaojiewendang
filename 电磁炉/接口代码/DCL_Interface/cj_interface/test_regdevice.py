#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import unittest
import json
import requests
requests.packages.urllib3.disable_warnings()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class regdeviceTest(MyTest):
    '''注册设备'''
    url_path = '/v1/device/regdevice'

    @classmethod
    def setUpClass(cls):
        pass

    def test_regdevice_success(self):
        '''注册设备'''
        payload = {'deviceId': '53256485',
                   'userId': '442376660',
                   'ownerId': '442376660',
                   'ownerName': 'REcc',
                   'deviceModelName': 'chunmi.ihcooker.v1'
                   }
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)


    # def test_regdevice_success1(self):
    #     '''注册设备'''
    #     # 'name=米家电磁炉-台湾版' \
    #     # '&deviceId=91838660' \
    #     # '&userId=442376660' \
    #     # '&userName=米家电磁炉-台湾版' \
    #     # '&ownerId=&deviceModelName=chunmi.ihcooker.tw1' \
    #     # '&ownerName=REcc&language=zh_TW'
    #     payload = {'name': '米家电磁炉-台湾版',
    #                'deviceId': '91838660',
    #                'userId': '442376660',
    #                'userName': '米家电磁炉-台湾版',
    #                'ownerId':'',
    #                'deviceModelName': 'chunmi.ihcooker.tw1',
    #                'ownerName':'REcc',
    #                'language':'zh_TW'
    #                }
    #     r = self.myhttp('POST',
    #                     self.url_path,
    #                     payload,
    #                     )
    #
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['code'], 1)
    #
    #
    #
