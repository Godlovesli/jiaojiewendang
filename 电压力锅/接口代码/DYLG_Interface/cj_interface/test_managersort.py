#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class managersortTest(MyTest):
    '''我的模式,管理;分页获取[列表] 编辑'''
    url_path = '/v1/recipe/manager/sort'


    @classmethod
    def setUpClass(cls):
        pass

    def test_managersort_success(self):
        '''我的模式,管理;分页获取[列表] 编辑'''
        url_path = self.url_path + '?deviceid=57357285'
        post_data = [{"recipeid": 5, "top": 1, "type": 0},
                     {"recipeid": 1830, "top": 1, "type": 0},
                     {"recipeid": 1829, "top": 0, "type": 1},
                     {"recipeid": 2, "top": 0, "type": 1},
                     {"recipeid": 1, "top": 0, "type": 1},
                     {"recipeid": 6, "top": 1, "type": 0},
                     {"recipeid": 7, "top": 1, "type": 0},
                     {"recipeid": 8, "top": 1, "type": 0},
                     {"recipeid": 9, "top": 1, "type": 0},
                     {"recipeid": 1808, "top": 0, "type": 1},
                     {"recipeid": 4, "top": 0, "type": 1},
                     {"recipeid": 1580, "top": 0, "type": 1},
                     {"recipeid": 3, "top": 0, "type": 1}]
        data_json = json.dumps(post_data)
        r = self.myhttp('POST',
                         url_path,
                        data_json,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)




