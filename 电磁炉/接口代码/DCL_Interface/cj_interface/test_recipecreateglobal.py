#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import requests
import json
import sys
from base.cryp import encryptBase64
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecreateglobalTest(MyTest):
    '''创建一个自定义模式-针对特殊字符乱码(参数加密,language参数不需要加密)'''
    url_path = '/v1/recipe/collect/createglobal'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecreateglobal_success(self):
        '''创建一个自定义模式'''
        a = 'name=To&firePower=26&duration=60&temperature=0&deviceid=53256503'
        b = encryptBase64(a)
        data = {'data': b, 'language': 'zh_HK'}
        r = self.cry_myhttp('POST',
                         self.url_path,
                            data,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)

