#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
import json
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class V1topicgetTest(MyTest):
    '''主题列表'''
    url_path = '/v1/topic/get'

    @classmethod
    def setUpClass(cls):
        pass

    def test_topicget_ccsuccess(self):
        '''传必填参数'''
        params = 'pageNo=1'
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功',js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['content']


    def test_topicget_bccsuccess(self):
        '''传必填参数'''
        params = ''
        r = self.myhttp('GET',
                        self.url_path,
                        params
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('获取成功',js['message'])



    def test_topicget_signerror(self):
        '''sign不正确'''
        params = {'': ''}
        r = self.signerror('GET',
                           self.url_path,
                           params

                           )

        print r




    def test_topicget_noncerror(self):
        '''nonce不正确'''
        params = {'': ''}
        r = self.noncerror('GET',
                           self.url_path,
                           params

                           )

        print r






