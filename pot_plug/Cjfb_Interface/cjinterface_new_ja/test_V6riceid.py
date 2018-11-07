#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class riceidTest(CJMyTest):
    '''根据ID获取米详情'''
    url_path = '/v6/rice/id'

    @classmethod
    def setUpClass(cls):
        pass

    def test_riceid_success(self):
        '''所有参数都传'''
        r = self.cjmyhttp('GET',
                        self.url_path,
                        {'id': '1','language':'ja_JP'}   #ja_JP
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("获取米详情成功", js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['description']