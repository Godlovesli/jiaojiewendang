#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class commentaddTest(MyTest):
    '''添加一条评论'''
    url_path = '/v1/recipecomment/add'

    @classmethod
    def setUpClass(cls):
        pass

    def test_commentadd_success(self):
        '''所有必填字段都传'''
        payload ={
                    'recipeId': 23077,
                    'parentId': '',
                    'deviceId': self.deviceId,
                    'contents': '喜欢吃啊 ',
                    'language': ''
                }
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)



