#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class commentmoreTest(MyTest):
    '''获取最新评论(分页)'''
    url_path = '/v1/recipecomment/more'

    @classmethod
    def setUpClass(cls):
        pass

    def test_commentmore_success(self):
        '''只传必填参数'''
        payload = {'recipeid': '1580'}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['id']
            print js['result'][i]['contents']
            print js['result'][i]['userName']
        print js['result'][0]['id']


    def test_commentmore_success1(self):
        '''所有参数都传'''
        payload = {'recipeid': '1294','pageno':1,'perpage':5}
        r = self.myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['id']
            print js['result'][i]['contents']
            print js['result'][i]['userName']


    def test_commentmore_success2(self):
        '''所有参数都传'''
        payload = {'recipeid': '1294', 'pageno': 2, 'perpage': 5}
        r = self.myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        for i in range(len(js['result'])):
            print js['result'][i]['id']
            print js['result'][i]['contents']
            print js['result'][i]['userName']