#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from pathlib import Path

from libs.config import config_file_path
from tools.ace import AesEncrypt


def email_verification(email):
    import re
    pattern = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
    if re.match(pattern, email):
        return True
    return False

def code_verification(code):
    ace_list = AesEncrypt().decrypt(code).split("|")
    if ace_list[0] == "CateAide2":
        return True
    return False



if __name__ == '__main__':
    # emails = "pupper.cheng@gmail.com"
    # print(email_verification(emails))

    codes = "tSslW2IeCObGLpyWUDlaKtSHmQcxNPJoM3jREmpMSbM="
    code_verification(codes)