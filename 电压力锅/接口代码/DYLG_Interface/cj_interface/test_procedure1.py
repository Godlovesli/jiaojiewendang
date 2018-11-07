#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
requests.packages.urllib3.disable_warnings()

class procedure1Test(MyTest):
    '''流程1'''
    # 设置收藏-获取我的模式最近使用的集合 存在



    @classmethod
    def setUpClass(cls):
        pass

    def test_procedure1_success(self):
        '''所有参数都传'''
        recipeid=2059 #1300
        url_path1 = '/v1/recipe/manager/op'
        payload1 = {'deviceid': '57381615', 'recipeid':recipeid, 'flag': 1}
        r1 = self.myhttp('POST',
                         url_path1,
                        payload1,
                         )

        print r1
        js1 = json.loads(r1)
        self.assertEqual(js1['code'], 1)

        url_path = '/v1/recipe/manager/mylist'
        payload = {'deviceid': '57381615', 'pageno': 1, 'perpage': 10}
        r = self.myhttp(
                        'GET',
                        url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        ID = []
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            print js['result'][i]['recipe']['id']
            ID.append(js['result'][i]['recipe']['id'])
        print ID
        print recipeid in ID
        self.assertIs(recipeid in ID,True)
