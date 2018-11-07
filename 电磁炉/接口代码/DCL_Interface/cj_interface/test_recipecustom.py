#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class recipecustomTest(MyTest):
    '''自定义模式列表'''
    url_path = '/v1/recipe/collect/custom'

    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecustom_success1(self):
        '''所有参数都传'''
        payload = {'deviceid': self.deviceId, 'pageno': 1, 'perpage': 100}
        r = self.myhttp('GET',
                         self.url_path,
                        payload,
                         )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'],1)
        print "打印自定义模式列表个数：%d" %len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['recipe']['name']
            # print js['result'][i]['recipe']['id']



