#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecookscriptfindTest(CJMyTest):
    '''添加,当设备下发米种烹饪程序进行烹饪时,调用此接口(需要加密)'''
    url_path = '/device/cook/rice/add'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecookscriptfind_success(self):
        '''添加,当设备下发米种烹饪程序进行烹饪时,调用此接口(需要加密)'''

        r = self.cjmyhttpjs('POST',
                          self.url_path,
                          {'deviceId': self.deviceId, 'model': self.model_name,"riceId":1},
                          )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        # self.assertIn(u'获取菜谱烹饪程序成功', js['message'])













# ''''{
#     "content": {},
#     "message": "",
#     "pageModel": {
#         "list": [],
#         "objectBean": {},
#         "offset": 0,
#         "pageno": 0,
#         "perpage": 0,
#         "total": 0,
#         "totalPage": 0
#     },
#     "result": [],
#     "serverTimeMillis": 0,
#     "state": 0
# }'''