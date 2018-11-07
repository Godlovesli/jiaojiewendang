#coding=utf-8
# from cryptutil import *
import json
import requests
import unittest
from cryp import *
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MyTest(unittest.TestCase):

    def setUp(self):
        # self.base_url = 'http://10.0.10.100:17002'
        self.base_url = 'https://cinapi.joyami.com'
        # self.base_url = 'https://pre-cinapi.joyami.com'
        # self.base_url='https://testm.joyami.com'
        # self.base_url = 'https://inapi.coo-k.com'
        # self.base_url = 'https://cinapi.joyami.com'
        # self.base_url = 'http://pre-inductionplugapi.joyami.com'
        self.nonce = generateNonce()
        self.key = getSessionSecurity(self.nonce)

    def myhttp(self,method,url_path=None,params=None,token=None):
        url = self.base_url+url_path
        print url
        signature = generateSignature(self.nonce, method, url)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': signature,
                   'token': token
                   }
        # params = {'param': 'value', 'param': 'value'}
        # payload1 = urllib.urlencode(params)
        encoded = encryptAES(params, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        try:
            if method == 'GET':
                r = requests.get(url, params=payload, headers=headers,verify=False)
            if method == 'POST':
                r = requests.post(url, data=data, headers=headers,verify=False)
            result = r.text.encode()
            print result
            s = decryptAES(result, self.key)
            # json_response = json.loads(s)
            return s
        except Exception as e:
            print('%s' % e)
            return {}


    def nocryp(self, method, url_path=None, params=None, token=None):
        url = self.base_url + url_path
        signature = generateSignature(self.nonce, method, url)
        headers = {'nonce': self.nonce,
                    'User-Agent': 'chunmiapp',
                    'signature': signature,
                    'token': token
                    }
        # params = {'param': 'value', 'param': 'value'}
        payload = urllib.urlencode(params)
        try:
            if method == 'GET':
                r = requests.get(url, params=payload, headers=headers,verify=False)
            if method == 'POST':
                r = requests.post(url, data=params, headers=headers,verify=False)
            result = r.text.encode()
            s = decryptAES(result, self.key)
            # json_response = json.loads(s)
            return s
        except Exception as e:
            print('%s' % e)
            return {}

    def nosign(self, method, url_path=None, params=None, token=None):
        url = self.base_url + url_path
        signature = generateSignature(self.nonce, 'GET', url)
        headers = {'User-Agent': 'chunmiapp',
                    'token': token
                    }
        # params = {'param': 'value', 'param': 'value'}
        payload = urllib.urlencode(params)
        try:
            if method == 'GET':
                r = requests.get(url, params=payload, headers=headers,verify=False)
            if method == 'POST':
                r = requests.post(url, data=params, headers=headers,verify=False)
            result = r.text.encode()
            # s = decryptAES(result, self.key)
            # json_response = json.loads(s)
            return result
        except Exception as e:
            print('%s' % e)
            return {}

    def signerror(self, method, url_path=None, params=None, token=None):
        url = self.base_url + url_path
        signature = generateSignature(self.nonce,method, url)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': signature+'test',
                   'token': token
                   }
        # params = {'param': 'value', 'param': 'value'}
        payload = urllib.urlencode(params)
        try:
            if method == 'GET':
                r = requests.get(url, params=payload, headers=headers,verify=False)
            if method == 'POST':
                r = requests.post(url, data=params, headers=headers,verify=False)
            result = r.text.encode()
            json_response = json.loads(result)
            self.assertEqual(json_response['state'], -2)
            self.assertIn('拦截请求授权出错', json_response['message'])
            return result
        except Exception as e:
            print('%s' % e)
            return {}

    def noncerror(self, method, url_path=None, params=None, token=None):
        url = self.base_url + url_path
        signature = generateSignature(self.nonce, method, url)
        headers = {'nonce': self.nonce+ 'test',
                    'User-Agent': 'chunmiapp',
                    'signature': signature ,
                    'token': token
                    }
        # params = {'param': 'value', 'param': 'value'}
        payload = urllib.urlencode(params)
        try:
            if method == 'GET':
                r = requests.get(url, params=payload, headers=headers,verify=False)
            if method == 'POST':
                r = requests.post(url, data=params, headers=headers,verify=False)
            result = r.text.encode()
            json_response = json.loads(result)
            self.assertEqual(json_response['state'], -2)
            self.assertIn('拦截请求授权出错', json_response['message'])
            return result
        except Exception as e:
            print('%s' % e)
            return {}


    def myhttp1(self,method, url_path=None,params=None,token=None):
        '''不传token的情况暫可用这个方法'''
        self.url = self.base_url + url_path
        self.signature = generateSignature(self.nonce,method, self.url)
        # params = urllib.urlencode(params)
        encoded = encryptAES(params, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': self.signature,
                   'token': token
                   }
        if method == 'GET':
            url2 = self.url + '?' + payload
            request = urllib2.Request(url2, headers=headers)
            # response = urllib2.urlopen(request)
            # result = response.read()
            # s = decryptAES(result, self.key)
            # return s
        if method == 'POST':
            request = urllib2.Request(self.url, data=payload, headers=headers)
            # response = urllib2.urlopen(request)
            # result = response.read()
            # s = decryptAES(result, self.key)
            # return s
        response = urllib2.urlopen(request)
        result = response.read()
        s = decryptAES(result, self.key)
        return s

    def topicpost(self,method, url_path=None,post_data=None,token=None):
        self.url = self.base_url + url_path
        self.signature = generateSignature(self.nonce, method, self.url)
        jdata=json.dumps(post_data)
        headers = { 'User-Agent': 'chunmiapp',
                    'token': token,
                    'Content-Type': 'application/json'}
        r = requests.post(self.url, data=jdata, headers=headers,verify=False)
        result = r.text.encode()
        # request = urllib2.Request(self.url,data=jdata, headers=headers)
        # response = urllib2.urlopen(request)
        # result = response.read()
        return result


    def bujiami(self,method, url_path=None,post_data=None,token=None):
        self.url = self.base_url + url_path
        self.signature = generateSignature(self.nonce,method, self.url)
        params = urllib.urlencode(post_data)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': self.signature,
                   'token': token
                   }
        if method == 'GET':
            url2 = self.url + '?' + params
            request = urllib2.Request(url2, headers=headers)
        if method == 'POST':
            request = urllib2.Request(self.url, data=params, headers=headers)
        response = urllib2.urlopen(request)
        result = response.read()
        s = decryptAES(result, self.key)
        return s



    def nosign1(self,method, url_path=None,post_data=None,token=None):
        self.url = self.base_url + url_path
        params = urllib.urlencode(post_data)
        headers = {'User-Agent': 'chunmiapp',
                   'token': token
                   }
        if method == 'GET':
            url2 = self.url + '?' + params
            request = urllib2.Request(url2, headers=headers)
        if method == 'POST':
            request = urllib2.Request(self.url, data=params, headers=headers)
        response = urllib2.urlopen(request)
        result = response.read()
        return result


    def topicpost1(self,method, url_path=None,post_data=None,token=None):
        self.url = self.base_url + url_path
        self.signature = generateSignature(self.nonce, method, self.url)
        jdata=json.dumps(post_data)
        headers = { 'User-Agent': 'chunmiapp',
                    'token': token,
                    'Content-Type': 'application/json'}
        request = urllib2.Request(self.url,data=jdata, headers=headers)
        response = urllib2.urlopen(request)
        result = response.read()
        return result

    def publish(self,method, url_path=None,post_data=None,token=None):
        self.url = self.base_url + url_path
        self.signature =generateSignature(self.nonce,method,self.url)
        register_openers()
        data, headers = multipart_encode(post_data)
        request = urllib2.Request(self.url, data=data, headers=headers)
        request.add_header('nonce', self.nonce)
        request.add_header('signature', self.signature)
        request.add_header('User-Agent', 'chunmiapp')
        request.add_header('token',token)
        response = urllib2.urlopen(request)
        result = response.read()
        s = decryptAES(result, self.key)
        return s

    def tearDown(self):
        pass