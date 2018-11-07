#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class generateCookCodeTest(MyTest):
    '''根据食材,做法,口感生成临时程序'''
    url_path = '/v1/recipe/generateCookCode'

    @classmethod
    def setUpClass(cls):
        pass

    def test_generateCookCode_success(self):
        '''所有参数都传，口感A'''
        payload = {'deviceid': '57381615',
                   'name':'软糯',
                   'ingredientid':1,#食材ID
                   'practiceid':6,#做法ID
                   'textureid':2,#口感ID
                   'duration': 0
                   }
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        # self.assertIn('success', js['message'])
        print(js['result'])


    def test_generateCookCode_success1(self):
        '''所有参数都传，口感B'''
        payload = {'deviceid': '57380328',
                   'name': '适中',
                   'ingredientid': 1,  # 食材ID
                   'practiceid': 6,  # 做法ID
                   'textureid': 6,  # 口感ID
                   'duration': 0
                   }
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        # self.assertIn('success', js['message'])
        print(js['result'])


    def test_generateCookCode_success2(self):
        '''所有参数都传，口感C'''
        payload = {'deviceid': '57380328',
                   'name': '弹润',
                   'ingredientid': 1,  # 食材ID
                   'practiceid': 6,  # 做法ID
                   'textureid': 7,  # 口感ID
                   'duration': 0
                   }
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        # self.assertIn('success', js['message'])
        # print(js['result'])

