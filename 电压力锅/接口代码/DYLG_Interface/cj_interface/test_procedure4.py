#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class procedure4Test(MyTest):
    '''流程4'''
    # 恢复默认设置-获取我的模式 得到的默认模式一致


    @classmethod
    def setUpClass(cls):
        pass

    def test_procedure4_success(self):
        '''所有参数都传'''
        url_path1 = '/v1/recipe/manager/reset'
        payload = {'deviceid': '57357285'}   #57357235
        r = self.myhttp('POST',
                        url_path1,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        resert_recipe=[]
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            resert_recipe.append(js['result'][i]['recipe']['name'])
        print resert_recipe


        url_path = '/v1/recipe/manager/my'
        payload = {'deviceid': '57357285'}
        r = self.myhttp('GET',
                        url_path,
                        payload,
                        )

        print r
        js1 = json.loads(r)
        self.assertEqual(js1['code'], 1)
        my_recipe=[]
        for i in range(len(js1['result'])):
            print js1['result'][i]['recipe']['name']
            my_recipe.append(js1['result'][i]['recipe']['name'])
        print my_recipe
        self.assertEqual(my_recipe,resert_recipe)  # 重置后得到的食谱和我的模式列表食谱一致

