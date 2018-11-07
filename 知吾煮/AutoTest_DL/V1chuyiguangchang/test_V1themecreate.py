#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class V1themecreateTest(MyTest):
    '''快速添加一个话题'''
    url_path = '/v1/community/theme/create'

    @classmethod
    def setUpClass(cls):
        pass

    def test_themecreate_success(self):
        '''所有信息都发布'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                        self.url_path,
                        {"content": "test",
                         "title": "看看话题创建功能" },
                           #
                           # {"content": null, "deleted": 0, "id": null, "participants": 0, "publicTime": null,
                           #  "style": "{\"color\":\"blue\",\"shade\":\"dd\"}", "thempic": null, "title": "测试主题",
                           #  "toped": 0, "updateTime": null, "userId": null}

                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
