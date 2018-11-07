#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipelistByModelTest(MyTest):
    '''获取更多食谱'''
    url_path = '/v1/recipe/listByModel'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipelistByModel_success(self):
        '''非必填参数都传'''
        payload = {'model': 'chunmi.ihcooker.exp1','pageno':1,'perpage': '20', 'keyword': '', 'categoryid': '','language':''}
        r = self.cry_myhttp('GET',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']
            self.assertIsNot(js['result'][i]['cookCode'],None)


    def test_recipelistByModel_success1(self):
        '''所有参数都传'''
        payload = {'model': 'chunmi.ihcooker.hk1','pageno': 1, 'perpage': 100, 'keyword': '松饼', 'categoryid': '',
                   'language': ''}
        r = self.cry_myhttp('GET',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']

