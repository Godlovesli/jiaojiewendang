#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class commentaddnewTest(MyTest):
    '''添加一条评论'''
    url_path = '/v1/recipecomment/addnew'



    @classmethod
    def setUpClass(cls):
        pass

    def test_commentadd_success(self):
        '''所有必填字段都传'''
        payload = {'deviceId': self.deviceId, 'recipeId': 23077, 'contents': 'good o ', 'language': ''}
        r = self.myhttp('POST',
                         self.url_path,
                        json.dumps(payload),
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)



