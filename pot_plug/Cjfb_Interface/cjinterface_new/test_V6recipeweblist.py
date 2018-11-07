#coding:utf-8
# __author__ = 'feng'
from base.cjbase1 import CJMyTest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipeweblistTest(CJMyTest):
    '''食谱列表'''
    url_path = '/v6/recipe/web/listByModelName'


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeweblist_success(self):
        '''食谱列表'''
        r = self.cjbujiami('GET',
                        self.url_path,
                        {'model': self.model_name, 'language': self.language},

                         )
        print r
