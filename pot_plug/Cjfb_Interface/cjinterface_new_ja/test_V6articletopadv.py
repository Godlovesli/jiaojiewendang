#coding:utf-8
# -*- __author__ = 'feng' -*-
from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class articletopadvTest(CJMyTest):
    '''获取banner（6100首页,6200列表）'''
    # url_path = '/v4/article/topadv'
    url_path = '/v6/article/topadv'

    @classmethod
    def setUpClass(cls):
        pass

    def test_articletopadv_sysuccess(self):
        '''传所有参数,获取6100列表'''
        r = self.cjmyhttp('GET',
                         self.url_path,
                          {'type': '6100', 'language': 'ja_JP', 'deviceid': '91529315'},
                          # {'type': '6100', 'language': '', 'deviceid':'71617463' },
                         )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('banner数据获取成功', js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['id']

    # def test_articletopadv1_sysuccess(self):
    #     '''传所有参数,获取6100列表'''
    #     # # db = MySQLdb.connect("192.168.1.64", "root", "123456", "new_independent_api")  # 打开数据库连接
    #     # db = MyDB().getCon()
    #     # cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    #     # sql = "SELECT * FROM mipot_article WHERE type = '6200'and state='2200' and  devicemodelid='1'"
    #     # data_count = cursor.execute(sql)
    #     # print data_count
    #     # cursor.scroll(0, 'absolute')
    #     # rows = cursor.fetchall()
    #     # print rows
    #     # for row in rows:
    #     #     print row
    #     self.url = self.base_url + self.url_path
    #     print self.url
    #     self.signature = generateSignature(self.nonce, "GET", self.url)
    #     params = urllib.urlencode({'type': '6100','language': 'en_US','deviceid':46666777})
    #     print '传入的参数:'+ params
    #     encoded = encryptAES(params, self.key)
    #     datas = {'data': encoded}
    #     payload = urllib.urlencode(datas)
    #     url2 = self.url + '?' + payload
    #     request = urllib2.Request(url2)
    #     request.add_header('nonce', self.nonce)
    #     request.add_header('User-Agent', 'chunmiapp')
    #     request.add_header('signature', self.signature)
    #     response = urllib2.urlopen(request)
    #     result = response.read()
    #     print result
    #     r =decryptAES(result,self.key)
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['state'], 1)
    #     self.assertIn('banner数据获取成功', js['message'])
    #     print len(js['result'])
    #     for i in range(len(js['result'])):
    #         print js['result'][i]['id']
    #
    # def test_articletopadv_sysuccess1132(self):
    #     '''传所有参数,获取6200列表'''
    #     self.url = 'https://capi.joyami.com/v6/recipe/collect/list'
    #     self.signature = generateSignature(self.nonce, "GET", self.url)
    #     params = urllib.urlencode({'language': 'english', 'deviceid': 1083258})
    #     print '传入的参数:' + params
    #     encoded = encryptAES(params, self.key)
    #     datas = {'data': encoded}
    #     payload = urllib.urlencode(datas)
    #     url2 = self.url + '?' + payload
    #     request = urllib2.Request(url2)
    #     request.add_header('nonce', self.nonce)
    #     request.add_header('User-Agent', 'chunmiapp')
    #     request.add_header('signature', self.signature)
    #     response = urllib2.urlopen(request)
    #     result = response.read()
    #     print result
    #     r = decryptAES(result, self.key)
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['state'], 1)
    #     self.assertIn('banner数据获取成功', js['message'])
    #
    # def test_articletopadv_sysuccess11(self):
    #     '''传所有参数,获取6200列表'''
    #     self.url = 'http://10.0.10.100:17001/v6/article/topadv'
    #     self.signature = generateSignature(self.nonce, "GET", self.url)
    #     params = urllib.urlencode({'type': '6100','language': 'ru_RU', 'deviceid': 53046831})
    #     print '传入的参数:' + params
    #     encoded = encryptAES(params, self.key)
    #     datas = {'data': encoded}
    #     payload = urllib.urlencode(datas)
    #     url2 = self.url + '?' + payload
    #     request = urllib2.Request(url2)
    #     request.add_header('nonce', self.nonce)
    #     request.add_header('User-Agent', 'chunmiapp')
    #     request.add_header('signature', self.signature)
    #     response = urllib2.urlopen(request)
    #     result = response.read()
    #     print result
    #     r = decryptAES(result, self.key)
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['state'], 1)
    #     self.assertIn('banner数据获取成功', js['message'])
    #
    #
    # def test_articletopadv_sysuccess112(self):
    #     '''传所有参数,获取6200列表'''
    #     self.url = 'https://capi.joyami.com/v6/article/topadv'
    #     self.signature = generateSignature(self.nonce, "GET", self.url)
    #     params = urllib.urlencode({'type': '6100', 'language': 'taiwan', 'deviceid': 53028356})
    #     print '传入的参数:' + params
    #     encoded = encryptAES(params, self.key)
    #     datas = {'data': encoded}
    #     payload = urllib.urlencode(datas)
    #     url2 = self.url + '?' + payload
    #     request = urllib2.Request(url2)
    #     request.add_header('nonce', self.nonce)
    #     request.add_header('User-Agent', 'chunmiapp')
    #     request.add_header('signature', self.signature)
    #     response = urllib2.urlopen(request)
    #     result = response.read()
    #     print result
    #     r = decryptAES(result, self.key)
    #     print r
    #     js = json.loads(r)
    #     self.assertEqual(js['state'], 1)
    #     self.assertIn('banner数据获取成功', js['message'])