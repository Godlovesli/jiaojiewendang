# -*- coding:utf-8 -*-
import sys

import MySQLdb


class MyDB:
    #获取数据库连接
    def getCon(self):
        try:
            # conn=MySQLdb.connect("10.0.10.64","root", "123456", "new_independent_api")
            conn = MySQLdb.connect("10.0.10.100", "root", "chunmi456", "indenpendent_test")
            return conn
        except MySQLdb.Error,e:
            print "Mysqldb Error:%s" % e
            sys.exit()


