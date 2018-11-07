#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class getTwoRecipeCommentTest(MyTest):
    '''获取食谱的热门评论'''
    url_path =  '/v1/recipeComment/getTwoRecipeComment'

    @classmethod
    def setUpClass(cls):
        pass


    def test_getTwoRecipeComment_success(self):
        '''获取成功'''
        r = self.nosign('GET',
                         self.url_path,
                         { 'id': '423'},
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'评论获取成功', js['message'])





