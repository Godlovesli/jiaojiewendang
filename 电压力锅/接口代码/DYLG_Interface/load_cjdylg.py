#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 13:59
# @Author  : fengguifang
# @File    : load_cjdylg.py
# @Software: PyCharm

# > locust -f .\load_cjdylg.py
# 通过浏览器访问：http://localhost:8089（Locust启动网络监控器，默认为端口号为: 8089）

from locust import *

class mytest(TaskSet):

    @task(weight=1)
    def transaction_1(self):
        with self.client.get(name='article_topadv', url='/v1/article/topadv?deviceid=57357285&type=6100&language=', catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('error')



    @task(weight=1)
    def transaction_2(self):
        with self.client.get(name='ingredient_list', url='/v1/recipe/ingredient/list?language=',
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('error')


    @task(weight=1)
    def transaction_3(self):
        with self.client.get(name='managermy', url='/v1/recipe/manager/my?deviceid=57357285&language=',
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('error')


    @task(weight=1)
    def transaction_4(self):
        with self.client.get(name='recipe_detail', url='/v1/recipe/detail?deviceid=57357285&recipeid=1830&language=',
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('error')



    @task(weight=1)
    def transaction_5(self):
        with self.client.get(name='practice_list', url='/v1/recipe/practice/list?ingredientid=2&language=',
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('error')


    @task(weight=1)
    def transaction_6(self):
        with self.client.get(name='texture_list', url='/v1/recipe/texture/list?ingredientid=1&practiceid=2&language=',
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('error')



class myrun(HttpLocust):
    task_set = mytest
    host = 'http://10.0.10.100:17201'