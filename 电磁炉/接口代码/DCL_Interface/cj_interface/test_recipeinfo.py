#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipeinfoTest(MyTest):
    '''获取食谱详情（页面）'''
    url_path = '/v1/recipe/web/info/23077'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeinfo_success(self):
        '''所有参数都传'''
        payload = {'deviceid':'53256503'}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )

        print r




