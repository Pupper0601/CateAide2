#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import base64
import random

from Crypto.Cipher import AES

from libs.config import KEY, IV
from tools.logs import logger

# padding算法
BS = len(KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]


class AesEncrypt(object):
    def __init__(self):
        self.key = KEY
        self.mode = AES.MODE_CBC

    #加密函数
    def encrypt(self, text):
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
        #AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(self.ciphertext).decode('utf-8')

    #解密函数
    def decrypt(self, text):
        try:
            decode = base64.b64decode(text)
            cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
            plain_text = cryptor.decrypt(decode)
            return unpad(plain_text).decode('utf-8')
        except Exception as e:
            logger.error(f"解密失败: {str(e)}")
            return ""

    def random_string(self, length=16):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        return ''.join(random.choice(characters) for _ in range(length))

def test_ka():
    """试用激活码"""
    aes_encrypt = AesEncrypt()
    for i in range(100):
        day = 1
        t = "CateAide2" + "|" + str(day) + "|" + aes_encrypt.random_string(16)
        e = aes_encrypt.encrypt(t)
        print(e)

def permanent_ka():
    """永久激活码"""
    aes_encrypt = AesEncrypt()
    for i in range(100):
        day = 3650
        t = "CateAide2" + "|" + str(day) + "|" + aes_encrypt.random_string(16)
        e = aes_encrypt.encrypt(t)
        print(e)

if __name__ == '__main__':
    permanent_ka()
