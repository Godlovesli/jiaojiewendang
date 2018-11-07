#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipeinfoTest(CJMyTest):
    '''获取食谱详情信息'''
    url_path = '/v6/recipe/web/info/615'

    @classmethod
    def setUpClass(cls):
        pass


    def test_recipeinfo_success(self):
        '''获取食谱信息成功'''
        r = self.cjbujiami('GET',
                         self.url_path,
                         {'': ''},
                         )

        print r


