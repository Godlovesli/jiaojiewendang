#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class commentaddnewTest(MyTest):
    '''添加一条评论'''
    url_path = '/v1/recipecomment/addnewByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_commentadd_success(self):
        '''所有必填字段都传'''
        payload = { 'recipeId': 13375, 'contents': '赞', 'language': ''}
        r = self.cry_myhttp('POST',
                         self.url_path,
                        json.dumps(payload),
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertEqual(js['message'], 'success')


