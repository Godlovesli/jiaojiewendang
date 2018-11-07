#coding:utf-8
# __author__ = 'feng'
from base.base import MyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')





class recipecreateTest(MyTest):
    '''创建一个自定义模式'''
    url_path = '/v1/recipe/collect/create'    #根据设备ID创建一个(模式|食谱),当创建的是一个模式时候,textureId(口感),practiceId(做法),ingredientId(食材),为必填参数


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipecreate_success(self):
        '''创建一个自定义模式'''
        payload = {'deviceid': '57357285',
                   'name': '糯米',
                   'duration': 40,
                   'ingredientId':3,
                   'practiceId':1,
                   'textureId': 6
                   }
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertIn('success',js['message'])



    def test_recipecreate_didwc(self):
        '''deviceid未传'''
        payload = {
                   'name': 'testtest',
                   'duration': 20,
                   'ingredientId':4,
                   'practiceId':4,
                   'textureId': 4
                   }
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], -1)
        self.assertIn("parameter 'deviceid' is not present",js['message'])



    def test_recipecreate_drwc(self):
        '''duration未传'''
        payload = {'deviceid': '57357285',
                   'name': 'testtest',
                   'duration': '',
                   'ingredientId':4,
                   'practiceId':4,
                   'textureId': 4
                   }
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 1)
        # self.assertIn('success',js['message'])


    def test_recipecreate_igwc(self):
        '''ingredientId未传'''
        payload = {'deviceid': '57357285',
                   'name': 'testtest',
                   'duration': '20',
                   'ingredientId': '',
                   'practiceId': 4,
                   'textureId': 4
                   }
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 404)
        self.assertIn(u'模式的口感,食材,做法不能为空', js['message'])

    def test_recipecreate_pidwc(self):
        '''ingredientId未传'''
        payload = {'deviceid': '57357285',
                   'name': 'testtest',
                   'duration': '20',
                   'ingredientId': 4,
                   'practiceId': '',
                   'textureId': 4
                   }
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 404)
        self.assertIn(u'模式的口感,食材,做法不能为空', js['message'])



    def test_recipecreate_tidwc(self):
        '''ingredientId未传'''
        payload = {'deviceid': '57357285',
                   'name': 'testtest',
                   'duration': '20',
                   'ingredientId': 4,
                   'practiceId': 4,
                   'textureId': ''
                   }
        r = self.myhttp('POST',
                        self.url_path,
                        payload,
                        )

        print r
        js = json.loads(r)
        self.assertEqual(js['code'], 404)
        self.assertIn(u'模式的口感,食材,做法不能为空', js['message'])