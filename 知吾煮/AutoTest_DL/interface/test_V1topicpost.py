#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# -*- __author__ = 'feng' -*-
from base.base import MyTest
from base.login import Login
import unittest
import json
from HTMLTestRunner import HTMLTestRunner
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class V1topicpostTest(MyTest):
    '''发布主题'''
    url_path = '/v1/topic/post'

    @classmethod
    def setUpClass(cls):
        pass

    def test_topicpost_success(self):
        '''所有信息都发布'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                        self.url_path,
                        {"title": "test",
                         "content": "test",
                         "images": [{"url": "/static/indenpendent/recipe/2360/a1b966aed9f74854941ef9a564a10c19.JPG", "sort": 1,
                                     "uploadTime": 1473141942000},
                                    {"url": "/static/indenpendent/recipe/2486/7bdc8ba97af24cc9bc8c33ee91d119a1.jpg", "sort": 2,
                                     "uploadTime": 1473141950000}],
                         "recipeId": 258
                         },
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('发布成功',js['message'])

    def test_topicpost_success1(self):
        '''图片的uploadTime未传，可发布成功'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                        self.url_path,
                           {"title": "test2233",
                            "content": "test2233",
                            "images": [{"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 1},
                                       {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 2}],
                            "recipeId": 258  # 如果没有关联食谱、则不加此参数
                            },
                        token
                        )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('发布成功',js['message'])


    def test_topicpost_success2(self):
        '''图片的sort未传，可发布成功'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {"title": "test55",
                            "content": "test55",
                            "images": [
                                {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg",
                                 "uploadTime": 1473141942000},
                                {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg",
                                 "uploadTime": 1473141950000}],
                            "recipeId": 258
                            },
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('发布成功', js['message'])


    def test_topicpost_success3(self):
        '''recipeId未传，可发布成功'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {"title": "test33",
                            "content": "test33",
                            "images": [{"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 1},
                                       {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 2}]
                            },
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('发布成功', js['message'])


    def test_topicpost_ttlose(self):
        '''title未传'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {"content": "test66",
                            "images": [{"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg","sort": 1 },
                                    {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg","sort": 2}]
                              },
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('添加话题失败', js['message'])

    def test_topicpost_ttnull(self):
        '''title的值为空'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {"title": "",
                            "content": "test66",
                            "images": [{"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg","sort": 1 },
                                    {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg","sort": 2}]
                              },
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('发布成功', js['message'])



    def test_topicpost_ttpsnull(self):
        '''title参数为空'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {"": "title",
                            "content": "test66",
                            "images": [{"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg","sort": 1 },
                                    {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg","sort": 2}]
                              },
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('添加话题失败', js['message'])



    def test_topicpost_imlose(self):
        '''images未传'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                        {"title": "title",
                        "content": "test66"
                        },
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('发布成功', js['message'])



    def test_topicpost_imnull(self):
        '''images的值为空'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                          {"title": "title1",
                           "content": "test66",
                           "images": ""
                           },
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -1)
        self.assertIn('添加话题失败', js['message'])

    def test_topicpost_impanull(self):
        '''images参数为空'''

        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {"title": "title1",
                            "content": "test66",
                            "": [{"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 1},
                                 {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 2}]
                            },
                           token
                           )
        print r
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn('发布成功', js['message'])


    def test_topicpost_tokennull(self):
        '''token不传'''
        r = self.topicpost1('POST',
                           self.url_path,
                           {"title": "title1",
                            "content": "test66",
                            "images": [{"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 1},
                                 {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 2}]
                            }, )

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])


    def test_topicpost_tokenerror(self):
        '''token错误'''
        token = Login().login()  # 引用登录
        print token
        r = self.topicpost('POST',
                           self.url_path,
                           {"title": "title1",
                            "content": "test66",
                            "images": [{"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 1},
                                       {"url": "/static/recipe/0825707b6d674e538dccdd4c51c3381c.jpg", "sort": 2}]
                            },
                           token+'ee')

        print r
        js = json.loads(r)
        self.assertEqual(js['state'], -3)
        self.assertIn('token无效', js['message'])