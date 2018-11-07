#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipelistTest(MyTest):
    '''获取更多食谱'''
    url_path = '/v1/recipe/list'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeingredient_success(self):
        '''不传参数，只获取第一页数据'''
        payload = {'':''}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        # self.assertIn('success',js['message'])
        for i in range(len(js['result']['articleList'])):
            print js['result']['articleList'][i]['title']
            print js['result']['articleList'][i]['id']
        for i in range(len(js['result']['recipeVOList'])):
            print js['result']['recipeVOList'][i]['recipe']['name']
            print js['result']['recipeVOList'][i]['recipe']['id']

    def test_recipeingredient_success1(self):
        '''传参数，只获取第一页数据'''
        payload = {'categoryid': '','keyword':'','deviceid':'','pageno':1,'perpage':100}
        r = self.myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        print js
        self.assertEqual(js['code'], 1)
        # self.assertIn('success', js['message'])

        for i in range(len(js['result']['articleList'])):

            print js['result']['articleList'][i]['title']
            print js['result']['articleList'][i]['id']
        print "获取首页banner食谱数量：%d" % len(js['result']['articleList'])
        for i in range(len(js['result']['recipeVOList'])):
            print js['result']['recipeVOList'][i]['recipe']['name']
            print js['result']['recipeVOList'][i]['recipe']['id']
        print "获取食谱数量：%d" % len(js['result']['recipeVOList'])



    def test_recipeingredient_success2(self):
        '''获取非第一页数据'''
        payload = {'categoryid': '','keyword':'','deviceid':'','pageno':2,'perpage':5}
        r = self.myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertIn('success', js['message'])
        # for i in range(len(js['result']['articleList'])):
        #     print js['result']['articleList'][i]['title']
        #     print js['result']['articleList'][i]['id']
        print len(js['result']['recipeVOList'])
        for i in range(len(js['result']['recipeVOList'])):
            print js['result']['recipeVOList'][i]['recipe']['name']
            print js['result']['recipeVOList'][i]['recipe']['id']


    def test_recipeingredient_success3(self):
        '''搜索关键字'''
        payload = {'categoryid': '','keyword':'大蒜','deviceid':'','pageno':1,'perpage':10}
        r = self.myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertIn('success', js['message'])
        # for i in range(len(js['result']['articleList'])):
        #     print js['result']['articleList'][i]['title']
        #     print js['result']['articleList'][i]['id']
        print len(js['result']['recipeVOList'])
        for i in range(len(js['result']['recipeVOList'])):
            print js['result']['recipeVOList'][i]['recipe']['name']
            print js['result']['recipeVOList'][i]['recipe']['id']

    def test_recipeingredient_success4(self):
        '''搜索关键字'''
        payload = {'categoryid': '2','keyword':'大蒜','deviceid':'','pageno':1,'perpage':10}
        r = self.myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertIn('success', js['message'])
        # for i in range(len(js['result']['articleList'])):
        #     print js['result']['articleList'][i]['title']
        #     print js['result']['articleList'][i]['id']
        print len(js['result']['recipeVOList'])
        for i in range(len(js['result']['recipeVOList'])):
            print js['result']['recipeVOList'][i]['recipe']['name']
            print js['result']['recipeVOList'][i]['recipe']['id']

