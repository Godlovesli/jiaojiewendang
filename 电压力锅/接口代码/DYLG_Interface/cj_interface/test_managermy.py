#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class managermyTest(MyTest):
    '''获取我的模式'''

    # cookBook 模式 / 食谱
    # customRecipe 自定义食谱
    # defaultRecipe 默认食谱
    # favoriteRecipe 收藏食谱
    # topRecipe 自选食谱

    url_path = '/v1/recipe/manager/my'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeslist_success(self):
        '''所有参数都传'''
        payload = {'deviceid': '57381615'}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']
            print js['result'][i]['recipe']['icon']
            print js['result'][i]['recipe']['advIcon']





