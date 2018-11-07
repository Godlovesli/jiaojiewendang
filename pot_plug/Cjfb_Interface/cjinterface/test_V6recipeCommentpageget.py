#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 15:22
# @Author  : fengguifang
# @File    : test_V6recipeCommentpageget.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import requests
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import urllib, urllib2
from cjcryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class CommentlistdataTest(CJMyTest):
    '''食谱评论页'''
    url_path = '/v6/recipeComment/listdata'


    @classmethod
    def setUpClass(cls):
        pass

    def test_Commentlistdata_success(self):
        '''所有字段都传'''
        r = self.cjbujiami('GET',
                        self.url_path,
                          {'recipeId': 256, 'language': 'english'},
                         )
        print r
