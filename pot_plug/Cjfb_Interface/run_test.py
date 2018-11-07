 # !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time,sys
sys.path.append('./v7interface')

import unittest
from HTMLTestRunner_cn import HTMLTestRunner
# test_dir='./cjinterface_new'  #v7interface
proPath = os.path.dirname(os.path.realpath(__file__))
reportPath = os.path.join(proPath, "report")
test_dir=os.path.join(proPath,"v7interface")
discover = unittest.defaultTestLoader.discover(test_dir,pattern ='test_*.py')
if __name__ == "__main__":

	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = reportPath + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp,
							title=u'饭煲接口测试报告',
							description= u'用例执行情况：',
	                        verbosity = 2

							)
	runner.run(discover)
	fp.close()
