#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class literrecipeTest(CJMyTest):
    '''获取用户收藏菜谱'''
    url_path =  '/v6/literecipe/recipebydevice'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipelistrecipe1_success(self):
        '''获取用户收藏菜谱'''
        r = self.cjmyhttp('GET',
                         self.url_path,
                         {'deviceid': self.deviceId,'language': 'en_US'},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取菜谱列表成功', js['message'])
        for i in range(len(js['result'])):
            print js['result'][i]['name']

# class literrecipe1Test(unittest.TestCase):
#     '''获取用户收藏菜谱'''
#     def setUp(self):
#         self.base_url = 'http://10.0.10.100:17001'
#         # self.base_url = 'https://capi.joyami.com'
#         self.nonce = generateNonce()
#         self.key = getSessionSecurity(self.nonce)
#
#     def test_recipelistrecipe1_success1(self):
#         ''''''
#         self.url_path = '/v6/literecipe/recipebydevice'
#         url = self.base_url + self.url_path
#         self.signature = generateSignature(self.nonce, "GET", url)
#         params = urllib.urlencode( {'deviceid': 1083258,'language':''})
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
#         js = json.loads(r)
#         print len(js['result'])
#         for i in range(len(js['result'])):
#             print js['result'][i]['recipeId'],js['result'][i]['name'],js['result'][i]['cookCode']
#             # print js['result'][i]['recipeId']
