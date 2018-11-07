#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecookscriptfindTest(CJMyTest):
    '''根据设备ID和model获取米相关信息(需要加密)'''
    url_path = '/device/cook/getRice'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecookscriptfind_success(self):
        '''根据设备ID和model获取米相关信息'''
        r = self.cjmyhttp('GET',
                         self.url_path,
                          {'deviceId': self.deviceId, 'model': self.model_name},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        # self.assertIn(u'获取菜谱烹饪程序成功', js['message'])

#id是这条记录的id
