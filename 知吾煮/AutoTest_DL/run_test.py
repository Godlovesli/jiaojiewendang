 # !/usr/bin/python
# -*- coding: utf-8 -*-


import time,sys
sys.path.append('./interface')
#sys.path.append('./db_fixture')
import unittest
from HTMLTestRunner import HTMLTestRunner


# 指定测试用例为当前文件夹下的 interface 目录
# test_dir = './interface'
# test_dir='./V1wode'
test_dir='./V1chuyiguangchang'
discover = unittest.defaultTestLoader.discover(test_dir,pattern ='test_*.py')


if __name__ == "__main__":

	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './report/' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp,
							title=u'独立版接口测试报告',
							description= u'用例执行情况：')
	runner.run(discover)
	fp.close()