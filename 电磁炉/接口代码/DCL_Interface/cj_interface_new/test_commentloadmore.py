#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class commentloadmoreTest(MyTest):
    '''获取最新评论(分页)'''
    url_path = '/v1/recipecomment/loadmore'

    @classmethod
    def setUpClass(cls):
        pass

    def test_commentloadmore_success(self):
        '''所有参数都传'''
        payload = {'recipeid': '23077','pageno':1,'perpage':'10'}
        r = self.cry_myhttp('GET',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        print(len(js['result']))
        for i in range(len(js['result'])):
            print js['result'][i]['contents']



