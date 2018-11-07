#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecookscriptfindTest(CJMyTest):
    '''获取食谱烹饪程序'''
    url_path =  '/v6/recipecookscript/find'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecookscriptfind_success(self):
        '''获取食谱烹饪程序'''
        r = self.cjmyhttp('GET',
                         self.url_path,
                          {'deviceid': self.deviceId, 'recipeid': 256},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取菜谱烹饪程序成功', js['message'])

# class recipecookscriptfind1Test(unittest.TestCase):
#     '''获取食谱的烹饪程序'''
#     def setUp(self):
#         # self.base_url = 'https://testapi2.coo-k.com'
#         self.base_url = 'http://10.0.10.100:17001'
#         self.nonce = generateNonce()
#         self.key = getSessionSecurity(self.nonce)
#
#     def test_recipecookscriptfind_success(self):
#         ''''''
#         self.url_path = '/v6/recipecookscript/find'
#         url = self.base_url + self.url_path
#         self.signature = generateSignature(self.nonce, "GET", url)
#         params = urllib.urlencode( {'deviceid': 1128170,'recipeid':256})
#         print params
#         encoded = encryptAES(params, self.key)
#         data = {'data': encoded}
#         payload = urllib.urlencode(data)
#         headers = {'nonce': self.nonce,
#                    'User-Agent': 'chunmiapp',
#                    'signature': self.signature
#                    }
#         url2 = url + '?' + payload
#         print url2
#         request = urllib2.Request(url2, headers=headers)
#         print request
#         response = urllib2.urlopen(request)
#         print response
#         result = response.read()
#         print result
#         r = decryptAES(result,self.key)
#         print r
#
# class recipecookscriptfind22Test(unittest.TestCase):
#     '''获取食谱的烹饪程序'''
#     def setUp(self):
#         # self.base_url = 'https://testapi2.coo-k.com'
#         self.base_url = 'https://capi.joyami.com'
#         self.nonce = generateNonce()
#         self.key = getSessionSecurity(self.nonce)
#
#     def test_recipecookscriptfind_success(self):
#         ''''''
#         self.url_path = '/v6/recipecookscript/find'
#         url = self.base_url + self.url_path
#         self.signature = generateSignature(self.nonce, "GET", url)
#         params = urllib.urlencode( {'deviceid': 53028356,'recipeid':1,'cookstyleid':1100,'tasteid':4111,'language':'taiwan','cookerModel':'chunmi.cooker.normal1'})
#         print params
#         encoded = encryptAES(params, self.key)
#         data = {'data': encoded}
#         payload = urllib.urlencode(data)
#         headers = {'nonce': self.nonce,
#                    'User-Agent': 'chunmiapp',
#                    'signature': self.signature
#                    }
#         url2 = url + '?' + payload
#         print url2
#         request = urllib2.Request(url2, headers=headers)
#         print request
#         response = urllib2.urlopen(request)
#         print response
#         result = response.read()
#         print result
#         r = decryptAES(result,self.key)
#         print r
