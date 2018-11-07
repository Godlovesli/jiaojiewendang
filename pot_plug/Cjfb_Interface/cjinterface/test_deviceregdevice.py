#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
from base.CJcryp import *
import json
import urllib,urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipelistrecipeTest(CJMyTest):
    '''注册设备'''
    url_path =  '/v6/device/regdevice'

    @classmethod
    def setUpClass(cls):
        pass


    def test_deviceregdevice_success(self):
        '''注册饭煲'''
        r = self.cjmyhttp('POST',
                         self.url_path,
                          {'deviceid': '7182018',
                           'mac': 'F0:B4:29:BE:94:5C',
                           'userId': '54644930',
                           'online': '1',
                           'cityName': 'shanghai',
                           'ownerId': '54644930',
                           'ownerName': 'ff',
                           'modelName': self.model_name

                           },
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'注册设备成功', js['message'])


    def test_deviceregdevice_success1(self):
        import urllib, urllib2
        url='https://rumipotplugapi.joyami.com/v6/device/regdevice'
        # url = "http://10.0.10.100:17001/v6/device/regdevice"
        nonce = generateNonce()
        signature = generateSignature(nonce, "POST", url)
        A = 'latitude=38.6518&language=en_US&ownerId=&userId=271045941&deviceid=49646547&deviceId=49646547&mac=28:6C:07:26:4F:BE&modelName=chunmi.cooker.press2&ownerName=&cityName=武汉&name=申城&longitude=104.07642&online=false'
        key = getSessionSecurity(nonce)
        encoded = encryptAES(A, key)
        data = {"data": encoded}
        payload = urllib.urlencode(data)
        request = urllib2.Request(url, data=payload)
        request.add_header("nonce", nonce)
        request.add_header("signature", signature)
        request.add_header("User-Agent", "chunmiapp")
        response = urllib2.urlopen(request)
        result = response.read()
        print decryptAES(result, key)
        print type(decryptAES(result, key))