# #coding:utf-8
# # -*- __author__ = 'feng' -*-
# from base.base import MyTest
# from base.mydb import MyDB
# import requests
# import unittest
# import json
# import time
# from HTMLTestRunner import HTMLTestRunner
# import urllib, urllib2
# from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
# import MySQLdb
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
#
# class cookscriptgenerateTest(MyTest):
#     '''生成试煮烹饪程序'''
#     # url_path = '/v4/article/topadv'
#     url_path = '/v1/recipe/cookscript/generate'
#
#     @classmethod
#     def setUpClass(cls):
#         pass
#
#
#     def test_cookscriptgenerate_sysuccess(self):
#         '''所有参数都传入，生成试煮烹饪程序成功'''
#         self.base_url = 'http://10.0.10.100:17002'
#         self.url = self.base_url + '/v1/recipe/cookscript/generate'
#         self.signature = generateSignature(self.nonce, 'GET', self.url)
#         self.headers = {'nonce': self.nonce,
#                    'User-Agent': 'chunmiapp',
#                    'signature': self.signature
#
#                    }
#         # jdata":[{"description":"","name":"烹饪完成前4分钟开盖","stepPic":"recipe/57ae6b4f-15a9-47ee-a305-d35e4615f29c.png","resumeIndex":5,
#         # "resumeTime":4,"resumeType":18020}],
#         jdata1 ={'jdata':[{"description": "",
#                      "name": "烹饪完成前4分钟开盖",
#                      "stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg",
#                      "resumeIndex":5,
#                      "resumeTime":4,
#                      "resumeType":18020}]}
#         jdata2 = urllib.urlencode(jdata1)
#         encoded1 = encryptAES(jdata2, self.key)
#         data1 = {'data': encoded1}
#         payload1 = urllib.urlencode(data1)
#
#         post_data={'templetid':14,'deviceid':1083258}
#         post_data1 = urllib.urlencode(post_data)
#         encoded = encryptAES(post_data1, self.key)
#         data2 = {'data': encoded}
#         payload2 = urllib.urlencode(data2)
#         r = requests.get(self.url, params=payload2,json=payload1, headers=self.headers)
#         result = r.text.encode()
#         s = decryptAES(result, self.key)
#         print s
#         js = json.loads(s)
#         self.assertEqual(js['state'], 1)
#         self.assertIn('生成烹饪程序成功', js['message'])
#
#     def test_cookscriptgenerate_tidno(self):
#         '''templetid未传'''
#         self.base_url = 'http://10.0.10.100:17002'
#         self.url = self.base_url + '/v1/recipe/cookscript/generate'
#         self.nonce = generateNonce()
#         self.key = getSessionSecurity(self.nonce)
#         self.signature = generateSignature(self.nonce, 'GET', self.url)
#         self.headers = {'nonce': self.nonce,
#                         'User-Agent': 'chunmiapp',
#                         'signature': self.signature
#
#                         }
#
#         post_data = {'jdata': [{"description": "",
#                                 "name": "烹饪完成前4分钟开盖",
#                                 "stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg",
#                                 "resumeIndex": 5,
#                                 "resumeTime": 4,
#                                 "resumeType": 18020}]}
#         data_json = json.dumps(post_data)
#         print data_json
#         B = {'json': data_json, 'deviceid': 1083258}
#         payload1 = urllib.urlencode(B)
#         encoded = encryptAES(payload1, self.key)
#         data = {'data': encoded}
#         payload = urllib.urlencode(data)
#         print payload
#         url2 = self.url + '?' + payload
#         request = urllib2.Request(url2)
#         request.add_header('nonce', self.nonce)
#         request.add_header('signature', self.signature)
#         request.add_header('User-Agent', 'chunmiapp')
#         result = urllib2.urlopen(request).read()
#         print result
#         s = decryptAES(result, self.key)
#         print s
#         js = json.loads(s)
#         self.assertEqual(js['state'], -4)
#         self.assertIn("parameter 'templetid' is not present", js['message'])
#
#
#     def test_cookscriptgenerate_didno(self):
#         '''deviceid未传'''
#         self.base_url = 'http://10.0.10.100:17002'
#         self.url = self.base_url + '/v1/recipe/cookscript/generate'
#         self.nonce = generateNonce()
#         self.key = getSessionSecurity(self.nonce)
#         self.signature = generateSignature(self.nonce, 'GET', self.url)
#         self.headers = {'nonce': self.nonce,
#                         'User-Agent': 'chunmiapp',
#                         'signature': self.signature
#
#                         }
#
#         post_data = {'jdata': [{"description": "",
#                                 "name": "烹饪完成前4分钟开盖",
#                                 "stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg",
#                                 "resumeIndex": 5,
#                                 "resumeTime": 4,
#                                 "resumeType": 18020}]}
#         data_json = json.dumps(post_data)
#         print data_json
#         B = {'json': data_json, 'templetid':14}
#         payload1 = urllib.urlencode(B)
#         encoded = encryptAES(payload1, self.key)
#         data = {'data': encoded}
#         payload = urllib.urlencode(data)
#         print payload
#         url2 = self.url + '?' + payload
#         request = urllib2.Request(url2)
#         request.add_header('nonce', self.nonce)
#         request.add_header('signature', self.signature)
#         request.add_header('User-Agent', 'chunmiapp')
#         result = urllib2.urlopen(request).read()
#         print result
#         s = decryptAES(result, self.key)
#         print s
#         js = json.loads(s)
#         self.assertEqual(js['state'], -4)
#         self.assertIn("parameter 'deviceid' is not present", js['message'])
#
#
#     def test_cookscriptgenerate_signerror(self):
#         '''sign不正确'''
#         self.base_url = 'http://10.0.10.100:17002'
#         self.url = self.base_url + '/v1/recipe/cookscript/generate'
#         self.nonce = generateNonce()
#         self.key = getSessionSecurity(self.nonce)
#         self.signature = generateSignature(self.nonce, 'GET', self.url)
#         self.headers = {'nonce': self.nonce,
#                         'User-Agent': 'chunmiapp',
#                         'signature': self.signature
#
#                         }
#
#         post_data = {'jdata': [{"description": "",
#                                 "name": "烹饪完成前4分钟开盖",
#                                 "stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg",
#                                 "resumeIndex": 5,
#                                 "resumeTime": 4,
#                                 "resumeType": 18020}]}
#         data_json = json.dumps(post_data)
#         print data_json
#         B = {'json': data_json, 'templetid': 14, 'deviceid': 1083258}
#         payload1 = urllib.urlencode(B)
#         encoded = encryptAES(payload1, self.key)
#         data = {'data': encoded}
#         payload = urllib.urlencode(data)
#         print payload
#         url2 = self.url + '?' + payload
#         request = urllib2.Request(url2)
#         request.add_header('nonce', self.nonce)
#         request.add_header('signature', self.signature+'ee')
#         request.add_header('User-Agent', 'chunmiapp')
#         result = urllib2.urlopen(request).read()
#         print result
#         js = json.loads(result)
#         self.assertEqual(js['state'], -2)
#         self.assertIn("拦截请求授权出错", js['message'])
#
#
#     def test_cookscriptgenerate_noncerror(self):
#         '''nonce不正确'''
#         self.base_url = 'http://10.0.10.100:17002'
#         self.url = self.base_url + '/v1/recipe/cookscript/generate'
#         self.nonce = generateNonce()
#         self.key = getSessionSecurity(self.nonce)
#         self.signature = generateSignature(self.nonce, 'GET', self.url)
#         self.headers = {'nonce': self.nonce,
#                         'User-Agent': 'chunmiapp',
#                         'signature': self.signature
#
#                         }
#
#         post_data = {'jdata': [{"description": "",
#                                 "name": "烹饪完成前4分钟开盖",
#                                 "stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg",
#                                 "resumeIndex": 5,
#                                 "resumeTime": 4,
#                                 "resumeType": 18020}]}
#         data_json = json.dumps(post_data)
#         print data_json
#         B = {'json': data_json, 'templetid': 14, 'deviceid': 1083258}
#         payload1 = urllib.urlencode(B)
#         encoded = encryptAES(payload1, self.key)
#         data = {'data': encoded}
#         payload = urllib.urlencode(data)
#         print payload
#         url2 = self.url + '?' + payload
#         request = urllib2.Request(url2)
#         request.add_header('nonce', self.nonce+'ee')
#         request.add_header('signature', self.signature)
#         request.add_header('User-Agent', 'chunmiapp')
#         result = urllib2.urlopen(request).read()
#         print result
#         js = json.loads(result)
#         self.assertEqual(js['state'], -2)
#         self.assertIn("拦截请求授权出错", js['message'])
#
#
# class cookscriptgenerate12Test(MyTest):
#        def setUp(self):
#            pass
#
#        def test_case_01(self):
#             self.base_url = 'http://10.0.10.100:17002'
#             self.url = self.base_url + '/v1/recipe/cookscript/generate'
#             self.nonce = generateNonce()
#             self.key = getSessionSecurity(self.nonce)
#             self.signature = generateSignature(self.nonce, 'GET', self.url)
#             self.headers = {'nonce': self.nonce,
#                             'User-Agent': 'chunmiapp',
#                             'signature': self.signature
#
#                             }
#             jdata1 = {'jdata': [{"description": "",
#                                  "name": "烹饪完成前4分钟开盖",
#                                  "stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg",
#                                  "resumeIndex": 5,
#                                  "resumeTime": 4,
#                                  "resumeType": 18020}]}
#             jdata2 = urllib.urlencode(jdata1)
#             encoded1 = encryptAES(jdata2, self.key)
#             data1 = {'data': encoded1}
#             payload1 = urllib.urlencode(data1)
#
#             post_data = {'templetid': 14, 'deviceid': 1083258}
#             post_data1 = urllib.urlencode(post_data)
#             encoded = encryptAES(post_data1, self.key)
#             data2 = {'data': encoded}
#             payload2 = urllib.urlencode(data2)
#             r = requests.get(self.url, params=payload2, json=payload1, headers=self.headers)
#             result = r.text.encode()
#             s=decryptAES(result,self.key)
#             print s
#             js = json.loads(s)
#             self.assertEqual(js['state'], 1)
#             self.assertIn('生成烹饪程序成功', js['message'])
#
#        def test_case_02(self):
#             self.base_url = 'http://10.0.10.100:17002'
#             self.url = self.base_url + '/v1/recipe/cookscript/generate'
#             self.nonce = generateNonce()
#             self.key = getSessionSecurity(self.nonce)
#             self.signature = generateSignature(self.nonce, 'GET', self.url)
#             self.headers = {'nonce': self.nonce,
#                             'User-Agent': 'chunmiapp',
#                             'signature': self.signature
#
#                             }
#
#             post_data ={'jdata':[{"description": "",
#                          "name": "烹饪完成前4分钟开盖",
#                          "stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg",
#                          "resumeIndex":5,
#                          "resumeTime":4,
#                          "resumeType":18020}]}
#             data_json = json.dumps(post_data)
#             print data_json
#             B={'json':data_json,'templetid':14,'deviceid':1083258}
#             payload1 = urllib.urlencode(B)
#             encoded = encryptAES(payload1, self.key)
#             data = {'data': encoded}
#             payload = urllib.urlencode(data)
#             print payload
#             url2 = self.url + '?' + payload
#             request = urllib2.Request(url2)
#             request.add_header('nonce', self.nonce)
#             request.add_header('signature', self.signature)
#             request.add_header('User-Agent', 'chunmiapp')
#             result = urllib2.urlopen(request).read()
#             print result
#             s = decryptAES(result, self.key)
#             print s
#             js = json.loads(s)
#             self.assertEqual(js['state'], 1)
#             self.assertIn('生成烹饪程序成功', js['message'])
#
#        def test_case_03(self):
#            self.base_url = 'http://10.0.10.100:17002'
#            self.url = self.base_url + '/v1/recipe/cookscript/generate'
#            self.nonce = generateNonce()
#            self.key = getSessionSecurity(self.nonce)
#            self.signature = generateSignature(self.nonce, 'GET', self.url)
#            self.headers = {'nonce': self.nonce,
#                            'User-Agent': 'chunmiapp',
#                            'signature': self.signature
#
#                            }
#
#            post_data = {'jdata': [{"description": "",
#                                    "name": "烹饪完成前4分钟开盖",
#                                    "stepPic": "/7b56873b8081406dbfe4da027c2c175c.jpg",
#                                    "resumeIndex": 5,
#                                    "resumeTime": 4,
#                                    "resumeType": 18020}]}
#
#            data_json = json.dumps(post_data)
#            print data_json
#            B = {'json': data_json, 'templetid': 14, 'deviceid': 1083258}
#            payload1 = urllib.urlencode(B)
#            print payload1
#            encoded = encryptAES(payload1, self.key)
#            data = {'data': encoded}
#            print data
#            payload = urllib.urlencode(data)
#            print payload
#            r = requests.get(self.url, params=payload, headers=self.headers)
#            result = r.text.encode()
#            s = decryptAES(result, self.key)
#            print s
#            js = json.loads(s)
#            self.assertEqual(js['state'], 1)
#            self.assertIn('生成烹饪程序成功', js['message'])
