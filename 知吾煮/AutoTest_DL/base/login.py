#_*_ coding:utf-8 _*_
import requests
import unittest
import json
import time
from HTMLTestRunner import HTMLTestRunner
import random
import MySQLdb
from cryptutil import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 类定义
class Login:

    def login(self):
    #
        # self.loginurl = 'https://member.joyami.com/api/customer/v3/login.do'
        # # self.loginurl = 'http://10.0.10.99:17005/api/customer/v3/login.do'
        # self.md5key = 'AB14EF83C9204C268CA764AAF49D4D787C025837%$#@$&^%$@5610216-428D8A82-090E25849C03'
        # self.mobile = '18217739372'
        # self.userName = '1025'
        # # self.password = '25F9E794323B453885F5181F1B624D'
        # self.password='1E7CA4495801FC3A008EBB6D65D37017'
        # self.deviceID = 'ffffffff-d5ed-00c5-ffff-ffffc2b256'
        # self.loginType = 'mobile'
        # self.xiaomiun ='54644930'
        # self.random = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 6))
        # md5key = 'md5key=' + self.md5key
        # # password = 'password=' + self.password
        # # loginType = 'loginType=' + self.loginType
        # mobile = 'mobile=' + self.mobile
        # deviceID = 'deviceID=' + self.deviceID
        # random1 = 'random=' + self.random
        # xiaomiun = 'xiaomiun=' + self.xiaomiun
        # sign = md5key + '&' + deviceID + '&' + mobile + '&' + random1+ '&' + xiaomiun
        # self.sign = md5(sign)
        # payload = {'mobile': self.mobile,
        #            # 'password': self.password,
        #            'xiaomiun':self.xiaomiun,
        #            'deviceID': self.deviceID,
        #            # 'loginType': self.loginType,
        #            'random': self.random}
        # jdata = json.dumps(payload)
        # headers = {'Content-Type': 'application/json', 'sign': self.sign}
        # r = requests.post(self.loginurl, data=jdata, headers=headers,verify=False)
        # # print r
        # result = r.text
        # print result
        # js = json.loads(result)
        #
        # # token = js['result']['token']
        # # print token
        #
        # if js['message']=='成功':
        #     token = js['result']['token']
        #     print token
        # else:
        #     db = MySQLdb.connect("10.0.10.61", "root", "chunmitest", "usercenter")  # 打开数据库连接
        #     cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        #     sql = "SELECT * from login_record where mobile='18217739372' and userName='1025' ORDER BY loginTime DESC"
        #     data_count = cursor.execute(sql)
        #     cursor.scroll(0)
        #     rows = cursor.fetchone()
        #     token = rows['token']
        #
        # return token

        # token='ZDlhZWYxYWE3NmEzMDc5NzI5NGE3YjNiNDFlNWZlMGI='
        # return token

        token='MmE3NDllMjFkODJlMWI3MjgzZjU0M2EwZmZkZTZmY2I='  #正式环境
        return token


if __name__ == "__main__":
    p = Login()
    print p.login()





