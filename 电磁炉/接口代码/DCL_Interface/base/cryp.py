# -*- coding: utf-8 -*-
import base64
import random
import time
import hashlib
from Crypto.Cipher import AES

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 电磁炉
app_id  = 'com.chunmi.ihcooker'

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

def md5(src):
    return hashlib.md5(src).hexdigest().upper()

def encryptBase64(src):
    return base64.urlsafe_b64encode(src).strip().replace("\n", "").replace("\r", "");


def decryptBase64(src):
    return base64.urlsafe_b64decode(src)



def sha1(src):
    return hashlib.sha1(src).digest()




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

    # mill = int(round(time.time() * 1000))
    #
    # t = struct.pack(">i", mill / 60000)
    #
    # src.extend(t)

    result = encryptBase64(src)
    return result


def generateSignature(app_id, httpmethod, httpurl):
    """
    生成signature
    """
    s2 = httpmethod + "&" + httpurl + "&" + "app_id=" + app_id
    return encryptBase64(sha1(s2))


if __name__ == "__main__":
    import urllib, urllib2,requests,json

    appid = "com.chunmi.ihcooker"
    base_url='http://10.0.10.100:17011'
    url = "/v1/recipe/collect/createglobal"
    post_url=base_url+url
    print post_url
    signature = generateSignature(appid,"POST",url)
    a='name=áéíóúÁÉÍÓÚ&firePower=26&duration=60&temperature=0&deviceid=71477071'
    b= encryptBase64(a)
    print b
    print signature
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
        "signature": signature}
    data = {'data': b,'language':'es_ES'}
    r = requests.post(post_url, data=data, headers=headers)
    result = r.text.encode()
    print result
