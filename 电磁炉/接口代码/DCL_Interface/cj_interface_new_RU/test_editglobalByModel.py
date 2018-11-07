#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 15:40
# @Author  : fengguifang
# @File    : test_editglobalByModel.py
# @Software: PyCharm
from base.base import MyTest
import json
import requests
requests.packages.urllib3.disable_warnings()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class editlobalByModelTest(MyTest):
    '''根据model编辑自定义模式'''
    url_path = '/v1/recipe/collect/editglobalByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_createglobalByModel_success(self):
        '''所有必填字段都传'''
        payload ={'id':'13954','name':'áéíóúÁÉÍ','firePower':36,'duration':20,'temperature':0,'model':'chunmi.ihcooker.v1','language': ''}
        r = self.cry_myhttp('POST',
                         self.url_path,
                        json.dumps(payload),
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        self.assertEqual(js['message'], 'success')