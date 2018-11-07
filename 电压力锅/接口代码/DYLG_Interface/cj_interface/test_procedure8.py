#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class procedure8Test(MyTest):
    '''流程8'''
    # 添加一条评论-获取最新评论(2条)的第一条
    # 添加一条评论-获取最新评论(分页)的第一条


    @classmethod
    def setUpClass(cls):
        pass

    def test_procedure8_success(self):
        '''所有参数都传'''
        contents= 'good'
        url_path1 = '/v1/recipecomment/add'
        payload = {'deviceId': '57357285', 'recipeId': 1294, 'contents': contents}
        r = self.myhttp('POST',
                        url_path1,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertIn('success', js['message'])

        url_path2 = '/v1/recipecomment/toptwo'
        payload2 = {'recipeid': '1294'}
        r2 = self.myhttp('GET',
                        url_path2,
                        payload2,
                        )

        print r2
        js2 = json.loads(r2)
        self.assertEqual(js2['code'], 1)
        # self.assertEqual(js2['message'], 'success')
        self.assertEqual(js2['result'][0]['contents'],contents)
        comment_id=js2['result'][0]['id']

        url_path3 = '/v1/recipecomment/more'
        payload3 = {'recipeid': '1294'}
        r3 = self.myhttp('GET',
                        url_path3,
                        payload3,
                        )
        print r3
        js3 = json.loads(r3)
        self.assertEqual(js3['code'], 1)
        self.assertEqual(comment_id,js3['result'][0]['id'])
        self.assertEqual(contents, js3['result'][0]['contents'])

