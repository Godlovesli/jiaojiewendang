#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class highesttemperatureTest(CJMyTest):
    '''计算最高食谱温度'''
    url_path =  '/v6/recipe/caculateHighesttemperature'

    @classmethod
    def setUpClass(cls):
        pass


    def test_Highesttemperature_success(self):
        '''计算最高食谱温度'''
        r = self.cjmyhttp('POST',
                      self.url_path,
                         {'elevation':'200','startTime':'20161223','deviceId': self.deviceId},#

                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn(u'获取最高温度成功', js['message'])