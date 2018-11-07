#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class procedure5Test(MyTest):
    '''流程5'''
    # 创建一个自定义模式-获取我的模式最近使用的集合，创建后在列表中存在


    @classmethod
    def setUpClass(cls):
        pass

    def test_procedure5_success(self):
        '''所有参数都传'''
        url_path1 = '/v1/recipe/collect/create'
        payload = {'deviceid': '57357285',
                   'name': 'testtest',
                   'duration': 20,
                   'ingredientId': 1,
                   'practiceId': 4,
                   'textureId': 7
                   }
        r = self.myhttp('POST',
                        url_path1,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertIn('success', js['message'])
        create_custom_id=js['result']['recipe']['id']
        print create_custom_id

        url_path2 = '/v1/recipe/manager/mylist'
        payload2 = {'deviceid': '57357285', 'pageno': 1, 'perpage': 10}
        r2 = self.myhttp('GET',
                        url_path2,
                        payload2,
                        )
        print r2
        js2 = json.loads(r2)
        self.assertEqual(js2['code'], 1)
        ID = []
        for i in range(len(js2['result'])):
            print js2['result'][i]['recipe']['name']
            print js2['result'][i]['recipe']['id']
            ID.append(js2['result'][i]['recipe']['id'])
        print ID
        print create_custom_id in ID   # 增加的自定义模式ID存在于 我的模式最近使用的集合
        self.assertIs(create_custom_id in ID, True)


