#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 17:29
# @Author  : fengguifang
# @File    : dcl_cry.py
# @Software: PyCharm
import base64
import random
import hashlib
from Crypto.Cipher import AES

__all__ = ["generateNonce", "generateSignature",  "encryptAES", "decryptAES"]

app_id  = 'com.chunmi.ihcooker'

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]


def md5(src):
    return hashlib.md5(src).hexdigest().upper()

# def encryptBase64(src):
#     return str(base64.urlsafe_b64encode(src),'utf-8').strip().replace("\n", "").replace("\r", "")

def encryptBase64(src):
    return base64.urlsafe_b64encode(src).strip().replace("\n", "").replace("\r", "")

def decryptBase64(src):
    return base64.urlsafe_b64decode(src).decode('utf-8')



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
    result = encryptBase64(src)

    return result


def generateSignature(httpmethod, httpurl):
    """
    生成signature
    """
    s2 = httpmethod + "&" + httpurl + "&" + "app_id=" + app_id
    return encryptBase64(sha1(s2.encode('utf-8')))