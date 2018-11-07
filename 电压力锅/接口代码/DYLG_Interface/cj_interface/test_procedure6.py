#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class procedure6Test(MyTest):
    '''流程6'''
    # 创建一个自定义模式-编辑自定义模式-获取我的模式最近使用的集合，编辑后，最近使用中显示编辑的名称


    @classmethod
    def setUpClass(cls):
        pass

    def test_procedure6_success(self):
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
        print  js
        self.assertEqual(js['code'], 1)

        create_custom_id= js['result']['recipe']['id']
        create_custom_name = js['result']['recipe']['name'].decode("utf8","ignore")

        print create_custom_name
        print create_custom_id

        url_path2 = '/v1/recipe/collect/edit'
        payload2 = {'deviceid': '57357285', 'id': create_custom_id, 'name': '编辑自定义aaa', 'duration': 10}
        r2 = self.myhttp('POST',
                        url_path2,
                        payload2,
                        )

        print r2
        js2 = json.loads(r2)
        self.assertEqual(js2['code'], 1)
        edit_custom_name = js2['result']['recipe']['name']
        print edit_custom_name
        url_path3 = '/v1/recipe/manager/mylist'
        payload3 = {'deviceid': '57357285', 'pageno': 1, 'perpage': 10}
        r3 = self.myhttp('GET',
                        url_path3,
                        payload3,
                        )
        print r3
        js3 = json.loads(r3)
        self.assertEqual(js3['code'], 1)
        custom_name = []
        for i in range(len(js3['result'])):
            print js3['result'][i]['recipe']['name']
            print js3['result'][i]['recipe']['id']
            custom_name.append(js3['result'][i]['recipe']['name'])
        print custom_name
        print edit_custom_name in custom_name  # 修改后的自定义模式名称存在于 我的模式最近使用的集合
        self.assertIs(edit_custom_name in custom_name, True)


