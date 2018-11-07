#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class commentaddTest(MyTest):
    '''添加一条评论'''
    url_path = '/v1/recipecomment/save'#json数据传输格式
    # url_path='/v1/recipecomment/add'
    @classmethod
    def setUpClass(cls):
        pass

    def test_commentadd_success(self):
        '''所有必填字段都传'''
        payload = {
            # 'recipeComment': 'good',
            'contents': 'good',
            'deleted': 0,
            'deviceId': 57357285,
            'id': 20,
            'ip': '192.0.10.209',
            'parentId': 1,
            'recipeId': 1580,
            'stars': 0,
            'state': 0,
            'time': '2018-07-31T05:34:07.838Z',
            'userId': 1
        }

        r = self.myhttp('POST',
                         self.url_path,
                        json.dumps(payload))

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertEqual(js['message'], 'success')


    # def test_commentadd_success1(self):
    #     '''所有必填字段都传'''
    #     payload = { 'recipeId': 1294, 'recipeComment': 'good'}
    #     r = self.myhttp('POST',
    #                     self.url_path,
    #                     payload,
    #                     )
    #
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['code'], 1)
    #     self.assertEqual(js['message'], 'success')
    #
    # def test_commentadd_success2(self):
    #     '''所有必填字段都传'''
    #     payload = {'recipeId': 1294, 'recipeComment': '好'}
    #     r = self.myhttp('POST',
    #                     self.url_path,
    #                     payload,
    #                     )
    #
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['code'], 1)
    #     self.assertEqual(js['message'], 'success')
