# -*- coding: utf-8 -*-
import base64
import random
import time
import struct
import hashlib
from Crypto.Cipher import AES
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

"""
created by 王丹华 Tue, 12 Jul 2016 11:07:05 +0800
"""

__all__ = ["generateNonce", "generateSignature", "getSessionSecurity", "encryptAES", "decryptAES"]
# 插件版
app_id = '10005'
app_key = 'W7v4D60fds2Cmk2U'
# 独立版
# app_id = '10006'
# app_key = 'mJxhaXrFSZzNCUnP'

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]


def encryptBase64(src):
    return base64.urlsafe_b64encode(src).strip().replace("\n", "").replace("\r", "");


def decryptBase64(src):
    return base64.urlsafe_b64decode(src)


def md5(src):
    return hashlib.md5(src).hexdigest().upper()


def sha256(src):
    return hashlib.sha256(src).digest()


def sha1(src):
    return hashlib.sha1(src).digest()


def getSessionSecurity(src):
    """
    生成AES key
    """
    nonce = decryptBase64(src)
    return sha256(app_key + nonce)


def encryptAES(src, key):
    """
    生成AES密文
    """
    iv = bytearray([117, 2, 3, 11, 105, 78, 90, 110, 112, 56, 78, 23, 41, 58, 93, 96])
    cryptor = AES.new(key, AES.MODE_CBC, str(iv))
    ciphertext = cryptor.encrypt(pad(src))
    return encryptBase64(ciphertext)


def decryptAES(src, key):
    """
    解析AES密文
    """
    src = decryptBase64(src)
    iv = bytearray([117, 2, 3, 11, 105, 78, 90, 110, 112, 56, 78, 23, 41, 58, 93, 96])
    cryptor = AES.new(key, AES.MODE_CBC, str(iv))

    text = cryptor.decrypt(src);
    return unpad(text)


def generateNonce():
    """
    生成nonce
    """
    src = bytearray()

    for i in range(8):
        src.append(random.randint(0, 255))

    mill = int(round(time.time() * 1000))

    t = struct.pack(">i", mill / 60000)

    src.extend(t)

    result = encryptBase64(src)

    return result


def generateSignature(nonce, httpmethod, httpurl):
    """
    生成signature
    """
    s1 = encryptBase64(sha256(app_key + nonce))
    s2 = httpmethod + "&" + httpurl + "&" + "app_id=" + app_id + "&" + s1
    print('s2的值:'+s2)
    return encryptBase64(sha1(s2))


if __name__ == "__main__":
    import urllib, urllib2
    import json

    base = "http://framipotplugapi.joyami.com"
    # base = "http://10.0.10.100:17001"
    url = "/v6/device/regdevice"
    # url = '/v6/device/global/regdevice'
    post_url = base + url
    print(post_url)
    nonce = generateNonce()
    print('nonce的值：'+nonce)
    signature = generateSignature(nonce, "POST", post_url)
    print('加密：'+nonce+ "&" +  "POST"+ "&" +  post_url)
    print('signature的值：'+signature)
    A = 'latitude=31.185258&language=taiwan&ownerId=&userId=271045941&deviceid=7182018&deviceId=1083258&mac=64:09:80:2E:8E:ED&modelName=chunmi.cooker.press1&ownerName=&cityName=上海&name=米家壓力IH電鍋&longitude=121.598745&online=true'
    print('参数：'+ A)
    key = getSessionSecurity(nonce)
    print('key的值 :'+key)
    encoded = encryptAES(A, key)
    print('加密的内容：'+encoded)
    data = {"data": encoded}
    payload = urllib.urlencode(data)  # 把参数进行编码
    request = urllib2.Request(post_url, data=payload)  # 用.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
    request.add_header("nonce", nonce)
    request.add_header("signature", signature)
    request.add_header("User-Agent", "chunmiapp")
    response = urllib2.urlopen(request)  # 用.urlopen打开上一步返回的结果，得到请求后的响应内容
    result = response.read()  # 将响应结果用read()读取出来
    print result
    r = decryptAES(result, key)
    print "解密的结果：" + r
    # js = json.loads(r)
    # print js
    # self.assertEqual(js['state'], 1)
    # self.assertIn(u'注册设备成功', js['message'])