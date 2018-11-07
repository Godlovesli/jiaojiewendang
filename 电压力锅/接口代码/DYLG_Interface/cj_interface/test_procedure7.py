#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class procedure7Test(MyTest):
    '''流程7'''
    # 创建一个自定义模式-批量删除自定义-获取我的模式最近使用的集合，删除后，最近使用中不显示


    @classmethod
    def setUpClass(cls):
        pass

    def test_procedure7_success(self):
        '''所有参数都传'''
        url_path1 = '/v1/recipe/collect/create'
        payload = {'deviceid': '57357285',
                   'name': '创建自定义模式',
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

        url_path2 = '/v1/recipe/collect/del'
        payload2 = payload = {'deviceid': '57357285',
                   'recipeids': create_custom_id
                   }
        r2 = self.myhttp('POST',
                        url_path2,
                        payload2,
                        )

        print r2
        js2 = json.loads(r2)
        self.assertEqual(js2['code'], 1)
        # self.assertEqual(js2['message'], 'success')


        url_path3 = '/v1/recipe/manager/mylist'
        payload3 = {'deviceid': '57357285', 'pageno': 1, 'perpage': 10}
        r3 = self.myhttp('GET',
                        url_path3,
                        payload3,
                        )
        print r3
        js3 = json.loads(r3)
        self.assertEqual(js3['code'], 1)
        custom_id = []
        for i in range(len(js3['result'])):
            print js3['result'][i]['recipe']['name']
            print js3['result'][i]['recipe']['id']
            custom_id.append(js3['result'][i]['recipe']['id'])
        print custom_id
        print create_custom_id not in custom_id  # 删除后的自定义模式不存在于 我的模式最近使用的集合
        self.assertIs(create_custom_id not in custom_id, True)

