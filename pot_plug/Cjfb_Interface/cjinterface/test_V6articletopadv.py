#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class articletopadvTest(CJMyTest):
    '''获取banner（6100首页,6200列表）'''
    # url_path = '/v4/article/topadv'
    url_path = '/v6/article/topadv'

    @classmethod
    def setUpClass(cls):
        pass

    def test_articletopadv_sysuccess(self):
        '''传所有参数,获取6100列表'''
        r = self.cjmyhttp('GET',
                         self.url_path,
                          {'type': '6100', 'language': 'ja_JP', 'deviceid': '91903314'},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('banner数据获取成功', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['id']

