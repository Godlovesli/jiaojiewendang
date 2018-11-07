#coding:utf-8
# __author__ = 'feng'
from base.cjbase import CJMyTest
import json
import urllib, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from base.CJcryp import *
class recipeCommentaddTest(CJMyTest):
    '''食谱评论'''
    url_path = '/v6/recipeComment/addRecipeComment'


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipeCommentadd_success(self):
        '''所有字段都传'''
        r = self.cjmyhttp('POST',
                        self.url_path,
                         {'recipeId':1967,'content':'good111','stars':0,'language':self.language},
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn( '发表成功',js['message'])


    def test_recipeCommentadd_success1(self):
        '''所有字段都传'''
        r = self.cjmyhttp('POST',
                          self.url_path,
                          {'deviceId': '12755445', 'recipeId': 256, 'content': 'good', 'stars': 0, 'language': 'english','parent_id':9964},
                          )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('发表成功', js['message'])


class recipeCommentpagegetTest(CJMyTest):
    '''食谱评论页'''
    url_path = '/v6/recipeComment/listdata'


    @classmethod
    def setUpClass(cls):
        pass


    def test_recipelistdata_success11(self):
        '''食谱列表'''
        # 评论页，评论用户的显示规则:中文：饭煲用户;香港/台湾：用戶;
        #'language'不传或者传空值时，为中文，显示：饭煲用户
        # 'language'传 zh_TW（台湾）或 zh_HK（香港）时，显示：用戶
        #  'language'传 其他语言 时，显示：User

        # self.url_path = 'http://10.0.10.100:17001/v6/recipeComment/listdata'
        self.url_path = 'https://rumipotplugapi.joyami.com/v6/recipeComment/listdata'
        url = self.url_path
        self.signature = generateSignature(self.nonce, "GET", url)
        params = urllib.urlencode({'recipeId': 1967,'language': self.language})
        encoded = encryptAES(params, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': self.signature
                   }
        # url2 = url
        url2 = url + '?' + params
        print url2
        request = urllib2.Request(url2, headers=headers)
        print request
        response = urllib2.urlopen(request)
        print response
        result = response.read()
        js = json.loads(result)
        print js

        for i in range(len(js['list'])):
            print js['list'][i]['content']


