#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipeweblistTest(CJMyTest):
    '''食谱列表'''
    url_path = '/v6/recipe/web/list'


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeweblist_success(self):
        '''食谱列表'''
        r = self.cjbujiami('GET',
                        self.url_path,
                         {'deviceid': self.deviceId},

                         )
        print r


