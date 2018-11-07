#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class recipecreateglobalnewTest(MyTest):
    '''创建一个自定义模式-针对特殊字符乱码(加密,传json格式)'''
    url_path = '/v1/recipe/collect/createglobalnew'

    @classmethod
    def setUpClass(cls):
        pass

    def test_createglobalnew_success(self):
        '''创建一个自定义模式'''
        payload = {'name': 'áéíóúÁÉÍÓÚ', 'firePower': 26, 'duration': 60, 'temperature': 0, 'deviceid': 65707813,
                   'language': 'es_ES'}
        r = self.cry_myhttp('POST',
                         self.url_path,
                        json.dumps(payload),
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)




