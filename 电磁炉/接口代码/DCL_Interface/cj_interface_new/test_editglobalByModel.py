#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
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
        payload ={'id':'13954','name':'áéíóúÁÉÍ','firePower':36,'duration':20,'temperature':0,'model':self.model,'language': self.language}
        r = self.cry_myhttp('POST',
                         self.url_path,
                        json.dumps(payload),
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        self.assertEqual(js['message'], 'success')


