#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
from base.login import Login
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class indrecipecommentaddTest(MyTest):
    '''食谱评论-知吾煮(针对提交评论)'''
    url_path = '/v1/ind/recipecomment/add'

    @classmethod
    def setUpClass(cls):
        pass

    def test_indrecipecommentadd_success(self):
        '''所有必填字段都传'''
        token = Login().login()  # 引用登录
        # token='MTcyNmRiZjhlOTA5ZDkyNWM4NDU3YWVhN2MxYzlmMDU='
        # print(token)
        payload = {'deviceId': '53256503', 'recipeId': 3495, 'contents': '赞'}
        r = self.myhttp('POST',
                         self.url_path,
                        payload,
                        token
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        self.assertEqual(js['message'], 'success')

