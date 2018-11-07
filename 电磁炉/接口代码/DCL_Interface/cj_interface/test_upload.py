#coding:utf-8
# __author__ = 'feng'
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class uploadTest(unittest.TestCase):
    '''上传文件'''


    def setUp(self):
        # self.base_url = 'https://testapi2.coo-k.com'
        # self.base_url = 'https://capi.joyami.com'
        self.base_url = 'http://10.0.10.100:17011'
        self.url_path = '/file/upload'



    def test_upload_success(self):
        '''上传文件成功'''
        # url = self.base_url + self.url_path
        # headers = { "Accept": "application/json;charset=UTF-8",
        #            # 'User-Agent': 'chunmiapp',
        #            # 'signature': self.signature
        #            }
        # files = {'filename': open(r'D:\test.jpg', 'rb')}
        # r = requests.post(url, files=files)
        # print r
        # result = r.text
        # print result
        # js = json.loads(result)
        # self.assertEqual(js['code'], 1)


