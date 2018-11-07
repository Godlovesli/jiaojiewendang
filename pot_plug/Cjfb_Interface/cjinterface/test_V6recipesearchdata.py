#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class recipesearchdataTest(CJMyTest):
    '''食谱搜索列表'''
    url_path = '/v6/recipe/searchdata'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipeslist_success(self):
        '''所有字段都传'''
        r = self.cjbujiami('GET',
                        self.url_path,
                           {'perpage': 500, 'pageno': 1, 'deviceid': 46666777, 'language': '', 'name': '银耳', 'type': ''},


                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 0)
        print len(js['result'])
        for i in range(len(js['result'])):
            if js['result'][i]['name'] != None:
                print js['result'][i]['recipeId']
                print js['result'][i]['name']



