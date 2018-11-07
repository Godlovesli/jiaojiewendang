#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ricecollectallTest(CJMyTest):
    '''获取用户收藏的米信息'''
    url_path = '/v6/ricecollect/allfavricebydid'

    @classmethod
    def setUpClass(cls):
        pass

    def test_ricecollectall_success(self):
        '''所有参数都传'''
        #台湾的设备id   53027267
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'deviceid': '53027267',
                         'language': 'zh_TW'
                         }
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("查找记录成功", js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['id']
            print js['result'][i]['description']


    def test_FTricecollectall_success(self):
        '''所有参数都传'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'deviceid': '1128170','language':'taiwan'}
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("查找记录成功", js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['description']
