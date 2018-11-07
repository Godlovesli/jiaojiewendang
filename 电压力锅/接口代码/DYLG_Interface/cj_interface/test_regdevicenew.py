#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class regdeviceTest(MyTest):
    '''json格式注册设备'''
    url_path = '/v1/device/regdevicenew'

    @classmethod
    def setUpClass(cls):
        pass

    def test_regdevice_success(self):
        '''注册设备,传城市名、经纬度后，海拔是否拿到(应拿到海拔值)'''
        payload = {'deviceId': '57357285',
                   'userId': '442376660',
                   'ownerId': '442376660',
                   'ownerName': 'REcc',
                   'deviceModelName': 'chunmi.pre_cooker.cn2',
                   'cityName':'上海市',
                   'longitude': '121.598659',
                   'latitude': '31.185236'
                   }
        r = self.myhttp('POST',
                         self.url_path,
                         json.dumps(payload),
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertEqual(js['message'], 'success')
        print js['result']['elevation']
        if js['result']['elevation'] is not None:
            print js['result']['elevation']
        else:
            print "未拿到海拔值"
        self.assertEqual(js['result']['elevation'], 13)


    def test_regdevice_success1(self):
        '''注册设备,传经纬度后，海拔是否拿到(应拿到海拔值)'''
        payload = {'deviceId': '57357285',
                   'userId': '442376660',
                   'ownerId': '442376660',
                   'ownerName': 'REcc',
                   'deviceModelName': 'chunmi.pre_cooker.cn2',
                   'cityName': '',
                   'longitude': '121.598659',
                   'latitude': '31.185236'
                   }
        r = self.myhttp('POST',
                        self.url_path,
                        json.dumps(payload),
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertEqual(js['message'], 'success')
        if js['result']['elevation'] is not None:
            print js['result']['elevation']
        else:
            print "未拿到海拔值"
        self.assertEqual(js['result']['elevation'], 13)


    def test_regdevice_success2(self):
        '''注册设备,传城市名后，海拔是否拿到(应拿到海拔值)'''
        payload = {'deviceId': '57357285',
                   'userId': '442376660',
                   'ownerId': '442376660',
                   'ownerName': 'REcc',
                   'deviceModelName': 'chunmi.pre_cooker.cn2',
                   'cityName': '上海市',
                   'longitude': '',
                   'latitude': ''
                   }
        r = self.myhttp('POST',
                        self.url_path,
                        json.dumps(payload),
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertEqual(js['message'], 'success')
        if js['result']['elevation'] is not None:
            print js['result']['elevation']
        else:
            print "未拿到海拔值"
        self.assertEqual(js['result']['elevation'],13)