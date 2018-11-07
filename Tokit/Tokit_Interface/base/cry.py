#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 10:36
# @Author  : fengguifang
# @File    : cry.py
# @Software: PyCharm
import base64
import hashlib


app_id  = 'com.chunmi.tokit'

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]


def md5(src):
    return hashlib.md5(src.encode()).hexdigest().upper()

def encryptBase64(src):
    return str(base64.urlsafe_b64encode(src),'utf-8').strip().replace("\n", "").replace("\r", "");


def generateSignature(app_id, httpmethod, httpurl):
    """
    生成signature
    """
    s2 = httpmethod + "&" + httpurl + "&" + "app_id=" + app_id
    print (s2)
    return encryptBase64(hashlib.sha1(s2.encode('utf-8')).digest())


if __name__ == "__main__":
    import requests
    a='GET&/user/check/18721587248&app_id=com.chunmi.tokit'
    print(generateSignature('app_id=com.chunmi.tokit','GET','/user/check/18721587248'))
    base_url = 'http://10.0.10.100:8704'
    self_url = "/user/rpc/batch/query"
    url = base_url + self_url
    app_id = 'com.chunmi.tokit'
    signature = generateSignature(app_id, "POST", self_url)
    headers = {'Content-Type': 'application/json',
               "signature": signature}
    data =[{'userids':[10,11]}]
    r = requests.post(url, data=data, headers=headers)
    result = r.text
    print(result)
