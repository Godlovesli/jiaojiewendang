#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class commentinfoTest(MyTest):
    '''获取评论详情(页面)'''
    url_path = '/v1/recipecomment/web/info/23077'

    @classmethod
    def setUpClass(cls):
        pass

    def test_commentinfo_success(self):
        '''所有必填字段都传'''
        payload = {'language': ''}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )

        print r



